#!/usr/bin/env python3
""" Module for querying schools by topic in a MongoDB collection. """


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns a list of schools
    in the collection that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for within the school documents.

    Returns:
        A list of schools that have the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
