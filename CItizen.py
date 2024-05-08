import streamlit as st
from web3 import Web3
import json
import datetime

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Load contract ABI and address
contract_address = '0xe463E796d379DB21043cC94Cc42F25Ffdf97DFdE'
abi_file_path = r'D:\MIT-WPU\6th sem\Seminar\Streamlit Citizen\build\contracts\IdentityManagement.json'
with open(abi_file_path, 'r') as file:
    contract_data = json.load(file)
    contract_abi = contract_data['abi']

# Instantiate contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Streamlit app
st.title('Citizen Identity Management')

# Function to create or update identity for a specific Ethereum address
def create_or_update_identity(eth_address, first_name, last_name, dob, national_id):
    dob_timestamp = int(datetime.datetime.combine(dob, datetime.time.min).timestamp())
    tx_hash = contract.functions.createOrUpdateIdentity(first_name, last_name, dob_timestamp, national_id).transact({'from': eth_address})
    st.write('Transaction Hash:', tx_hash.hex())

# Function to verify identity for a specific Ethereum address
def verify_identity(eth_address):
    verified = contract.functions.verifyIdentity(eth_address).call()
    if verified:
        st.success('Identity Verified')
    else:
        st.error('Identity Not Verified')

# Get user input for Ethereum address
eth_address = st.text_input('Enter Ethereum Address')

if eth_address:
    # Options for the user
    option = st.radio("What do you want to do?", ("Create/Update Identity", "Verify Identity"))

    if option == "Create/Update Identity":
        # Get user input for identity information
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        dob = st.date_input('Date of Birth')
        national_id = st.text_input('National ID')

        # Button to create or update identity
        if st.button('Create/Update Identity'):
            if first_name and last_name and dob and national_id:
                create_or_update_identity(eth_address, first_name, last_name, dob, national_id)
            else:
                st.warning('Please fill in all fields')

    elif option == "Verify Identity":
        # Button to verify identity
        if st.button('Verify Identity'):
            verify_identity(eth_address)
