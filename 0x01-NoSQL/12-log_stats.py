#!/usr/bin/env python3
"""log stats module that provides some stats about nginx
logs stored in MongoDB"""


from pymongo import MongoClient


def get_log_stats(nginx_collection):
    """ A function that gets the status"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def main():
    """The main function that has the mongo client"""
    client = MongoClient('mongodb://127.0.0.1:27017')

    get_log_stats(client.logs.nginx)


if __name__ == '__main__':
    main()
