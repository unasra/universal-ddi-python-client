# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.convert_rname_api import ConvertRnameApi

from bloxone_client.api_client import ApiClient


class TestConvertRnameApi(unittest.TestCase):
    """ConvertRnameApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = ConvertRnameApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_convert_r_name(self) -> None:
        """Test case for convert_r_name

        Convert the object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
