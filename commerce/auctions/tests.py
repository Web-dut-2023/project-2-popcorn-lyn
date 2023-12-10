# auctions/tests/test_models.py

from django.test import TestCase
from .models import User, Category, Listing, Bid, Comment

class YourAppModelsTestCase(TestCase):

    def setUp(self):
        # 在测试开始前设置一些初始化数据
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.listing = Listing.objects.create(
            title='Test Listing',
            description='This is a test listing',
            starting_bid=10.00,
            category=self.category,
            creator=self.user
        )

    def test_listing_model(self):
        self.assertEqual(str(self.listing), 'Test Listing')
        self.assertEqual(self.listing.current_bid, 0.00)

    # 添加更多的测试用例...

    def tearDown(self):
        # 在测试结束后进行一些清理操作
        pass
