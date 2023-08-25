import unittest
from tasks.task1 import Queue
from tasks.task2 import MegaQueue,QueueAlreadyExist,QueueAlreadyExist,QueueOutOfRangeException

class TestQueue(unittest.TestCase):
    def setUp(self):
        
        self.ls=["test1",["test2","test2"],"test3",("test4","test4","test4")]
        
        self.queue=Queue()
        
    def runTest(self):
        self.setUp()
        
        self.assertEqual(self.queue.isempty(),True,"Incorrect isempty")
        
        for item in self.ls:
            self.queue.append(item)
        
        self.assertEqual(self.queue.isempty(),False,"Incorrect isempty")
        
        for item in self.ls:
            self.assertEqual(self.queue.pop(),item,"Incorrect pop out")
        
        self.assertEqual(self.queue.isempty(),True,"Incorrect isempty")
        self.assertEqual(self.queue.pop(),None,"Incorrect pop out")

class TestMegaQueue(unittest.TestCase):
    def setUp(self):
        self.ls=["test1",["test2","test2"],"test3",("test4","test4","test4")]
        
    def testQueue(self):
        """
        Tests the normal behavious of a fourlength
        """
        fourlength= MegaQueue("test4",4)
        self.assertEqual(fourlength.isempty(),True,"Incorrect isempty")
        
        for item in self.ls:
            fourlength.append(item)
        
        self.assertEqual(fourlength.isempty(),False,"Incorrect isempty")
        
        for item in self.ls:
            self.assertEqual(fourlength.pop(),item,"Incorrect pop out")
        
        self.assertEqual(fourlength.isempty(),True,"Incorrect isempty")
        self.assertEqual(fourlength.pop(),None,"Incorrect pop out")
        
    def testQueueUsingGetQueue(self):
        MegaQueue("test5",4)
        queue=MegaQueue.GetQueueObject("test5")
        self.assertEqual(queue.isempty(),True,"Incorrect isempty")
        
        for item in self.ls:
            queue.append(item)
        
        self.assertEqual(queue.isempty(),False,"Incorrect isempty")
        
        for item in self.ls:
            self.assertEqual(queue.pop(),item,"Incorrect pop out")
        
        self.assertEqual(queue.isempty(),True,"Incorrect isempty")
        self.assertEqual(queue.pop(),None,"Incorrect pop out")
        
    def testQueueOutOfRange(self):
        onelength = MegaQueue("test1",1)
        zerolength = MegaQueue("test0",0)
        threelength = MegaQueue("test3",0)
        with self.assertRaises(QueueOutOfRangeException):
            for item in self.ls:
                onelength.append(item)
                
        with self.assertRaises(QueueOutOfRangeException):
            for item in self.ls:
                zerolength.append(item)
                
        with self.assertRaises(QueueOutOfRangeException):
            for item in self.ls:
                threelength.append(item)
         
    def testQueueAlreadyExist(self):
        test1 = MegaQueue("test6",1)
        test2 = MegaQueue("test7",0)
        test3 = MegaQueue("test8",0)
        test3 = MegaQueue("test9",0)
        with self.assertRaises(QueueAlreadyExist):
            duplicate1=MegaQueue("test6",1)
            
        with self.assertRaises(QueueAlreadyExist):
            duplicate2=MegaQueue("test7",6)
            
        with self.assertRaises(QueueAlreadyExist):
            duplicate3=MegaQueue("test8",5)
            
        with self.assertRaises(QueueAlreadyExist):
            duplicate4=MegaQueue("test9",0)
    
    def testGetQueue(self):
        firstcase = MegaQueue("test10",1)
        secondcase = MegaQueue("test11",0)
        thirdcase = MegaQueue("test12",0)
        
        self.assertEqual(firstcase.GetQueueObject("test10"),firstcase,"Test10 isn't equal firstcase")
        self.assertNotEqual(firstcase.GetQueueObject("test10"),secondcase,"Test10 isn't equal firstcase")
        self.assertNotEqual(firstcase.GetQueueObject("test10"),thirdcase,"Test10 isn't equal firstcase")

    def testmaxTypeError(self):
        with self.assertRaises(TypeError):
            MegaQueue("test15","1")
        with self.assertRaises(TypeError):
            MegaQueue("test16",[1 , 2])
        with self.assertRaises(TypeError):
            MegaQueue("test17",1.5)

if __name__ is "__main__":
    unittest.main()