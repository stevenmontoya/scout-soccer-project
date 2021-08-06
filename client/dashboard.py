import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px


def get_data_from_stadistics(key):
    return [stadistic[key] for stadistic in team_stadistics]


def draw_bar(x_data, y_data, title):
    fig = go.Figure(go.Bar(
        x=x_data,
        y=y_data,
        orientation='h'))

    fig.layout.plot_bgcolor = '#141414'
    fig.layout.title = title

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


def draw_dash_board():
    teams = get_data_from_stadistics('team')

    draw_conditional_button(goal_button, 'Goals',
                            'goal_scored', teams, 'Total goals', get_data_from_stadistics)

    draw_conditional_button(possession_button, 'Mean possession',
                            'mean_possession', teams, 'Possession', get_data_from_stadistics)

    draw_conditional_button(shots_button, 'Total shots',
                            'shots', teams, 'Total shots', get_data_from_stadistics)

    draw_conditional_button(cards_button, 'Total cards',
                            'yellow_cards', teams, 'Total cards', get_data_from_stadistics)


st.write("# EURO CUP 2020")
response = requests.get('http://localhost:8000/stadistics')
team_stadistics = response.json()

st.markdown(""" <style> div.stButton > button:first-child {
  background-color: rgb(23, 180, 207);
} </style>""", unsafe_allow_html=True)


goal_button, possession_button, shots_button, cards_button = st.beta_columns(4)

draw_dash_board()
