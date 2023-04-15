import pandas as pd


def getDataSet():
    df = pd.read_csv(r"/Users/sayantankundu/Downloads/data01.csv")
    df.dropna(inplace=True)
    data = df.head()
    arr_data = data[["ID", "age", "heart rate",
                     "hypertensive", "diabetes", "depression"]].to_numpy(dtype='int', na_value=-1)
    return arr_data
