from tasks.task1 import Queue

class MegaQueue(Queue):
    __instancesdict={}
    def __init__(self,name,max):
        if name in MegaQueue.__instancesdict.keys():
            raise QueueAlreadyExist
        else:
            if  isinstance(max, int):
                self.__max = max
                MegaQueue.__instancesdict[name]=self
                super().__init__()
                self.__name=name
            else:
                raise TypeError
            
    def append(self,item):
        if len(self) >= self.__max:
            raise  QueueOutOfRangeException
        else:
            super().append(item)
            
    @classmethod
    def GetQueueObject(self,name):
        """
        I used classmethod decorator to use this method without calling class constructor
        """
        if name in MegaQueue.__instancesdict.keys():
            return MegaQueue.__instancesdict[name]
        else:
            return None
        
    def __len__(self):
        return super().__len__()
        
class QueueOutOfRangeException(Exception):
    pass

class QueueAlreadyExist(Exception):
    pass