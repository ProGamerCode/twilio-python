# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class CompositionSettingsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_settings().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/CompositionSettings/Default',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "string",
                "aws_credentials_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "encryption_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "aws_s3_url": "https://www.twilio.com",
                "aws_storage_enabled": true,
                "encryption_enabled": true,
                "url": "https://video.twilio.com/v1/CompositionSettings/Default"
            }
            '''
        ))

        actual = self.client.video.v1.composition_settings().fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_settings().create(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/CompositionSettings/Default',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "aws_credentials_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "encryption_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "aws_s3_url": "https://www.twilio.com",
                "aws_storage_enabled": true,
                "encryption_enabled": true,
                "url": "https://video.twilio.com/v1/CompositionSettings/Default"
            }
            '''
        ))

        actual = self.client.video.v1.composition_settings().create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)
