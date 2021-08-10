import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components
import pandas as pd


def get_data_from_stadistics(key):
    return [stadistic[key] for stadistic in team_stadistics]


def draw_bar(x_data, y_data, title):
    fig = go.Figure(go.Bar(
        x=x_data,
        y=y_data,
        orientation='h'))

    fig.layout.plot_bgcolor = '#141414'
    fig.layout.title = title
    fig.update_layout(
        autosize=False,
        width=1200,
        height=800,)

    st.plotly_chart(fig, config={
        'displayModeBar': False
    })


def draw_pie(data, values, names, title):
    pie = px.pie(data, values=values, names=names,
                 title=title)

    st.plotly_chart(pie, config={
        'displayModeBar': False
    })


def draw_conditional_button(button, buttonId, query, y_data,  title, fn):
    if (button.button(buttonId)):
        x_data = fn(query)
        draw_bar(x_data, y_data, title)


def draw_heat_map_corr(button):
    if (button.button('Heat map')):
        response = requests.get(
            f'http://localhost:8000/stadistics')
        team_stadisticss = response.json()
        df = pd.DataFrame.from_records(team_stadisticss)
        df = df.set_index('team')
        df = df.drop('top_scored', axis=1)
        fig = px.imshow(df.corr())
        fig.update_layout(
            autosize=False,
            width=1200,
            height=800,)
        st.plotly_chart(fig, config={'displayModeBar': False})


def draw_dash_board():
    teams = get_data_from_stadistics('team')

    draw_conditional_button(goal_button, 'Goals',
                            'goal_scored', teams, 'Total goals', get_data_from_stadistics)

    draw_conditional_button(goal_conceded_button, 'Goals conceded',
                            'goal_conceded', teams, 'Total goals', get_data_from_stadistics)

    draw_conditional_button(possession_button, 'Mean possession',
                            'mean_possession', teams, 'Possession', get_data_from_stadistics)

    draw_conditional_button(shots_button, 'Total shots',
                            'shots', teams, 'Total shots', get_data_from_stadistics)

    draw_conditional_button(cards_button, 'Total cards',
                            'yellow_cards', teams, 'Total cards', get_data_from_stadistics)

    draw_conditional_button(extra_time_button, 'Extra times',
                            'extra_times', teams, 'Extra times', get_data_from_stadistics)

    draw_heat_map_corr(heat_map_button)


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


def draw_team_info(team):
    response = requests.get(f'http://localhost:8000/stadistics/teams/{team}')
    team_stadisticss = response.json()
    team = Team(team_stadisticss)
    team.draw_info()


def draw_teams_page():
    team = st.selectbox('', get_data_from_stadistics('team'))
    if (team):
        draw_team_info(team)


def draw_compare_page():
    components.html("""
        <style>
            .title {
                margin-left: 40%;
                color: white;
                font-family: "IBM Plex Sans", sans-serif;
            }

        </style>
        <h1 class="title"> Compare Teams </h1>
    """)
    team_1, team_2 = st.beta_columns(2)

    team_a = team_1.selectbox(
        'Select Team A', get_data_from_stadistics('team'))

    team_b = team_2.selectbox(
        'Select Team B', get_data_from_stadistics('team'))

    if ((team_a) and (team_b)):
        col1, col2, col3, col4 = st.beta_columns(4)

        response_team_a = requests.get(
            f'http://localhost:8000/stadistics/teams/{team_a}')
        team_s_a = response_team_a.json()

        response_team_b = requests.get(
            f'http://localhost:8000/stadistics/teams/{team_b}')
        team_s_b = response_team_b.json()

        del team_s_a['team']
        del team_s_a['top_scored']
        del team_s_b['team']
        del team_s_b['top_scored']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(r=list(team_s_a.values()), theta=list(team_s_a.keys(
        )), name=f'{team_a}'))

        fig.add_trace(go.Scatterpolar(r=list(team_s_b.values()), theta=list(team_s_b.keys(
        )), name=f'{team_b}'))

        fig.update_traces(fill='toself')
        fig.layout.plot_bgcolor = '#141414'
        fig.layout.title = 'Compare All staditics'
        fig.update_layout(autosize=False, width=600, height=600)

        col2.plotly_chart(fig, config={'displayModeBar': False})


st.write("# EURO CUP 2020")
response = requests.get('http://localhost:8000/stadistics')
team_stadistics = response.json()

st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: rgb(23, 180, 207);
    }
</style>
     """, unsafe_allow_html=True)

st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 80%;

    }}

    # MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

</style>
""",
    unsafe_allow_html=True,
)

goal_button, goal_conceded_button, possession_button, shots_button, cards_button, extra_time_button, heat_map_button = st.beta_columns(
    7)

page = st.sidebar.selectbox("Select page", ["Dashboard", "Teams", "Compare"])

if page == 'Dashboard':
    draw_dash_board()
if page == 'Teams':
    draw_teams_page()
if page == 'Compare':
    draw_compare_page()
