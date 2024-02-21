import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res=pd[pd['area']>3000000 and pd['population']>25000000]
    return res

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len()>15][["tweet_id"]]

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match("[a-zA-Z][a-z0-9A-Z_.-]*@leetcode\.com")]

def wrong_rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    def get_lowest(row):
        vn_pairs=[(row[e], e) for e in ['store1', 'store2', 'store3'] if pd.notna(row[e])]
        vn_pairs.sort()
        return vn_pairs[0][1] if vn_pairs else None
    def use_lowest(row):
        store_col=row['store']
        if pd.notna(store_col):
            return row[store_col]
        return None
    products['store']=products.apply(get_lowest,axis=1)
    #products['price']=products.apply(use_lowest,axis=1)
    return products#.drop(columns=['store1','store2','store3'])

def main():
    big_countries()
    return


if __name__ == "__main__":
    main()
