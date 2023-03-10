from pymongo import MongoClient


class MongoInterface:
    def __init__(self, db_name, host=None, port=None, connection_url=None):
        if connection_url:
            self.client = MongoClient(connection_url)
        if host and port:
            self.client = MongoClient(host, port)

        self.db = self.client[db_name]

    def insert(self, collection, document):
        self.db[collection].insert_one(document)

    def find(self, collection, query):
        return self.db[collection].find(query)

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def update(self, collection, query, document):
        self.db[collection].update_one(query, document)

    def delete(self, collection, query):
        self.db[collection].delete_one(query)

    def delete_many(self, collection, query):
        self.db[collection].delete_many(query)

    def drop(self, collection):
        self.db[collection].drop()

    def get_all(self, collection):
        return self.db[collection].find()

    def get_all_sorted(self, collection, sort_key, sort_order):
        return self.db[collection].find().sort(sort_key, sort_order)

    def get_all_sorted_limit(self, collection, sort_key, sort_order, limit):
        return self.db[collection].find().sort(sort_key, sort_order).limit(limit)

    def get_all_sorted_limit_skip(self, collection, sort_key, sort_order, limit, skip):
        return self.db[collection].find().sort(sort_key, sort_order).limit(limit).skip(skip)

    def get_all_limit(self, collection, limit):
        return self.db[collection].find().limit(limit)

    def get_all_limit_skip(self, collection, limit, skip):
        return self.db[collection].find().limit(limit).skip(skip)

    def get_all_skip(self, collection, skip):
        return self.db[collection].find().skip(skip)

    def get_all_sorted_limit_skip_projection(self, collection, sort_key, sort_order, limit, skip, projection):
        return self.db[collection].find(projection=projection).sort(sort_key, sort_order).limit(limit).skip(skip)

    def get_all_sorted_limit_projection(self, collection, sort_key, sort_order, limit, projection):
        return self.db[collection].find(projection=projection).sort(sort_key, sort_order).limit(limit)

    def get_all_sorted_projection(self, collection, sort_key, sort_order, projection):
        return self.db[collection].find(projection=projection).sort(sort_key, sort_order)