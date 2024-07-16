#!/usr/bin/env python3
""" inser_school module that inserts a new document"""


def insert_school(mongo_collection, **kwargs):
    """A function that inserts a new document in a collection
    based on kwargs
    Return: The new _id
    """
    new_doc_id = mongo_collection.insert_one(kwargs)
    return new_doc_id.inserted_id
