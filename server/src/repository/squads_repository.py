from config.mongodb_connection import db
squads_collection = db.get_collection('squads')


def save_all(squads):
    squads_collection.insert(squads)
    return {}


def find_squad(team_name, filter={'_id': 0}):
    return squads_collection.find_one({'name': team_name}, filter)
