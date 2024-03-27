#!/usr/bin/env python3
"""Doc module"""
from pymongo import MongoClient
from collections import Counter
"""Doc import"""


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
    ips_counter = Counter(doc['ip'] for doc in collection.find())
    tops_ips = ips_counter.most_common(10)

    return total_logs, method_counts, s_count, tops_ips


if __name__ == "__main__":
    """Connect to MongoDB"""
    client = MongoClient()
    db = client['logs']
    collection = db['nginx']

    """Get logs stats"""
    total_logs, method_counts, s_count, tops_ips = get_logs_stats(collection)

    # Print stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{s_count} status check")
    print('IPs:')
    for ip, count in tops_ips:
        print(f"\t{ip}: {count}")
