import unittest
from app.models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        self.new_source = Source('test name','test author','test title','test description')
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
        
# if __name__ =='__main__':
    # unittest.main()