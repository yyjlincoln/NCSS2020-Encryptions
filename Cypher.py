


class Cypher:
    def __init__(self):
        pass

    # def _pre_process_key(self, key, master):
    #     key = list(key)
    #     for x in range(len(key)): # Pre-process the key. Get each character of the key's Unicode value (1), and each character of the masterkey's Unicode value (2).
    #         # Loop through, if the index%2 == 0, it will perform (1) - (2), otherwise plus
    #         if x % 2:
    #             key[x] = chr(
    #                 abs(ord(key[x]) + ord(master[x % len(master)])) % 65536) 
    #         else:
    #             key[x] = chr(
    #                 abs(ord(key[x]) - ord(master[x % len(master)])) % 65536)
    #         # considering that it might exceed the range of unicode, do a %.
    #         # considering that it might <0, get abs()
    #     k = ''
    #     for x in key:
    #         k += x
    #     return k

    def _encrypt(self, string, key):
        string = list(string)
        l = ''
        for x in range(len(string)): # Get each character of the key's Unicode value (1), and each character of the key's Unicode value (2).
            string[x] = str(ord(string[x]) + ord(key[x % len(key)])) # Plus the unicode value, conver the string, and record the length of the string.
            l += str(len(string[x]))

        k = ''
        for x in string:
            k += str(x)
        k = k+'::'+ l
        # Convert to string, add the length after double :
        return k
    
    def _decrypt(self, string, key, delta):
        # Same stuff, reverse encrypt.
        d = list(delta)
        split = []
        i = 0
        for x in d:
            split.append(string[i:(int(x)+i)])
            i+=int(x)

        s = []
        # print(split)
        for x in range(len(split)):
            # print( int(split[x]), ord(key[x % len(key)]) ,int(split[x]) - ord(key[x % len(key)]))
            s.append(chr(  int(split[x]) - ord(key[x % len(key)])  )) 
            # print(string[x]))

        k = ''
        for x in s:
            k += str(x)

        return k

    def encrypt(self, string, key):
        # k = self._encrypt(string, self._pre_process_key(key, master))
        k = self._encrypt(string, key)
        return k

    def decrypt(self, string, key):
        string = string.split('::')
        # key = self._pre_process_key(key,master)
        return self._decrypt(string[0], key, string[1])




def encrypt(string, key = 'yyj:li'):

    a = Cypher()
    # key = key.split(':')
    # k, master = key
    return a.encrypt(string, key)

def decrypt(string, key = 'yyj:li'):
    a = Cypher()
    # key = key.split(':')
    # k, master = key
    return a.decrypt(string, key)

# print(encrypt('1234','123:34'))
# print(decrypt('511525154::2322','123:34'))

# ord()
# chr()
