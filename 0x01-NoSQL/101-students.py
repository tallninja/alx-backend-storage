#!/usr/bin/env python3
"""101-students.py"""


def top_students(mongo_collection):
    """This function returns all students sorted by average score"""
    doc = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
    return list(doc)
