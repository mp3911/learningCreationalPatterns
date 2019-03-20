from PythonFactory import personFactory
from PythonFactory import log

import sys
sys.tracebacklimit = 0

import unittest

class testPersonFactory(unittest.TestCase):

    def test_Factory(self):
        self.assertEqual(personFactory("funkyPerson").get().age, 25)
        log.info("Yaaaaay!!!")
    
    def test_Output_Function(self):
        self.assertEqual(personFactory("funkyPerson").get().name, "Michal Price")

    def test_Output(self):
        self.assertEqual(personFactory("funkyPerson").get().funk, 10000)

if __name__ == "__main__":
    unittest.main()    