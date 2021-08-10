from main import app
from fastapi import Body
from repository.stadistics_repository import find_all
from repository.stadistics_repository import find_team
from repository.stadistics_repository import save_all


@app.post('/stadistics', status_code=201)
async def list_stadistics(teams_stadistics=Body(...)):
    return save_all(teams_stadistics)


@app.get('/stadistics', status_code=200)
async def list_stadistics():
    return find_all()


@app.get('/stadistics/teams/{team_name}', status_code=200)
async def list_teams(team_name: str):
    return find_team(team_name)
