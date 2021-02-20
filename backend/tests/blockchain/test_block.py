from backend.blockchain.block import Block, GENESIS_DATA

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)


    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash


#Test how blocks are created with the genesise method too
def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    # assert genesis.timestamp == GENESIS_DATA['timestamp']
    # assert genesis.last_hash == GENESIS_DATA['last_hash']
    # assert genesis.hash == GENESIS_DATA['hash']
    # assert genesis.data == GENESIS_DATA['data']
    # ^Code above can be refactored in a for loop to access the data automatically and guarantees all instances in the genesis block matches the data in the genesis dictionary 
   
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) ==value

    