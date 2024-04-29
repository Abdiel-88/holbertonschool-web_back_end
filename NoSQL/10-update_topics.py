#!/usr/bin/env python3
""" Module for updating topics in a school document in MongoDB. """

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    
    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to be set for the school.

    Returns:
        None; the function updates the document in the database.
    """
    # Update the document where the name matches the provided name.
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
