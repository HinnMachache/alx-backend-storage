#!/usr/bin/env python3
"""
def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """ Function that updates a collection """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
