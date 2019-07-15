import unittest




class sum(unittest.TestCase):
    def testone(self):
        a = 3
        b = 5
        self.assertNotEqual(a,b)
        print("1")



    def testtwo(self):
        a = "we"
        b = "we"
        self.assertEqual(a,b)
        print("2")



    def testthee(self):
        a = "dss"
        b = 5
        self.assertNotEqual(a,b)
        print("3")



    def testfour(self):
        a = "sadfsdf"
        b = "dsfsf"
        self.assertNotEqual(a,b)
        print("4")




if __name__ == '__main__':
    unittest.main()



