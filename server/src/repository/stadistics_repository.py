from config.mongodb_connection import db
stadistics_collection = db.get_collection('stadistics')


def save_all(team_stadistics):
    stadistics_collection.insert(team_stadistics)
    return {}


def find_all(query={}, filter={'_id': 0}):
    stadistics = stadistics_collection.find(query, filter)
    return [stadistic for stadistic in list(stadistics)]


def find_team(team_name, filter={'_id': 0}):
    team = stadistics_collection.find_one({'team': team_name}, filter)
    return team
