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
                "_id": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": "$_id",
                "averageScore": 1
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
