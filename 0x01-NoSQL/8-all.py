#!/usr/bin/env python3
""" all module that lists all documents in a collection """


def list_all(mongo_collection):
    """ A function that lists all documents in a collection
    Return: empty list if no document in the collection
    """
    return ([document for document in mongo_collection.find()])
