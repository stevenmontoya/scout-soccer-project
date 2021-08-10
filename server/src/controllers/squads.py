from main import app
from repository.squads_repository import find_squad


@app.get('/squads/{team_name}', status_code=200)
async def list_squads(team_name):
    team_squad = find_squad(team_name, {'_id': 0, 'squad': 1})
    return team_squad['squad']
