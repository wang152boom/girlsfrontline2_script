from survey import AnonymousSurvey
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """this is a class for test function"""
    def setUp(self) -> None:
        question = 'what lan'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['en', 'zh', 'rb']

    def test_storge_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_storge_mul_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

