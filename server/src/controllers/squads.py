from main import app
from fastapi import Body
from repository.squads_repository import find_squad
from repository.squads_repository import save_all


@app.post('/squads', status_code=201)
async def list_stadistics(squads=Body(...)):
    return save_all(squads)


@app.get('/squads/{team_name}', status_code=200)
async def list_squads(team_name):
    team_squad = find_squad(team_name, {'_id': 0, 'squad': 1})
    return team_squad['squad']
