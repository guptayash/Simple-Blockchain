import hashlib
import datetime
class Transaction:
    def __init__(self, toAddress, fromAddress, amount):
        self.toAddress=toAddress
        self.fromAddress=fromAddress
        self.amount=amount
    def __repr__(self):
        return "toAddress: {}, fromAddress {}, amount: {}".format(self.toAddress,self.fromAddress,self.amount)
        
class Block:

    def __init__(self,year,month,day, transactions, previousHash=''):
        self.transactions=transactions
        self.date=datetime.date(year,month,day)
        self.previousHash=previousHash
        self.nonce=0
        self.hash=self.CalcHash()


    def CalcHash(self):
        return hashlib.sha256((str(self.transactions)+self.previousHash+str(self.nonce)).encode('utf-8')).hexdigest()

    def mineBlock(self,difficulty):
        print("Difficulty is",difficulty)
        #print(self.hash[0:difficulty])
        print("Mining Block ...")
        while (self.hash[0:difficulty]!='0'*difficulty):
            self.hash=self.CalcHash()
            self.nonce+=1
            #print(self.nonce)
        print("Block Mined", self.hash)


    
    def __repr__(self):
        return 'Date: {}, Data: {}, Previous Hash: {}, Self Hash: {}'.format(self.date,self.transactions, self.previousHash,self.hash)
class Blockchain:
    def __init__(self):
        self.chain=[self.GenesisBlock()]
        self.difficulty=4
        self.pendingTransactions=[]
        self.miningRewards= 1

    def __str__(self):
        return ', '.join(self.chain)
    def __repr__(self):
        return str(self.chain)
    def GenesisBlock(self):
        return Block(2018,1,22,"Genesis Block - First Block","0")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

##    def addBlock(self,new):
##        new.previousHash=self.getLatestBlock().hash
##        new.mineBlock(self.difficulty)
##        self.chain.append(new)
    def minePendingTransactions(self,miningRewardAddress):
        A=Block(2018,1,22, self.pendingTransactions)
        A.mineBlock(self.difficulty)
        print("Block successfully mined")
        self.chain.append(A)
        self.pendingTransactions=[Transaction(None,miningRewardAddress,self.miningRewards)]

    def createTransaction(self,transaction):
        self.pendingTransactions.append(transaction)
    def ValidChain(self):
        for i in range(1,len(self.chain)):
            if self.chain[i].hash!= self.chain[i].CalcHash() or self.chain[i].previousHash!=self.chain[i-1].hash:
                return False
            else:
                return True

    
