#!/usr/bin/env python3
"""9-insert_school"""


def insert_school(mongo_collection, **kwargs):
    """Create the document from the key-value arguments"""
    doc = {}
    for key, value in kwargs.items():
        doc[key] = value
    result = mongo_collection.insert_one(doc)
    return result.inserted_id
