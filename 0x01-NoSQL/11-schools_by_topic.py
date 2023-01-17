#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """Gets the documents in the collection that have the specified topic"""
    return mongo_collection.find({"topics": topic})
