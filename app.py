# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

from wallet import generate_account, get_balance, send_transaction

# Database of lands available for sale
land_database = {
    "Land 1": ["Land 1", .25],
    "Land 2": ["Land 2", .15],
    "Land 3": ["Land 3", .43],
    "Land 4": ["Land 4", .17],
    "Land 5": ["Land 5", .20]
}

lands = ["Land 1", "Land 2", "Land 3", "Land 4", "Land 5"]

def get_land():
    db_list = list(land_database.values())

    for number in range(len(lands)):
        st.write("Name of land: ", db_list[number][0])
        st.write("Price of land: ", db_list[number][1])
        st.text(" \n")

# Streamlit code
st.markdown("# Buy land on Super Earth!")
st.text(" \n")

get_land()

account = generate_account()

st.sidebar.markdown("## Purchase land on Super Earth with Ether!")

st.sidebar.write(account.address)

st.sidebar.write(get_balance(w3, account.address))