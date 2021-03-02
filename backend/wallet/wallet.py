import json
import uuid

from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of a miners balance.
    Allows a minor to authorize transactions.
    """
    def __init__(self):
        #UUID -  Universial unique identifier
        # in terminal call:
        # 1. python3
        # 2. uuid.uuid4()
        # This will generate a new UUID everytime the function is called
            self.address = str(uuid.uuid4())[0:8]
            self.balance = STARTING_BALANCE
            self.private_key = ec.generate_private_key(
                ec.SECP256K1(),
                default_backend()
                )
            # SEC= standards of efficient cryptography, P=prime, 256 = 256 bits, K=Koblitz 1= First implementation of the algorithm
            self.public_key = self.private_key.public_key()
            #^^To accesss the private key based on the public key object



    def sign(self, data):
        """
        Generate a signature based on teh data using the local private key.
        """

        return self.private_key.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256()))
        #ECDSA = elliptic cryptography digital signature algorithm
        #Uses elliptic curves to create keypairs and signatures.

    @staticmethod
    def verify(public_key, data, signature):
        """
        Verify a signature based on the original public key & data.
        """
        try:
            public_key.verify(
                signature,
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())
                )
            return True
        except InvalidSignature:
            return False


def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')

    data = { 'foo': 'bar'}
    signature = wallet.sign(data)
    print(f'signature: {signature}')

    should_be_valid = Wallet.verify(wallet.public_key, data, signature)
    print(f'should be valid: {should_be_valid}')

    should_be_invalid = Wallet.verify(Wallet().public_key, data, signature)
    print(f'should be invalid: {should_be_invalid}')



if __name__ == '__main__':
    main()