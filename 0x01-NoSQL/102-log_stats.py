#!/usr/bin/env python3
"""log stats module that provides some stats about nginx
logs stored in MongoDB"""


from pymongo import MongoClient


def get_log_stats(nginx_collection):
    """ A function that gets the status about nginx"""
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    
    print(f'{nginx_collection.count_documents({})} logs')
    
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')
        
    status = nginx_collection.count_documents({"path": "/status"})
    print(f'{status} status check')

def print_top_ips(server_collection):
    """A function that prints the top 10 IPs
    in a collection.
    """
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))

def main():
    """The main function that has the mongo client"""
    client = MongoClient('mongodb://127.0.0.1:27017')

    get_log_stats(client.logs.nginx)
    print_top_ips(client.logs.nginx)

    
if __name__ == '__main__':
    main()
