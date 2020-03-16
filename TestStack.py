from Stack import Stack
from Stack import StackException
import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.instance =Stack()

    def testClear(self):
        self.instance.clear()
        self.assertEqual(0,self.instance.size)
        self.assertEqual([],self.instance.Stack)
    
    def testContain(self):
        self.assertFalse(self.instance.contains('string'))
        self.assertFalse(self.instance.contains(''))
        self.assertFalse(self.instance.contains(None))

        self.instance.push("string1")
        self.instance.push("string2")
        self.instance.push("string1")
        self.assertTrue(self.instance.contains("string1"))
    
    def testPeek(self):
        self.assertRaises(StackException,self.instance.peek)
        self.instance.push("string1")
        self.instance.push("string2")
        self.assertEqual("string2",self.instance.peek())
        self.assertEqual(2,self.instance.size)
        self.assertEqual(["string1","string2"],self.instance.Stack)
    
    def testPush(self):        
        self.instance.push("string1")
        self.instance.push("string2")
        self.instance.push("string3")
        self.assertEqual(["string1","string2","string3"],self.instance.Stack)

        self.instance.push("")
        self.instance.push("")
        self.assertEqual(["string1","string2","string3","",""],self.instance.Stack)

        self.instance.push(None)
        self.instance.push("string1")
        self.assertEqual(["string1","string2","string3","","",None,"string1"],self.instance.Stack)

    def testPop(self):
        self.assertRaises(StackException,self.instance.pop)

        self.instance.push("string1")
        self.instance.push("string2")
        popvalue= self.instance.pop()
        self.assertEqual(["string1"],self.instance.Stack)
        self.assertEqual(1,self.instance.size)
        self.assertEqual(popvalue,"string2")

        popvalue= self.instance.pop()
        self.assertEqual([],self.instance.Stack)
        self.assertEqual(0,self.instance.size)
        self.assertEqual(popvalue,"string1")

        self.assertRaises(StackException,self.instance.pop)
    
    def testIsEmpty(self):
        self.assertTrue(self.instance.isEmpty())
        self.instance.push("string1")
        self.assertFalse(self.instance.isEmpty())
        self.instance.pop()
        self.assertTrue(self.instance.isEmpty())
        

if __name__ == '__main__':
    unittest.main()