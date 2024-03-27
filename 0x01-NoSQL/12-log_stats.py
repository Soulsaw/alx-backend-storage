#!/usr/bin/env python3
"""Doc module"""
from pymongo import MongoClient
"""Doc import modele"""


def get_logs_stats(collection):
    """Get total number of logs"""
    total_logs = collection.count_documents({})
    """Count logs by method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    """Count logs with method=GET and path=/status"""
    s_count = collection.count_documents({"method": "GET", "path": "/status"})

    return total_logs, method_counts, s_count


if __name__ == "__main__":
    """Connect to MongoDB"""
    client = MongoClient()
    db = client['logs']
    collection = db['nginx']

    """Get logs stats"""
    total_logs, method_counts, s_count = get_logs_stats(collection)

    # Print stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{s_count} status check")
