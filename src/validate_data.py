def validate(df):

    errors=[]

    if 'customer_id' not in df.columns:

        errors.append("customer_id missing")

    if df['age'].min()<0:

        errors.append("Invalid age")

    return errors
