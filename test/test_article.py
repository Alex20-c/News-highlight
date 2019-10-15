import unittest
from app.models import Article, Source


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    
    def setUp(self):
         
        self.new_article=Article("associated-press","Jacky","Police: More than a dozen people rescued from SeaWorld ride","Police say more than a dozen people trapped on a ride at SeaWorld in San Diego have been rescued","https://apnews.com/aea502a4689b4f13b0ed6cc890746be7","https://storage.googleapis.com/afs-prod/media/media:4e33d65cbdf9439c806a2f6f07038b66/2048.jpeg","2019-02-19T07:52:32Z","News")

    def test_article(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()
