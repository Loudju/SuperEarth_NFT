# Imports
import json
import os
from pathlib import Path
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

from wallet import generate_account, get_balance, buy_land

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load ABI
    with open(Path('contracts\compiled\land_abi.json')) as f:
        land_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=land_abi
    )
    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()

# Database of lands available for sale
land_database = {
    "Land 1": ["Land 1", .25, "0xaBa6f43b2Bae43Ff7C697aB5A03847796d4A6afB"],
    "Land 2": ["Land 2", .15, "0x45F7B55bB08f8665Dc8E294D412dCC238fb7F00E"],
    "Land 3": ["Land 3", .43, "0xD1EC080bE92EC2175ea60E64FD835f44ef7Ba3d8"],
    "Land 4": ["Land 4", .17, "0xa7808b6a7d45fc8f46F149Ec4B98fEc697eF0e61"],
    "Land 5": ["Land 5", .20, "0x91d409a2910e352970965C0c64AE4dc6886E0bb6"]
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



accounts = w3.eth.accounts
account = accounts[0]

st.sidebar.markdown("## Purchase land on Super Earth with Ether!")

st.sidebar.write(account)



land = st.sidebar.selectbox('Select a Land', lands)

price = land_database[land][1]

st.sidebar.write("Price of land in ETH:", price)

buyer_account = land_database[land][2]
new_land = land
if st.sidebar.button("Buy Land"):
    contract.functions.purchaseLand(buyer_account, new_land).transact({'from': buyer_account, 'gas': 1000000})
    st.balloons()
    st.text(" \n")
    st.text(" \n")
    st.write("Congratulations! You now own land on Super Earth!")