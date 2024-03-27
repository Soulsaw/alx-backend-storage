#!/usr/bin/env python3
"""Doc module"""


def update_topics(mongo_collection, name, topics):
    """Doc of the function"""
    mongo_collection.update_many({"name": name}, { '$set': {"topics": topics}})
