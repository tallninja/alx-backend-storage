#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    """Gets all documents in the collection"""
    mongo_collection.insert_one({"name": "UCSD"})
    doc = mongo_collection.find()

    doc_list = list(doc)
    if doc == 0:
        return []
    return doc_list
