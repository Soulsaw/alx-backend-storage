#!/usr/bin/env python3
"""Doc module"""


def top_students(mongo_collection):
    """Document the function"""
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
