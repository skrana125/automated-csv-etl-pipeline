def generate_report(df):

    report=f"""

Total records : {len(df)}

Average spending : {df['spending'].mean()}

Max spending : {df['spending'].max()}

Min spending : {df['spending'].min()}

"""

    return report



def data_profile(df):

    profile=f"""

Columns : {list(df.columns)}

Null values :

{df.isnull().sum()}

Data types :

{df.dtypes}

"""

    return profile
