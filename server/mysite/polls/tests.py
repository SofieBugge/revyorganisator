"""Tests for the polls-app."""

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):
    """Tests the questions-method and related functions."""

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() should return False for questions published
        in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
