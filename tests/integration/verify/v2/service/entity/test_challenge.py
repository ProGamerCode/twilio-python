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


class ChallengeTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .entities("identity") \
                                 .challenges.create(factor_sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", twilio_sandbox_mode="twilio_sandbox_mode")

        values = {'FactorSid': "YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        headers = {'Twilio-Sandbox-Mode': "twilio_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Challenges',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Challenges',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "pending",
                "responded_reason": "none",
                "details": "{\\"message\\": \\"Hi! Mr. John Doe, would you like to sign up?\\", \\"date\\":\\"2020-07-01T12:13:14Z\\", \\"fields\\": [{\\"label\\": \\"Action\\", \\"value\\": \\"Sign up in portal\\"}]}",
                "hidden_details": "{\\"ip\\": \\"172.168.1.234\\"}",
                "factor_type": "push",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .challenges.create(factor_sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .entities("identity") \
                                 .challenges("YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch(twilio_sandbox_mode="twilio_sandbox_mode")

        headers = {'Twilio-Sandbox-Mode': "twilio_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Challenges/YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            headers=headers,
        ))

    def test_fetch_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "pending",
                "responded_reason": "none",
                "details": "{\\"message\\": \\"Hi! Mr. John Doe, would you like to sign up?\\", \\"fields\\": [{\\"label\\": \\"Action\\", \\"value\\": \\"Sign up in portal\\"}]}",
                "hidden_details": "{\\"ip\\": \\"172.168.1.234\\"}",
                "factor_type": "push",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .challenges("YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .entities("identity") \
                                 .challenges.list(twilio_sandbox_mode="twilio_sandbox_mode")

        headers = {'Twilio-Sandbox-Mode': "twilio_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Challenges',
            headers=headers,
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "challenges": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "challenges"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .challenges.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "challenges": [
                    {
                        "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "identity": "ff483d1ff591898a9942916050d2ca3f",
                        "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "date_responded": "2015-07-30T20:00:00Z",
                        "expiration_date": "2015-07-30T20:00:00Z",
                        "status": "pending",
                        "responded_reason": "none",
                        "details": "{\\"message\\": \\"Hi! Mr. John Doe, would you like to sign up?\\", \\"fields\\": [{\\"label\\": \\"Action\\", \\"value\\": \\"Sign up in portal\\"}]}",
                        "hidden_details": "{\\"ip\\": \\"172.168.1.234\\"}",
                        "factor_type": "push",
                        "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "challenges"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .challenges.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .entities("identity") \
                                 .challenges("YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(twilio_sandbox_mode="twilio_sandbox_mode")

        headers = {'Twilio-Sandbox-Mode': "twilio_sandbox_mode", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Challenges/YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            headers=headers,
        ))

    def test_verify_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "approved",
                "responded_reason": "none",
                "details": "{\\"message\\": \\"Hi! Mr. John Doe, would you like to sign up?\\", \\"fields\\": [{\\"label\\": \\"Action\\", \\"value\\": \\"Sign up in portal\\"}]}",
                "hidden_details": "{\\"ip\\": \\"172.168.1.234\\"}",
                "factor_type": "push",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .challenges("YCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
