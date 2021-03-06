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


class DeviceTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Devices/THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enabled": true,
                "deployment_sid": "DLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "bob@twilio.com",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": "2016-07-30T20:00:00Z",
                "date_authenticated": null,
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices/THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Devices/THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .devices.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Devices',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enabled": true,
                "deployment_sid": "DLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "bob@twilio.com",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": "2016-07-30T20:00:00Z",
                "date_authenticated": null,
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices/THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices.create()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .devices.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Devices',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "devices": [],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices?PageSize=50&Page=0",
                    "key": "devices",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "devices": [
                    {
                        "sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "friendly_name": "friendly_name",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "enabled": true,
                        "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "deployment_sid": "DLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "identity": "bob@twilio.com",
                        "date_created": "2016-07-30T20:00:00Z",
                        "date_updated": "2016-07-30T20:00:00Z",
                        "date_authenticated": null,
                        "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices/THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices?PageSize=50&Page=0",
                    "key": "devices",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Devices/THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enabled": true,
                "deployment_sid": "DLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "bob@twilio.com",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": "2016-07-30T20:00:00Z",
                "date_authenticated": null,
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Devices/THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets("FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .devices("THXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
