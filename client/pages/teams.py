import streamlit as st
import requests


def get_data_from_stadistics(key):
    response = requests.get('http://localhost:8000/stadistics')
    team_stadistics = response.json()
    return [stadistic[key] for stadistic in team_stadistics]


def draw_teams_page():
    team = st.selectbox('', get_data_from_stadistics('team'))
    if (team):
        draw_team_info(team)


def draw_team_info(team):
    response = requests.get(f'http://localhost:8000/stadistics/teams/{team}')
    team_stadisticss = response.json()
    team = Team(team_stadisticss)
    team.draw_info()


def draw_player(team):
    response = requests.get(f'http://localhost:8000/squads/{team}')
    squad = response.json()
    players = [Player(player) for player in squad]

    pc_1, pc_2, pc_3, pc_4 = st.beta_columns(4)

    with pc_1:
        for player in players[0:7]:
            player.draw()
    with pc_2:
        for player in players[7:14]:
            player.draw()
    with pc_3:
        for player in players[14:21]:
            player.draw()
    with pc_4:
        for player in players[21:28]:
            player.draw()


class MapperDict(object):
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)


class Player(MapperDict):
    def __init__(self, iterable=(), **kwargs):
        super().__init__(iterable, **kwargs)

    def draw(self):
        if(st.button(self.name)):
            st.write('Player stadistics')


class Team(MapperDict):
    def __init__(self, iterable=(), **kwargs):
        super().__init__(iterable, **kwargs)

    def draw_info(self):
        col1, col2, col3 = st.beta_columns(3)

        with col1:
            st.write(f' ### Possession: ', self.mean_possession)
            st.write(f' ### Goals: ', self.goal_scored)
            st.write(f' ### Goals: conceded ', self.goal_conceded)
        with col2:
            st.write(f' ### Penalties: ', self.penalties)
            st.write(f' ### Shots: ', self.shots)

        with col3:
            st.write(f' ### Leading Score:  ', self.top_scored)
            st.write(f' ### Cards: ', self.mean_possession)
            st.write(f' ### Extra times: ', self.extra_times)

        m = st.markdown("""
        <style>
            div.stButton > button:first-child {
                margin-top: 4em;
                margin-left: 40%;
            }
        </style>""", unsafe_allow_html=True)
        if (st.button('View Squad')):
            draw_player(self.team)
