import hashlib
import json

def crypto_hash(data):
    """
    Return  a sha-256 hash of the given data
    """
    stringified_data = json.dumps(data)

    #return hashlib.sha256(data.encode('utf-8')).hexdigest()
   
        #^data needs to be encoded before hashing
        #^adding ".encode('utf-8)" encodes the data, converting it into the UTF-8 byte string representation
        #^This result will only provide the memory address but the hash value should be a unique output based on the unique input so the encoded data must be converted once more
            #^A hex digest method can be used to convert the data into a 64-character hexadecimal string
        
    #In the instance that your data is anything but a string, Pythons "json.dump()" can simply stringify that data:
    return hashlib.sha256(stringified_data('utf-8')).hexdigest()

    def main():
        print(f"crypto_hash('foo'):{crypto_hash('foo)}")

        if __name__ == '__main__':
            main()

