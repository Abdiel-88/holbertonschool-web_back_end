#!/usr/bin/env python3
""" Module to generate statistics from Nginx logs stored in MongoDB. """

from pymongo import MongoClient

def log_stats():
    """ Function to print stats about Nginx logs. """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Total documents/logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count by methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"    method {method}: {count}")

    # Count of documents where method is GET and path is /status
    status_checks = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()
