class Queue():
    def __init__(self):
        self.__list=[]
    def append(self,item):
        self.__list.append(item)
    def pop(self):
        try : 
            return self.__list.pop(0)
        except IndexError:
            print("the queue is currently empty ")
            return None
    
    def isempty(self):
        return not len(self)
    
    def __len__(self):
        return len(self.__list)