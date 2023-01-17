#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """Updates the document with the specified name and sets the topic list"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
