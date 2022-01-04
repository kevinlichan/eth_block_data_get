# Import the required modules
from web3 import Web3
import pandas as pd
import numpy as np

# Establish connection to blockchain via Infura
infura_url = <INSERT INFURA URL>
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

# Set up a dataframe to tabulate the data
df = pd.DataFrame(columns=['block','timestamp','gasLimit', 'gasUsed', 'difficulty', 'transaction_count'])

# Specify the range of blocks to retrieve
end = web3.eth.getBlockNumber() ## Latest block number
interval = 40000 ## Specify the number of blocks to get data from
start = end - interval
print(start)

# Retrieve block data
for i in range(interval):
    block = web3.eth.get_block(end - i)
    block_number = block.number
    block_timestamp = block.timestamp
    block_gaslimit = block.gasLimit
    block_gasused = block.gasUsed
    block_difficulty = block.totalDifficulty
    block_txncount = web3.eth.get_block_transaction_count(block_number)
    df2 = pd.DataFrame([(block_number, block_timestamp, block_gaslimit, block_gasused, block_difficulty, block_txncount)], columns=['block','timestamp','gasLimit', 'gasUsed', 'difficulty', 'transaction_count'])
    df = df.append(df2)
print("complete")
df.to_csv('block_data.csv')
