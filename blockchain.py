from block import Block, genesis, mine_block

class Blockchain:
    """
    Blockchain: A public ledger of transactions.
    Implemented as a list of blacks A.K.A transactional data sets
    """

    # List of blocks and consists of block items
    def __init__(self): 
        self.chain = [genesis()]
    
    def add_block(self, data):
        last_block = self.chain[-1]
        #index of -1 pulls the last block of the chain

        self.chain.append(mine_block(last_block, data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()
