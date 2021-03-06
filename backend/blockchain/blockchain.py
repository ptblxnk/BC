from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: A public ledger of transactions.
    Implemented as a list of blacks A.K.A transactional data sets
    """

    # List of blocks and consists of block items
    def __init__(self): 
        self.chain = [Block.genesis()]
    
    def add_block(self, data):
        #refactored since mine block is only used once
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming one if the following applies:
          - The incoming chain is longer than the local one.
          - The incoming chain is formatted properly.
        """

        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace. The incoming chain must be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = chain

    def to_json(self):
        """
        Serialize teh blockchain into a list of blocks
        """
        # serialize_chain = []

        # for block in self.chain:
        #     serialize_chain.append(block.to_json())
        # return serialize_chain
        #^^^^^ REFACTORED THIS CODE ^^^^^
        return list(map(lambda block: block.to_json(), self.chain))


    @staticmethod
    def from_json(chain_json):
        """
        Deserialize a lost of serialzed blocks into a Blockchain instance.
        The result will contain a chain lost of Block instances.
        """
        blockchain = Blockchain()
        blockchain.chain = list(
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )

        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of teh blockchain:
           - the chain must start with the genesis block
           - blocks must be formatted correctly
        """

        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid ')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()
