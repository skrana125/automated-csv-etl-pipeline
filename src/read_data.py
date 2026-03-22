import pandas as pd

def read_data(file):

    try:

        df = pd.read_csv(file)

        return df

    except Exception as e:

        print("Error reading file:",e)

        return None
