import pymongo


def get_database():
    CONNECTION_STRING = "mongodb+srv://mauritsseelen:aZRnLIqimOAe4IoV@cluster0.fah1h2e.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(CONNECTION_STRING)

    return client['mor']


if __name__ == "__main__":
    dbname = get_database()
