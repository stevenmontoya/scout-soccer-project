import api.instance as api_instance


urlBase = 'http://localhost:8000/squads'


def get_squad(team):
    response = api_instance.get(f'{urlBase}/{team}')
    return response.json()
