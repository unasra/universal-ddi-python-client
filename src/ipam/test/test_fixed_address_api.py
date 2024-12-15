# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.api.fixed_address_api import FixedAddressApi

from bloxone_client.api_client import ApiClient


class TestFixedAddressApi(unittest.TestCase):
    """FixedAddressApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = FixedAddressApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the fixed address.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Move the fixed address to the recycle bin.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Retrieve fixed addresses.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the fixed address.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the fixed address.
        """
        pass


if __name__ == '__main__':
    unittest.main()
