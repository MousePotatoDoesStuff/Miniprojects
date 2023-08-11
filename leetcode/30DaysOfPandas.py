import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res=pd[pd['area']>3000000 and pd['population']>25000000]
    return res

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len()>15][["tweet_id"]]

def main():
    big_countries()
    return


if __name__ == "__main__":
    main()
