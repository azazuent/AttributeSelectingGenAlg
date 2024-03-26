import pandas as pd
import numpy as np


def get_titanic_data() -> (pd.DataFrame, pd.Series):
    data = pd.read_csv("datasets/titanic.csv", header=0)

    target = data["Survived"]
    data = data.drop(columns="Survived")
    return data, target


processed_data = get_titanic_data()
#print(processed_data[0])
#print(processed_data[1])
