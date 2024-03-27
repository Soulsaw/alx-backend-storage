#!/usr/bin/env python3
"""Doc module"""


def list_all(mongo_collection):
    """Doc of the function"""
    documents = list(mongo_collection.find({}))
    return documents
