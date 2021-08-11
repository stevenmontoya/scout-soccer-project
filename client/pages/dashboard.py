import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from styles import add_button_style
from api.stadistics_api import get_all


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
        team_stadisticss = get_all()
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
    st.write("# EURO CUP 2020")

    add_button_style()

    goal_button, goal_conceded_button, possession_button, shots_button, cards_button, extra_time_button, heat_map_button = st.beta_columns(
        7)

    teams = get_all('team')

    draw_conditional_button(goal_button, 'Goals',
                            'goal_scored', teams, 'Total goals', get_all)

    draw_conditional_button(goal_conceded_button, 'Goals conceded',
                            'goal_conceded', teams, 'Total goals', get_all)

    draw_conditional_button(possession_button, 'Mean possession',
                            'mean_possession', teams, 'Possession', get_all)

    draw_conditional_button(shots_button, 'Total shots',
                            'shots', teams, 'Total shots', get_all)

    draw_conditional_button(cards_button, 'Total cards',
                            'yellow_cards', teams, 'Total cards', get_all)

    draw_conditional_button(extra_time_button, 'Extra times',
                            'extra_times', teams, 'Extra times', get_all)

    draw_heat_map_corr(heat_map_button)
