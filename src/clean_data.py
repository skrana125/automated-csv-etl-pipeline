def clean_data(df):

    df=df.drop_duplicates()

    df['city']=df['city'].fillna("Unknown")

    df['age']=df['age'].fillna(df['age'].mean())

    df['spending']=df['spending'].fillna(0)

    return df
