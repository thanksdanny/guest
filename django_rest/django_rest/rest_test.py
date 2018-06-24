import unittest
import requests

class UserTest(unittest.TestCase):
    '''用户查询测试'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8888/users'
        self.auth = ('admin', 'Ab134679')

    def test_user1(self):
        '''test user admin'''
        r = requests.get(self.base_url+'/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'admin')
        self.assertEqual(result['email', 'admin@mail.com'])

    def test_user2(self):
        '''test user danny'''
        r = requests.get(self.base_url+'/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'danny')
        self.assertEqual(result['email'], 'danny@mail.com')


class GroupsTest(unittest.TestCase):
    '''用户组查询测试'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8888/groups'
        self.auth = ('admin', 'Ab134679')

    def test_groups1(self):
        '''test groups test'''
        r = requests.get(self.base_url+'/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'test')

    def test_group2(self):
        '''test groups developer'''
        r = requests.get(self.base_url+'/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'developer')

if __name__ == '__main__':
    unittest.main()
