# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# From `crypto_wallet.py import the functions generate_account, get_balance, and send_transaction

from crypto_wallet import generate_account, get_balance, send_transaction

# Database of EthWork candidates including their name, digital address, rating and hourly cost per Ether.
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the EthWork candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of EthWork candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("EthWork Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Codels

# Streamlit application headings
st.markdown("# EthWork!")
st.markdown("## Hire An EthWork Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()
account_address= account.address
##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account_address)

##########################################
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
balance = get_balance(w3,account_address)
st.sidebar.write(balance)
##########################################

# Create a select box to chose a EthWork candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the EthWork candidate
candidate = candidate_database[person][0]

# Write the EthWork candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the EthWork candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the EthWork candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the EthWork candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the EthWork candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the EthWork candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = candidate_database[person][3] * hours


# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)


# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.
if st.sidebar.button("Send Transaction"):
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes EthWork candidates to the Streamlit page
get_people(w3)

################################################################################