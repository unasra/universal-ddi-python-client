# coding: utf-8

"""
    Infoblox FW API

    Infoblox Threat Defense Cloud is an extension of the Infoblox Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to Infoblox Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. Infoblox Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.api.internal_domain_lists_api import InternalDomainListsApi

from universal_ddi_client.api_client import ApiClient


class TestInternalDomainListsApi(unittest.TestCase):
    """InternalDomainListsApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = InternalDomainListsApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create_internal_domains(self) -> None:
        """Test case for create_internal_domains

        Create Internal Domains.
        """
        pass

    def test_delete_internal_domains(self) -> None:
        """Test case for delete_internal_domains

        Delete Internal Domains.
        """
        pass

    def test_delete_single_internal_domains(self) -> None:
        """Test case for delete_single_internal_domains

        Delete Internal Domains.
        """
        pass

    def test_internal_domains_items_partial_update(self) -> None:
        """Test case for internal_domains_items_partial_update

        Patch Internal Domains.
        """
        pass

    def test_list_internal_domains(self) -> None:
        """Test case for list_internal_domains

        List Internal Domains.
        """
        pass

    def test_read_internal_domains(self) -> None:
        """Test case for read_internal_domains

        Read Internal Domains.
        """
        pass

    def test_update_internal_domains(self) -> None:
        """Test case for update_internal_domains

        Update Internal Domains.
        """
        pass


if __name__ == '__main__':
    unittest.main()
