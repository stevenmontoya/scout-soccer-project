from main import app
from repository.stadistics_repository import find_all
from repository.stadistics_repository import find_team


@app.get('/stadistics', status_code=200)
async def list_stadistics():
    return find_all()


@app.get('/stadistics/teams/{team_name}', status_code=200)
async def list_teams(team_name: str):
    return find_team(team_name)
