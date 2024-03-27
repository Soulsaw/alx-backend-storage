#!/usr/bin/env python3
"""Doc module"""


def schools_by_topic(mongo_collection, topic):
    """Doc of the function"""
    documents = mongo_collection.find({"topics": topic})
    return documents
