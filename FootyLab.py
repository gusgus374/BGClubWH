# Copyright (c) [2024] DataRook, Inc. All rights reserved.
# This source code is licensed under the license found in the
# LICENSE.md file in the root directory of this source tree.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
from streamlit_ace import st_ace
import streamlit.components.v1 as components
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns

st.set_page_config(
    page_title="footyLab • Play to Learn | DataRook, Inc.",
    page_icon="./media/footylab_v2_icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://datarook.com/contact',
        'About': "## This is a demo version of footyLab. Contact gus@datarook.com to learn more"
    }
)

if "user" not in st.session_state:
    st.session_state.user = None
#if "password" not in st.session_state:
#     st.session_state.password = None

ROLES = [None,"Coach Gus", "Max", "Edgar", "Gaspar", "Lilly", "Colton", "Ja'zyrion", "Saboji", "Julian Gowens", "Player 9", "Player 10", "Player 11", "Player 12", "Player 13", "Player 14", "Player 15", "Player 16", "Player 17", "Player 18", "Player 19", "Player 20"]
allroles = ["Coach Gus", "Max", "Edgar", "Gaspar", "Lilly", "Colton", "Ja'zyrion", "Saboji", "Julian Gowens", "Player 9", "Player 10", "Player 11", "Player 12", "Player 13", "Player 14", "Player 15", "Player 16", "Player 17", "Player 18", "Player 19", "Player 20"]
playersdeployed = ["Coach Gus", "Saboji", "Lilly"]
def login():

    st.header("Log in")
    user = st.selectbox("User", ROLES)
    #password = st.text_input("Password")

    if st.button("Log in"):
        st.session_state.user = user
        #st.session_state.password = password
        st.rerun()


def logout():
    st.session_state.user = None
    #st.session_state.password = None
    st.rerun()


user = st.session_state.user
#password = st.session_state.password

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

BootRoom = st.Page(
    "./coach/1_BootRoom.py",
    title="BootRoom",
    icon=":material/interactive_space:",
)
coachGus = st.Page(
    "./coach/coachGus.py", title="Coach's Examples", icon=":material/sports:",default=(user == "Coach Gus")
)
classpage = st.Page(
    "./coach/Class_Page.py",
    title="Class Page",
    icon=":material/school:"
)

codeBox = st.Page(
    "./coach/codeBox.py", title="", icon=":material/person_play:",default=(user not in playersdeployed)
)
prosoccer = st.Page(
    "./coach/2_US_Pro_Soccer.py",
    title="Pro Soccer Data",
    icon=":material/sports_and_outdoors:",
)

example1 = st.Page(
    "./coach/example1.py",
    title="My First Soccer Data App!",
    icon=":material/school:"
)
example2 = st.Page(
    "./coach/example2.py",
    title="Soccer Distance Calculator",
    icon=":material/school:"
)
example3 = st.Page(
    "./coach/example3.py",
    title="Soccer Speed Converter",
    icon=":material/school:"
)
example4 = st.Page(
    "./coach/example4.py",
    title="Soccer Stats Chart Maker",
    icon=":material/school:"
)

example5 = st.Page(
    "./coach/example5.py",
    title="Sprint Counter",
    icon=":material/school:"
)

example6 = st.Page(
    "./coach/example6.py",
    title="Soccer Calendar",
    icon=":material/school:"
)

example7 = st.Page(
    "./coach/example7.py",
    title="Speed and Distance Calculator",
    icon=":material/school:"
)

example8 = st.Page(
    "./coach/example8.py",
    title="Power Plays Counter",
    icon=":material/school:"
)

example9 = st.Page(
    "./coach/example9.py",
    title="Acceleration Explorer",
    icon=":material/school:"
)

example10 = st.Page(
    "./coach/example10.py",
    title="My Soccer Dashboard",
    icon=":material/school:"
)


saboj = st.Page(
    "./roster/saiboj.py",
    title="Saboji's App",
    icon=":material/sports_and_outdoors:",
    default=(user == "Saboji")
)
lilly = st.Page(
    "./roster/lilly.py",
    title="Lilly's App",
    icon=":material/sports_and_outdoors:",
    default=(user == "Lilly")
)
account_pages = [logout_page, settings]
explore_pages = [BootRoom, prosoccer]
build_pages = [codeBox]
examples_pages = [example1, example2, example3, example4, example5, example6, example7, example8, example9, example10]
deployed_pages = [coachGus, classpage, lilly, saboj]

page_dict = {}

if (st.session_state.user in allroles):
    page_dict["Create Magic"] = build_pages
if (st.session_state.user in allroles):
    page_dict["Examples from Coach"] = examples_pages
if (st.session_state.user in allroles):
    page_dict["Data Exploration"] = explore_pages
if (st.session_state.user in allroles):
    page_dict["From the Lab"] = deployed_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

st.logo("./media/footylab_v2_horizontal.png",link="https://datarook.com/")

st.divider()
st.header("Links and Resources")
col1, col2 = st.columns(2)
with col1:
      #st.subheader("Streamlit ~~Docs~~ Spellbook")
      st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about Streamlit ~~methods~~ spells", icon="🪄")
      uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
      with open(uploaded_file) as f:
            btn = st.download_button(
                  label="Download Last 30 Days GPS Data",
                  data = f,
                  file_name="gps_data.csv",
                  mime="text/csv"
                )
with col2:
      st.page_link("https://footylab.notion.site/Boys-Girls-Club-Western-Heights-184d64111f03802eb2e5fb6e3d3c677e", label="footyLab Magicians", icon="🧙‍♀️")
      st.page_link("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/", label="Emoji Codes!", icon="😎")
      st.page_link("https://app.veo.co/clubs/datarook-academy/teams/soccer-lab/#recordings", label="Game Footage", icon="🎥")
      #st.page_link("https://forms.gle/7Zn14EdkySSFArir8", label="Day 1 Info Form", icon="📋")
      