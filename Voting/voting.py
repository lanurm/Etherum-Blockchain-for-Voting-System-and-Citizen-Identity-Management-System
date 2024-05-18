import streamlit as st
from web3 import Web3
import json

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Load contract ABI and address
contract_address = '0xd2cc53dB1C9e54f4Bd1210d46463bd994ef51EC8'
abi_file_path = r'D:\MIT-WPU\6th sem\Seminar\Streamlit\build\contracts\Voting.json'
with open(abi_file_path, 'r') as file:
    contract_data = json.load(file)
    contract_abi = contract_data['abi']

# Instantiate contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Streamlit app
st.title('E-Voting System')

# Function to vote for a candidate
def vote(candidate_id, user_address):
    # Specify the account to use for transactions
    web3.eth.default_account = user_address
    
    tx_hash = contract.functions.vote(candidate_id).transact()
    st.write('Transaction Hash:', tx_hash.hex())

# Function to get total votes for a candidate
def get_total_votes(candidate_id):
    total_votes = contract.functions.getTotalVotes(candidate_id).call()
    st.write('Total Votes for Candidate', candidate_id, ':', total_votes)

# Get user input for candidate ID and Ethereum address
candidate_id = st.text_input('Enter Candidate ID')
user_address = st.text_input('Enter Your Ethereum Address')

# Button to cast a vote
if st.button('Vote'):
    if candidate_id and user_address:
        vote(int(candidate_id), user_address)
    else:
        st.warning('Please enter Candidate ID and Ethereum Address')

# Button to get total votes for a candidate
if st.button('Get Total Votes'):
    if candidate_id:
        get_total_votes(int(candidate_id))
    else:
        st.warning('Please enter Candidate ID')
