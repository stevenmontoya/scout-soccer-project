import streamlit as st
import plotly.graph_objects as go
from components.title_component import title_component
from api.stadistics_api import get_all, get_stadistics_team


def draw_compare_page():
    title_component()

    team_1, team_2 = st.beta_columns(2)

    team_a = team_1.selectbox(
        'Select Team A', get_all('team'))

    team_b = team_2.selectbox(
        'Select Team B', get_all('team'))

    if ((team_a) and (team_b)):
        col1, col2, col3, col4 = st.beta_columns(4)

        team_s_a = get_stadistics_team(team_a)

        team_s_b = get_stadistics_team(team_a)

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
