import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_get_repo_stub(self):
        # Note: In real tests, you'd mock GitHub API
        response = self.client.get('/repos/octocat/Hello-World')
        self.assertIn(response.status_code, [200, 503, 404])  # Because it's live

    def test_create_webhook(self):
        response = self.client.post(
            '/repos/octocat/Hello-World/webhooks',
            json={"url": "http://example.com/webhook"}
        )
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
