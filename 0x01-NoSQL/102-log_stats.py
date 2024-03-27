#!/usr/bin/env python3
"""Doc module"""
from pymongo import MongoClient


def get_logs_stats(mongo_collection):
    # Get total number of logs
    total_logs = mongo_collection.count_documents({})

    # Count logs by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = mongo_collection.count_documents({"method": method})

    # Count logs with method=GET and path=/status
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    return total_logs, method_counts, status_check_count

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient()
    db = client['logs']
    collection = db['nginx']

    # Get logs stats
    total_logs, method_counts, status_check_count = get_logs_stats(collection)

    # Print stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
