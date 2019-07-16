# pandas 실습

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def read_dataset():
    return pd.read_csv('iris.csv'), pd.read_csv('iris_metadata.csv')

def merge_dfs(iris, metadata):
    ### complete here 1줄
    return pd.merge(iris,metadata, left_on='species', right_on='name')

def split_df(df, ratio):
    ### complete here 2줄
    # X_train = df.sample(frac= ratio, random_state =1)
    # X_test = df.drop(X_train.)
    splited_index = round(len(df)*ratio)
    return df.iloc[:splited_index], df.iloc[splited_index:]

def truncate_non_toxics(df):
    ### complete here 1줄
    return df.loc[df['toxic'] > 0]   # df.loc가 뭐지??

def main():
    split_ratio = 0.7
    iris, metadata = read_dataset()
    ### complete here
    sum_df = merge_dfs(iris, metadata)
    train_df, test_df = split_df(sum_df, split_ratio)
    train_df = truncate_non_toxics(train_df)
    test_df= truncate_non_toxics(test_df)

    print(train_df.describe())
    print(test_df.describe())


main()




