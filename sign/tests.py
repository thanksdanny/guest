from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101', email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'beijing')
        self.assertTrue(result.status)

    def test_guess_models(self):
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    """测试index首页"""
    def test_index_page_renders_index_template(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    '''测试登陆动作'''
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_admin(self):
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@mail.com")

    def test_login_action_username_password_null(self):
        '''用户名为空'''
        test_data = {'username': '', 'password': ''}
        response = self.client.post('login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login_action', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        '''登陆成功'''
        test_data = {'username': 'admin', 'password': 'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
    """发布会管理"""
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_event_mange_success(self):
        '''测试发布会：xiaomi5'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_event_mange_search_success(self):
        '''测试发布搜索'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)
