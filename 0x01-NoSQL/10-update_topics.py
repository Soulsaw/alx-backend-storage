#!/usr/bin/env python3
"""Doc module"""


def update_topics(mongo_collection, name, topics):
    """Doc of the function"""
    document = mongo_collection.update_(topics)
    return document.inserted_id
