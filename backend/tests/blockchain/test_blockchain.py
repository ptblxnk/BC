from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def tst_blockchain_instance():
    blockchain = Blockchain()

    #Accessing the 1st item in the chain which should be the genesis block
    assert blockcahin.chain[0].hash == GENESIS_DATA['hash']

def  test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    #Accessing the final item in the chain and making sure that data matches the same data within the data variable in the add_block method 
    assert blockchain.chain[-1].data == data