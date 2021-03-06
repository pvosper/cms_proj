from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import utc

import datetime

from cmsblog.models import Post, Category, Event, Talk, Speaker, Venue


class PostTestCase(TestCase):
    fixtures = ['cmsblog_test_fixture.json', ]

    def setUp(self):
        # Setup is run before every test method.
        self.user = User.objects.get(pk=1)  # pk = 'primary key' (id)

    def test_string_representation(self):
        """Checks to see if Post instance returns correct name string"""
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        """Checks to see if Category instance returns correct name string"""
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class EventTestCase(TestCase):

    def test_string_representation(self):
        """Checks to see if Event instance returns correct name string"""
        expected = "An Event"
        c1 = Event(title=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class TalkTestCase(TestCase):

    def test_string_representation(self):
        """Checks to see if Talk instance returns correct title string"""
        expected = "A Talk"
        c1 = Talk(title=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class SpeakerTestCase(TestCase):

    def test_string_representation(self):
        """Checks to see if Speaker instance returns correct name string"""
        expected = "A Speaker"
        c1 = Speaker(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class VenueTestCase(TestCase):

    def test_string_representation(self):
        """Checks to see if Venue instance returns correct name string"""
        expected = "A Venue"
        c1 = Venue(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['cmsblog_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        """Check to see (List only published)"""
        resp = self.client.get('/')  # todo This will fail with home refactor
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """Check to see (Details only published)"""
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)