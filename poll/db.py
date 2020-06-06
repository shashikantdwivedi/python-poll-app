import pymongo

# TODO - Replace DATABASE-URL with your mongoDB database URL
db_connection = pymongo.MongoClient(
    "DATABASE-URL")
database = db_connection["polls"]
presidential = database["presidential"]
