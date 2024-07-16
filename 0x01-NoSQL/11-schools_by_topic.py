#!/usr/bin/env python
"""" schools_by_topics module that returns the list of school
having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ A function that returns the list of school having
    a specific topic"""
    filter_topics = mongo_collection.find(
            {"topics": topic})
    return [document for document in filter_topics]
