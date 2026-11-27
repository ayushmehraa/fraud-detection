from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(X:pd.DataFrame, y:pd.Series):
   
    X_train, X_test ,y_train, y_test = train_test_split(X,y,test_size=0.2, stratify=y, random_state=42)
   
    return X_train, X_test, y_train, y_test

