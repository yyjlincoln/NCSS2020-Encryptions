


class Cypher:
    def __init__(self):
        pass

    def encrypt(self, string):
        string = list(string)
        l = ''
        for x in range(len(string)):
            string[x] = str(ord(string[x]) + 1)
            l += str(len(string[x]))

        k = ''
        for x in string:
            k += str(x)
        k = k+'::'+ l
        # print('EOE')
        return k
    
    def decrypt(self, string, delta):
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
            s.append(chr(  int(split[x]) - 1  )) 
            # print(string[x]))

        k = ''
        for x in s:
            k += str(x)

        return k

    def _encrypt(self, string):
        k = self.encrypt(string)
        return k

    def _decrypt(self, string):
        string = string.split('::')
        return self.decrypt(string[0], string[1])

a = Cypher()
print(a._encrypt('123'))
print(a._decrypt('505152::222'))


# print(encrypt('1234','123:34'))
# print(decrypt('511525154::2322','123:34'))

# ord()
# chr()
