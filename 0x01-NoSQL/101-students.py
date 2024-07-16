#!/usr/bin/env python3
"""top_student module that returns all students sorted by
average score"""


def top_students(mongo_collection):
    """A function that returns all students sorted by
    average score"""
    pipeline = [
            {
                '$project': {
                    'name': 1,
                    'scores': 1,
                    'averageScore': {'$avg': '$scores'}
                    }
                },
            {
                '$sort': {'averageScore': -1}
                }
            ]

    cursor = mongo_collection.aggregate(pipeline)

    results = [{'name': doc['name'], 'averageScore': doc['averageScore']} for doc in cursor]

    return results
