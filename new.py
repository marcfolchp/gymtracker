import pandas as pd
from datetime import date
import warnings
import seaborn as sns

warnings.filterwarnings("ignore")

def table(bodypart, exercise, weight, repetitions):

    from datetime import date
    
    thetable = pd.read_csv("table.csv")

    date = date.today().strftime("%d/%m/%Y")
    score = weight + (repetitions * 0.3)

    newrow = {"Date":date, "Training":bodypart, "Exercise":exercise, "Weight":weight, "Repetitions":repetitions, "Score":score}
    newrow = pd.DataFrame(newrow, index=[0])
    thetable = pd.concat([thetable, newrow])
    
    return thetable.to_csv("table.csv", index=False)

def graph(exercise):

    graph = pd.read_csv("table.csv")
    
    graphs = graph[graph["Exercise"]==exercise][["Date", "Score"]].groupby("Date").mean()