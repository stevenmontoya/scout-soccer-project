from config.mongodb_connection import db
squads_collection = db.get_collection('squads')


def find_squad(team_name, filter={'_id': 0}):
    team = squads_collection.find_one({'name': team_name}, filter)
    return team
