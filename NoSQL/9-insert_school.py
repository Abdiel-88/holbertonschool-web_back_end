#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a
    collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Arbitrary keyword arguments that define the document fields.

    Returns:
        The new document's _id.
    """
    # The insert_one method is used to insert a new document.
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id  # This returns the ObjectId of the new document.
