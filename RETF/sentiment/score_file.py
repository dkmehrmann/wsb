
# If you quit before completing the exercise, you point the `infile` 
# argument to the `outfile` so you may pick up where you left off.

# the file for scoring
infile = "data_for_scoring_wallstreetbets_2016-01-01_2016-06-01_True_Andrew.csv"
# the output file (can be same as input file)
outfile = "output_andrew.csv"

import pandas as pd

def print_message(row):
    print("\n-------------------")
    print(row.text)
    print("")
    print("Symbol: {0}".format(row.ticker))
    print("")
    print("1: Positive (bullish)")
    print("2: Negative (bearish)")
    print("3: Not Sure/Wrong Ticker")
    print("4: Exit")
    

if __name__ == '__main__':
    
    df = pd.read_csv(infile, index_col=0)
    
    for ix, row in df.iterrows():
        if row.score == 'unk':
            while True:
                print_message(row)
                inp = input("Input: ")
                if not inp in ['1', '2', '3', '4']:
                    print('thats not valid, try again')
                else:
                    break
            if inp == '4':
                break
            df.loc[ix, 'score'] = ['bull', 'bear', 'usr_unk'][int(inp)-1]

    df.to_csv(outfile)