import streamlit as st
import csv
import statistics
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random
from PIL import Image
import pydeck as pdk



pd.set_option('display.max_columns', 20)  # displays all columns
pd.set_option('display.max_rows', 50)  # displays all rows
pd.set_option('display.width', 500)  # prevents output from being on 2 lines


file_name = "MPSVotes.csv"
data = pd.read_csv(file_name)

#set title
st.title('WHO WILL BE MR . PHI SIG')


Contestants = []
for i in data['Contestants']:
    if i not in Contestants:
        Contestants.append(i)


UpdatedVotes = []
for j in data['Votes']:
    if j not in UpdatedVotes:
        UpdatedVotes.append(j)

#st.sidebar.header('Select which contestants you would like to compare')
#options = st.sidebar.multiselect('Who will it be?', Contestants)
#st.write('You selected:', options)

if st.button('Update'):
    st.balloons()
    for i in range(len(Contestants)):
        for j in range(len(UpdatedVotes)):
            if Contestants[i] == UpdatedVotes[j]:
                break
    plt.bar(Contestants, UpdatedVotes)
    plt.tick_params(axis='x', labelsize=5)
    plt.ylabel('Contestant Name')
    plt.title('Voting Dashboard')
    st.pyplot()
else:
    st.write()
