from requests.models import Response
import api.instance as api_instance
import api.utils.response as parse

urlBase = 'http://localhost:8000/stadistics'


def get_all(key=None):
    team_stadistics = api_instance.get(urlBase)
    return parse.list_response(team_stadistics, key)


def get_stadistics_team(team):
    return api_instance.get(f'{urlBase}/teams/{team}')
