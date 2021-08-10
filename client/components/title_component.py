import streamlit.components.v1 as components


def title_component():
    return components.html("""
        <style>
            .title {
                margin-left: 40%;
                color: white;
                font-family: "IBM Plex Sans", sans-serif;
            }

        </style>
        <h1 class="title"> Compare Teams </h1>
    """)
