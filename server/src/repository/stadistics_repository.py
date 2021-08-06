from config.mongodb_connection import db
stadistics_collection = db.get_collection('stadistics')


def find(query={}, filter={'_id': 0}):
    stadistics = stadistics_collection.find(query, filter)
    return [stadistic for stadistic in list(stadistics)]
