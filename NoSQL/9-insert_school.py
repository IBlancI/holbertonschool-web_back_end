#!/usr/bin/env python3
"""
Insert a document into a collection
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.my_db.school
    new_id = insert_school(collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_id))
