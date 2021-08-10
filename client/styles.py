import streamlit as st


def add_button_style():
    return st.markdown("""
        <style>
            div.stButton > button:first-child {
                background-color: rgb(23, 180, 207);
            }
        </style>
            """, unsafe_allow_html=True)


def add_general_styles():
    return st.markdown(
        """
        <style>
            .reportview-container .main .block-container{
                max-width: 80%;
            }

            #MainMenu {
                visibility: hidden;
            }

            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
