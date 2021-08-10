import streamlit as st
from pages.teams import draw_teams_page
from pages.compare import draw_compare_page
from pages.dashboard import draw_dash_board
from styles import add_general_styles

page = st.sidebar.selectbox("Select page", ["Dashboard", "Teams", "Compare"])

add_general_styles()

if page == 'Teams':
    draw_teams_page()
elif page == 'Compare':
    draw_compare_page()
else:
    draw_dash_board()
