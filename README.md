# project3_fintech

Develop a project that utilizes blockchain technology. 

Initial Ideas:
 1. For clients to purchase land on the new super earth planet discovered recently via Ethereum token.
 
 2. To be able to register and update the star land registry dApp, pin an star land File to IPFS via Pinata.
 
 3. All property NFT contracts are encrypted and tokenized on Solidity Remix IDE.

![NASA-Has-Discovered-300-Million-Inhabitable-Planets](https://user-images.githubusercontent.com/103230949/192163101-17ee432e-f5cd-4478-abd8-cc1a43af43f1.jpg)

![LP 890-9c](https://user-images.githubusercontent.com/103230949/192163074-cb68c627-55d6-4f25-8b51-7ad3c822c8ce.png)

![Screenshot 2022-09-20 190151](https://user-images.githubusercontent.com/103230949/192163098-95eecc1f-ced6-4eb6-ad09-36cf8693c0e2.png)

The class presentation is located here: [New Earth Found - LP 890-9c.pdf](https://github.com/Loudju/project3_fintech/files/9641826/New.Earth.Found.-.LP.890-9c.pdf)

---
## Top Offerings

---

## Technologies

This project uses Solidity, Remix IDE, Git Bash, Visual Studio, and Github.

---

## Installation Guide

The web version of Remix IDE was used and this is the Solidity version that was used:

    pragma solidity ^0.5.0


Imports and libraries:

    import streamlit as st

    from dataclasses import dataclass

    from typing import Any, List

    from web3 import Web3

    w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

    from wallet import generate_account, get_balance, send_transaction

    import os

    import requests

    from dotenv import load_dotenv

    load_dotenv()

    from bip44 import Wallet

    from web3 import Account

    from web3 import middleware

    from web3.gas_strategies.time_based import medium_gas_price_strategy

---

## Usage

* Step 1: 


* Step 2: 


* Step 3: 



---

## Streamlit Snippets

![screenshot1](streamlit_screenshots/screenshot1.png)
![screenshot2](streamlit_screenshots/screenshot2.png)
![screenshot3](streamlit_screenshots/screenshot3.png)
![screenshot4](streamlit_screenshots/screenshot4.png)

## Star Land Registry & Appraisal System with IPFS

## Instructions
  1. Deploy the Contract
![Metamask Transaction](https://user-images.githubusercontent.com/103230949/192166192-cbbf0137-8532-4831-8ece-7c7ba3647150.png)

  2. Prepare the environment
  
 ![Metamask Transaction Confirmed](https://user-images.githubusercontent.com/103230949/192166203-bc46f139-da53-4571-ba24-2bed5370a097.png)
 
  3. Build the dApp
  
### Reister New Star Land:

![Register Star Land](https://user-images.githubusercontent.com/103230949/192166212-59d08168-93c7-4dc9-a3ad-619230171135.png)

### Appraise Star Land and Get Transaction History:

![Appraise Star Land and Get Hisotry](https://user-images.githubusercontent.com/103230949/192166215-bb54d892-b66f-4fff-8d5d-022e5b1cd8e5.png)

---

## Contributors

Allyssa Carmin

Vicky Lee

Julian Louden

Noman Zubairi

---

## License

SMU Fintech Course, Project 3
