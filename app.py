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
    "Diamond Land - Girls best friend": ["Diamond Land - Girls best friend", 2.25, "0xaBa6f43b2Bae43Ff7C697aB5A03847796d4A6afB", "images\Land1.jpg", "Diamond Land is an exquisite piece of land ownership that provides the best of the best in precious diamonds. Not only does this land hold diamonds but rubies of the most unique kind have been found to live deep within super earth. To rap your mind around just how much, lets just say, Diamond Land holds nearly 10 times the amount that have been found in Africa with more to spare. Our expectation is that the Top Jewelers from around the world will flood the market extremely quickly. Buy Now before its too late."],
    "Oil & Gas Land": ["Oil & Gas Land", 1.15, "0x45F7B55bB08f8665Dc8E294D412dCC238fb7F00E", "images\Land2.jpg", "While Gas prices are soaring and people around this planet are going crazy, Super Earth has an abundance of Oil and Gas landfills that would make  the Saudi Arabian Supply look miniscule. This will not last long. As this is by far one of the most sought after types of Land on this planet and beyond. Super Earth will literaly fuel this planet. Be apart of saving planet earth today. Buy now!"],
    "Waterloo Infinite water spring rights": ["Waterloo Infinite water spring rights", 3.43, "0xD1EC080bE92EC2175ea60E64FD835f44ef7Ba3d8", "images\Land3.jpg", "As you may know, water is at a drought on planet earth and resources are becoming more limited by the day. Buy land on Super Earth now, where your investment will last many light years beyond planet earth. With fresh spring water rights the possibilities are near infitie on how you could benefit humanity or commercialize your rights as you see fit."],
    "Gold Heaven": ["Gold Heaven", 2.17, "0xa7808b6a7d45fc8f46F149Ec4B98fEc697eF0e61", "images\Land4.jpg", "Own the rights to your own gold heaven with these special out of this world land rights. As you may know gold is not just a commodity but very important when building the very technology that we use daily from phones to laptops. Gold has backed the dollar at one point and now the availability is beyond what the government can control. Own your own gold heaven today and the possibility to fund the money supply of the future. The possibilities are endless with this purchase as Gold is thee super conductor for Life."],
    "Ti22 - Titanium Overload": ["Ti22 - Titanium Overload", 3.20, "0x91d409a2910e352970965C0c64AE4dc6886E0bb6", "images\Land5.jpg", "Titanium is one of the strongest metals known to man and has been the bedrock of our defense departments weapon supply and the ability to build innovative technologies with many use cases. Do not hesitate to buy, as this land is sought after by all of the top governmental powers on earth such as The United States, China, Russia, Saudi, and more. With your purchase you could control innovation for centuries to come."]
}

lands = ["Diamond Land - Girls best friend", "Oil & Gas Land", "Waterloo Infinite water spring rights", "Gold Heaven", "Ti22 - Titanium Overload"]

def get_land():
    db_list = list(land_database.values())

    for number in range(len(lands)):
        st.image(db_list[number][3], width=400)
        st.text(" \n")
        st.write("Name of land: ", db_list[number][0])
        st.write("Description: ", db_list[number][4])
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
    contract.functions.purchaseLand(buyer_account, new_land).transact({'from': buyer_account, 'to': account, 'amount': price})
    st.balloons()
    st.text(" \n")
    st.text(" \n")
    st.sidebar.write("Congratulations! You now own land on Super Earth!")