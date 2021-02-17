class Block:
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cyrptocurrency.
    """

    def __init__(self, data):
            self.data = data
    
    #default representation of the block 
    def __repr__(self):
            return f'Block - data: {self.data}'

class Blockchain:
    """
    Blockchain: A public ledger of transactions.
    Implemented as a list of blacks A.K.A transactional data sets
    """

    # List of blocks and consists of block items
    def __init__(self): 
        self.chain = []
    
    def add_block(self,data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')

print(blockchain)


