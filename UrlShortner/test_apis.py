import unittest
from model import db
from run import create_app


class ShortenerTestCase(unittest.TestCase):
    """This class represents the shortener test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.app.testing = True
        self.client = self.app.test_client()
        self.url = {'url': "http://www.google.com", 'short_url': "gog.com"}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_api_can_get_all_urls(self):
        """Test API can get a urls (GET request)."""

        res = self.client.get('/api/url/')
        self.assertEqual(res.status_code, 200)

    def test_api_create_short_url(self):
        """Test API can create a short url (POST request)"""

        res = self.client.post('/api/url/', data=self.url)
        self.assertEqual(res.status_code, 201)

    def test_url_can_be_edited(self):
        """Test API can edit an existing url. (PUT request)"""

        rv = self.client.post('/api/url/', data=self.url)
        self.assertEqual(rv.status_code, 201)

        rv = self.client.put('/api/url/1', data={'url': "https://www.google.com", 'short_url': "goog.com"})
        self.assertEqual(rv.status_code, 200)

        results = self.client.get('/api/url/1')
        self.assertIn('https://www.google.com', str(results.data['url']))

    def test_url_deletion(self):
        """Test API can delete an existing url. (DELETE request)."""

        rv = self.client.post('/api/url/', data=self.url)
        self.assertEqual(rv.status_code, 201)

        res = self.client.delete('/api/url/1')
        self.assertEqual(res.status_code, 200)

        # Test to see if it exists, should return a 400
        result = self.client.get('/api/url/1')
        self.assertEqual(result.status_code, 400)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
