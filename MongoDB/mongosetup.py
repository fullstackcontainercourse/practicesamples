import pymongo

MONGO_DB_CONNECTION_STRING = "mongodb://localhost:27017/"
DATABASE_NAME = "Library"


def getCollectionsFromLibraryDB(collectionTableName):

    mongoClient = pymongo.MongoClient(MONGO_DB_CONNECTION_STRING)

    database = mongoClient[DATABASE_NAME]

    collections = database[collectionTableName]

    return collections
