import pandas as pd
import matplotlib.pyplot as plt
from sklearn.calibration import LabelEncoder
from sklearn.linear_model import LinearRegression
import seaborn as sns

t1_data: pd.DataFrame = pd.DataFrame()

def define_vectors():
    t1_data["street"] = [80, 98, 75, 91, 78]
    t1_data["garage"] = [100, 82, 105, 89, 102]
    
    street = t1_data["street"].values
    garage = t1_data["garage"].values
    return (street, garage)

def show_correlation():
    print(t1_data["garage"].corr(t1_data["street"]))
    
def show_scatter(street, garage):
    plt.scatter(street, garage, marker = 'o', color = 'black')
    plt.xlabel("Street")
    plt.ylabel("Garage")
    plt.title("Диаграмма рассеивания")
    plt.show()  # doctest: +ELLIPS
    

def task1():
    (street, garage) = define_vectors()
    show_correlation()
    show_scatter(street, garage)
    
    
def show_correlation(data: pd.DataFrame):
    # corr1 = data.corrwith(data)
    print(data.corr())
    # print(data.corr().sort_values(ascending=False, by=data.columns.to_list()))
    
def pre_process_data(data: pd.DataFrame) -> pd.DataFrame:
    le = LabelEncoder()
    data["review"].fillna("empty", inplace=True)
    
    for column in data.columns:
        if data[column].dtype == 'object':
        # Примените кодирование только к колонкам с типом 'object' (строки)
            data[column] = le.fit_transform(data[column])
    

    del data["id"]
    del data["steam_purchase"]
    del data["language"]
    del data["written_during_early_access"]
    
    return data

def task2():
    data: pd.DataFrame = pd.read_csv("pr4\elden_ring_steam_reviews.csv")
    data = pre_process_data(data)
    show_correlation(data)
    

#task1()
task2()