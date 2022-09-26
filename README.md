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
## Top Offerings on the Super-Earth

 - Land 1-Diamond Land “Girls best friend”
 
![Land1](https://user-images.githubusercontent.com/103230949/192176522-62017aab-c0bb-4b9b-b278-e855af807046.jpg)

Diamond Land is an exquisite piece of land ownership that provides the best of the best in precious diamonds. Not only does this land hold diamonds but rubies of the most unique kind have been found to live deep within super earth. To rap your mind around just how much, lets just say, Diamond Land holds nearly 10 times the amount that have been found in Africa with more to spare. Our expectation is that the Top Jewelers from around the world will flood the market extremely quickly. Buy Now before its too late.


 - Land2- Oil & Gas Land
 
![Land2](https://user-images.githubusercontent.com/103230949/192176527-82ad9908-83c9-4dde-a954-2b13dc3d80cd.jpg)

While Gas prices are soaring and people around this planet are going crazy, Super Earth has an abundance of Oil and Gas landfills that would make  the Saudi Arabian Supply look miniscule. This will not last long. As this is by far one of the most sought after types of Land on this planet and beyond. Super Earth will literaly fuel this planet. Be apart of saving planet earth today. Buy now.


 - Land3- Waterloo “Infinite water spring rights”
 
![Land3](https://user-images.githubusercontent.com/103230949/192176538-841c6b00-b8bb-4702-a9b5-00e8cf48f018.jpg)

As you may know, water is at a drought on planet earth and resources are becoming more limited by the day. Buy land on Super Earth now, where your investment will last many light years beyond planet earth. With fresh spring water rights the possibilities are near infitie on how you could benefit humanity or commercialize your rights as you see fit.


 - Land-4 Gold Heaven
 
![Land4](https://user-images.githubusercontent.com/103230949/192176544-3d83ecc0-1524-470c-a103-d1cc1f3013cd.jpg)

Own the rights to your own gold heaven with these special out of this world land rights. As you may know gold is not just a commodity but very important when building the very technology that we use daily from phones to laptops. Gold has backed the dollar at one point and now the availability is beyond what the government can control. Own your own gold heaven today and the possibility to fund the money supply of the future. The possibilities are endless with this purchase as Gold is thee super conductor for Life.

 - Land5- Ti22 “Titanium Overload”
 
![Land5](https://user-images.githubusercontent.com/103230949/192176553-4c0a4040-2f99-41d9-8455-58e89331c1ac.jpg)

Titanium is one of the strongest metals known to man and has been the bedrock of our defense departments weapon supply and the ability to build innovative technologies with many use cases. Do not hesitate to buy, as this land is sought after by all of the top governmental powers on earth such as The United States, China, Russia, Saudi, and more. With your purchase you could control innovation for centuries to come.

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
