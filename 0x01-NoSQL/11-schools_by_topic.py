#!/usr/bin/env python3
"""Doc module"""


def schools_by_topic(mongo_collection, topic):
    """Doc of the function"""
    document = mongo_collection.insert_one(topic)
    return document.inserted_id
