
class HashTable:
    def __init__(self, table_size: int = 100):
        self.data=[[None] for i in range(table_size)]
        self.table_size = table_size
cc
    def get_hash(self, value: Any):

        return hash(value) % self.table_size

    def search(self,value:Any):
        i=self.get_hash(value)
        for j,v in enumerate(self.data[i]):
            if self.data[i][j]==value:
                return i,v
        return i,-1