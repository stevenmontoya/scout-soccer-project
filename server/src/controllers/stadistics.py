from main import app
from repository.stadistics_repository import find
from repository.stadistics_repository import find_team


@app.get('/stadistics', status_code=200)
async def list_stadistics():
    stadistics = find({}, {'_id': 0})
    return [stadistic for stadistic in list(stadistics)]


@app.get('/stadistics/teams/{team_name}', status_code=200)
async def list_teams(team_name: str):
    if team_name:
        team = find_team(team_name)
        return team
    return {}
