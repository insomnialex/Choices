import random
from pymongo import Connection


class Food(object):

    def __init__(self):
        self.db = Connection()["food"]["choices"]

    def add(self, name):
        name = str(name).lower()
        self.db.update({'name':name}, {'name':name}, upsert=True)

    def remove(self, name):
        self.db.remove({'name':name})

    def get_all(self):
        retVal = []
        try:
            cur = self.db.find()
            for i in cur:
                retVal.append(i['name'])
        except:
            pass
        return retVal
        

    def choose(self):
        try:
            cur = self.db.find()
            tmp = []
            for i in cur:
                tmp.append(i['name'])
            index = random.randrange(len(tmp))
            return tmp[index]
        except:
            return "unknown"
        

