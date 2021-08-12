import streamlit as st
import plotly.graph_objects as go
from api.stadistics_api import get_all, get_stadistics_team
from api.teams_api import get_squad
from api.utils.mapper import json_to_dataframe


def draw_teams_page():
    team = st.selectbox('', get_all('team'))
    if (team):
        draw_team_info(team)


def draw_team_info(team):
    team_stadisticss = get_stadistics_team(team)
    team = Team(team_stadisticss)
    team.draw_info()


def draw_player(team):
    response = get_squad(team)
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

    def __generate_stadistic_dict__(self):
        return {'Possession': 'mean_possession', 'Goals': 'goal_scored', 'Goals conceded': 'goal_conceded',
                'Penalties': 'penalties', 'Shots': 'shots', 'Yellow Cards': 'yellow_cards', 'Red Cards': 'red_cards', 'Extra times': 'extra_times'}

    def __metric_values__(self, key, filter_tag):
        dc = self.__generate_stadistic_dict__()
        teams = get_all()
        df = json_to_dataframe(teams)

        if filter_tag == 'min':
            return df[dc[key]].min()
        elif filter_tag == 'max':
            return df[dc[key]].max()

        return df[dc[key]].mean()

    def draw_info(self):
        col1, col2, col3 = st.beta_columns(3)
        col1, col2 = st.beta_columns(2)

        stadistic_option = ''
        compare_stadistic_option = ''
        with col1:
            stadistic_option = st.selectbox('', ('Possession', 'Goals', 'Goals conceded',
                                                 'Penalties', 'Shots', 'Yellow Cards', 'Red Cards',  'Extra times'))
        with col2:
            compare_stadistic_option = st.selectbox('', ('mean', 'max', 'min'))

        compare_value = self.__metric_values__(
            stadistic_option, compare_stadistic_option)

        fig = go.Figure(go.Bar(
            x=[compare_value, self.__getattribute__(
                self.__generate_stadistic_dict__()[stadistic_option])],
            y=[f'{compare_stadistic_option}', f'{self.team}'],
            orientation='h'))

        fig.update_layout(
            autosize=False,
            width=1300,
            height=700,)

        st.plotly_chart(fig, config={
            'displayModeBar': False
        })


m = st.markdown("""
        <style>
            div.stButton > button:first-child {
                margin-top: 4em;
                margin-left: 40%;
            }
        </style>""", unsafe_allow_html=True)
