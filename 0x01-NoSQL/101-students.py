#!/usr/bin/env python3
"""Doc module"""


def top_students(mongo_collection):
    """"""
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": "name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$project": {
                "_id": "$_id",
                "averageScore": 1,
                "_id": 0
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
