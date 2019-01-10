import src.prime as prime
import src.Rabin as Rabin
import pickle as pkl
import os

class crypto_system:
    def __init__(self, name):
        self.user_name = name
        self.private_key_file = 'bin/private_{n}.pkl'.format(n=name)
        self.public_key_file = 'bin/public_{n}.pkl'.format (n=name)

    def is_keys_file_exists(self, keys_file):
        if not os.path.exists (keys_file):
            print ('There is no keys`s file <{kf}>'.format(kf=keys_file))
            return False
        else:
            return True

    def key_gen(self):

        keySize = int(input('Key size (128 recommended): '))

        p = prime.generate_prime_number(keySize)
        print('p: ', p)
        q = prime.generate_prime_number(keySize)
        print('q: ', q)
        n = p*q
        print('n: ', n)
        pkl.dump((p,q), open(self.private_key_file, 'wb'))
        pkl.dump(n, open(self.public_key_file, 'wb'))


    def load_public_key(self, public_key_file):

        if not self.is_keys_file_exists(public_key_file):
            exit()

        n =  pkl.load(open(public_key_file, 'rb'))

        print ("Public key loaded! Using:")

        print('n: ', n)

        return n

    def load_private_key(self, private_key_file):

        if not self.is_keys_file_exists(private_key_file):
            exit()

        p, q =  pkl.load(open(private_key_file, 'rb'))

        print ("Private keys loaded! Using:")

        print('p: ', p)
        print ('q: ', q)

        return p, q


    def encryption(self):

        key_holder = input('\nInput key holder`s name:')
        enc_file_name = input ('\nInput file name with cypher text: ')

        public_key_file_name = 'bin/public_{kh}.pkl'.format(kh=key_holder)
        n = self.load_public_key(public_key_file_name)
        _str = input('\nYour string: ')

        with open('bin/{efn}.txt'.format(efn=enc_file_name), 'w') as f:

            for plaintext in _str:
                ciphertext = Rabin.encryption(ord(plaintext), n)
                f.write(str(ciphertext) + ' ')

        print('\nCheck encrypt data in bin/{efn}.txt'.format(efn=enc_file_name))

    def decryption(self):
        cypher_text = input('Enter cypher text file name:')

        if not self.is_keys_file_exists('bin/{ct}.txt'.format(ct=cypher_text)):
            exit()

        p,q = self.load_private_key(self.private_key_file)

        result = ''

        with open('bin/{ct}.txt'.format(ct=cypher_text), 'r') as f:
            data = [int(k) for k in f.read().split(' ') if len(k) > 0]

        try:
            for ciphertext in data:
                plaintext = Rabin.decryption(ciphertext, p, q)
                result += chr(plaintext)

            print ('\nDecrypted text: ', result)
        except Exception as e:
            print('Error while decryption cypher text:', e)

if __name__ == '__main__':
    user_name = input('Enter user name:')
    rb = crypto_system(user_name)
    print('\nChoose the action:\n[--kg] Keys generating\n[--enc] Encryption\n[--dec] Decryption')
    action = input('Enter action key: ')
    if action == '--kg':
        print('\n<Rabin Key generation>')
        rb.key_gen()
        print('<Rabin Key generation is successful done>')
    elif action == '--enc':
        print('\n<Rabin Encryption>')
        rb.encryption()
        print ('<Rabin Encryption is successful done>')
    elif action == '--dec':
        print('\n<Rabin Decryption>')
        rb.decryption()
        print ('<Rabin Decryption is successful done>')
    else:
        print ('\nThe parameter [{ac}] is not available'.format (ac=action))
    
   
