import pandas as pd


def get_titanic_data() -> (pd.DataFrame, pd.Series):
    data = pd.read_csv("datasets/titanic.csv", header=0)

    target = data["Survived"]
    data = data.drop(columns="Survived")
    return data, target
