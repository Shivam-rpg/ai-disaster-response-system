import pandas as pd

def load_and_clean_data():

    messages = pd.read_csv("disaster_messages.csv.zip")
    categories = pd.read_csv("disaster_categories.csv.zip")

    df = pd.merge(messages, categories, on="id")

    categories_split = df['categories'].str.split(';', expand=True)

    row = categories_split.iloc[0]
    category_colnames = row.apply(lambda x: x[:-2])
    categories_split.columns = category_colnames

    for column in categories_split:
        categories_split[column] = categories_split[column].astype(str).str[-1]
        categories_split[column] = pd.to_numeric(categories_split[column])
        categories_split[column] = categories_split[column].apply(lambda x: 1 if x >= 1 else 0)

    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories_split], axis=1)

    df = df[[
        "message",
        "medical_help",
        "food",
        "water",
        "shelter"
    ]]

    df = df.dropna()
    df = df[df["message"].str.len() > 20]
    df["message"] = df["message"].str.lower()

    return df