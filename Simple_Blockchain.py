import hashlib
import datetime

class Block:
    def __init__(self, index, year,month,day, data, previousHash=''):
        self.index=index
        self.data=data
        self.date=datetime.date(year,month,day)
        self.previousHash=previousHash
        self.hash=self.CalcHash()

    def CalcHash(self):
        return hashlib.sha256((str(self.index)+self.data+self.previousHash).encode('utf-8')).hexdigest()

    def __repr__(self):
        return 'Index: {}, Date: {}, Data: {}, Previous Hash: {}, Self Hash: {}'.format(self.index, self.date,self.data, self.previousHash,self.hash)
class Blockchain:
    def __init__(self):
        self.chain=[self.GenesisBlock()]

    def __str__(self):
        return ', '.join(self.chain)
    def __repr__(self):
        return str(self.chain)
    def GenesisBlock(self):
        return Block(0,2018,1,22,"Genesis Block","0")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def addBlock(self,new):
        new.previousHash=self.getLatestBlock().hash
        new.hash = new.CalcHash()
        self.chain.append(new)
