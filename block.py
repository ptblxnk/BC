import time 
from crypto_hash import crypto_hash

class Block:
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cyrptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data):
            self.timestamp = timestamp
            self.last_hash = last_hash
            self.hash = hash
            self.data = data
    
    #default representation of the block 
    def __repr__(self):
            return (
                'Block('
                f'timestamp: {self.timestamp}, '
                f'last_hash: {self.last_hash}, '
                f'hash: {self.hash}, '
                f'data: {self.data})'
            )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given "last_block" and "data".
        """
        #Created a timestamp variable that can call the time_ns method that returns the number of nanoseconds since 1/1/1970
        timestamp = time.time_ns()
        #Gets the last hash by accessing the hash of teh previous block
        last_hash = last_block.hash
        #Constructing the hash based off of all the other values of the block 
        hash = crypto_hash(timestamp, last_hash, data)
        #^This will produce a hash value made of both the timestamp and the last hash, which for the 1st block will refernce the genesis block

        return Block(timestamp, last_hash, hash, data)
    @staticmethod
    def genesis():
        """
        Generate the denesis block.
        """
        return Block(1, 'genesis_last_hash', 'genesis_hash', [])
  
def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()