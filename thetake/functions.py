def authenticator (username, password):
    import pandas as pd
    from pymongo import MongoClient
    import pandas as pd
    import streamlit_authenticator as stauth
    import hashlib

    # Replace '<your_connection_string>' with the actual connection string from MongoDB Atlas
    connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)

    # Access a specific database (replace 'your_database' with your actual database name)
    db = client.gymtracker

    # Access a specific collection within the database (replace 'your_collection' with your actual collection name)
    collection = db.users

    user = collection.find_one({"username": username, "password": hashlib.sha256(str(password).encode()).hexdigest()})

    if user:
        return True
    else:
        return False
    
def registrator (name, surname, age, username, password):
    import pandas as pd
    from pymongo import MongoClient
    import pandas as pd
    import streamlit_authenticator as stauth
    import hashlib

    # Replace '<your_connection_string>' with the actual connection string from MongoDB Atlas
    connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)

    # Access a specific database (replace 'your_database' with your actual database name)
    db = client.gymtracker

    # Access a specific collection within the database (replace 'your_collection' with your actual collection name)
    collection = db.users

    document_to_insert = {
    "name": name,
    "surname": surname,
    "age": age,
    "username": username,
    "password": hashlib.sha256(str(password).encode()).hexdigest()
    }

    collection.insert_one(document_to_insert)

def cloudation (username, bodypart, exercise, weight, repetitions, score):
    import pandas as pd
    from pymongo import MongoClient
    import pandas as pd
    import streamlit_authenticator as stauth
    import hashlib
    from datetime import date

    # Replace '<your_connection_string>' with the actual connection string from MongoDB Atlas
    connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)

    # Access a specific database (replace 'your_database' with your actual database name)
    db = client.gymtracker

    # Access a specific collection within the database (replace 'your_collection' with your actual collection name)
    collection = db.data

    document_to_insert = {
    "date": date.today().strftime("%d/%m/%Y"),
    "username": username,
    "bodypart": bodypart,
    "exercise": exercise,
    "weight": weight,
    "repetitions": repetitions,
    "score": score
    }

    collection.insert_one(document_to_insert)

def exercises (username):
    import pandas as pd
    from pymongo import MongoClient
    import pandas as pd
    import streamlit_authenticator as stauth
    import hashlib
    from datetime import date

    connection_string = "mongodb+srv://marcfolchpomares:AstonMartin1@mycluster.e19nlo1.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)

    # Access a specific database (replace 'your_database' with your actual database name)
    db = client.gymtracker

    # Access a specific collection within the database (replace 'your_collection' with your actual collection name)
    collection = db.data

    cursor = collection.find()

    # Convert the cursor to a list of dictionaries
    data = list(cursor)

    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Now 'df' contains your MongoDB collection data in a Pandas DataFrame
    username_filter = df[df["username"] == username]
    username_bodypart = username_filter.exercise.unique().tolist()
    return username_bodypart