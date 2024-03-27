#!/usr/bin/env python3
"""Doc module"""


def insert_school(mongo_collection, **kwargs):
    """Doc of the function"""
    document = mongo_collection.insert_one(kwargs)
    return document['_id']
