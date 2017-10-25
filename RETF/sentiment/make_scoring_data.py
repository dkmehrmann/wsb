
start_date = '2016-01-01'
end_date = '2016-06-01'
dollar_sign = True
subreddit = 'wallstreetbets'
total_N = 600

fname = 'data_for_scoring_{0}_{1}_{2}_{3}_{4}.csv'

import sys
sys.path.insert(0, '../..')
from RETF.reddit_scraper.scrape import SubScraper
from RETF.portfolio.get_stats import Post, unix_to_datetime
import pandas as pd
from RETF.portfolio.match_tickers import SymbolFinder
from RETF.portfolio.index import make_ticker_list
import numpy as np


def format_labeling_data(submission):
    p = Post(submission)
    # create text the same way it will be created in prod
    p.create_text() 
    # return filtered tokens
    return unix_to_datetime(submission.created_utc), p.text, sf.get_primary_ticker(p.text), 'unk'

if __name__ == '__main__':

    sf = SymbolFinder(make_ticker_list(['../../data/nyse.csv', '../../data/nasdaq.csv']), dollar_sign=dollar_sign)
    
    scraper = SubScraper("../../RETF/credentials.txt")
    
    submissions=scraper.get_submissions_between(subreddit, start_date, end_date)
    
    df = pd.DataFrame([format_labeling_data(x) for x in submissions], columns=['date', 'text', 'ticker', 'score'])
    
    df['scorer'] = np.random.choice(['Andrew','Joe','Casey'], len(df))
    
    df = df.loc[df.ticker.notnull()]
    
    df = df.sample(total_N)
    
    for person in ['Andrew', 'Joe', 'Casey']:
        df[df.scorer == person].to_csv(fname.format(subreddit, start_date, end_date, dollar_sign, person))