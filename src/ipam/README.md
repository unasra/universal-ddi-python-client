# ipam
The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

The `ipam` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.1.0
- Generator version: 7.5.0
- Build package: com.infoblox.codegen.UniversalDdiPythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* pydantic

## Getting Started

In your own code, to use this library to connect and interact with ipam,
you can run the following:

```python

import ipam
from ipam.rest import ApiException
from pprint import pprint

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")


# Enter a context with an instance of the API client
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.AddressApi(api_client)
    body = ipam.Address() # Address | 

    try:
        # Create the IP address.
        api_response = api_instance.create(body)
        print("The response of AddressApi->create:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressApi->create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressApi* | [**create**](ipam/docs/AddressApi.md#create) | **POST** /ipam/address | Create the IP address.
*AddressApi* | [**delete**](ipam/docs/AddressApi.md#delete) | **DELETE** /ipam/address/{id} | Move the IP address to the recycle bin.
*AddressApi* | [**list**](ipam/docs/AddressApi.md#list) | **GET** /ipam/address | Retrieve IP addresses.
*AddressApi* | [**read**](ipam/docs/AddressApi.md#read) | **GET** /ipam/address/{id} | Retrieve the IP address.
*AddressApi* | [**update**](ipam/docs/AddressApi.md#update) | **PATCH** /ipam/address/{id} | Update the IP address.
*AddressBlockApi* | [**copy**](ipam/docs/AddressBlockApi.md#copy) | **POST** /ipam/address_block/{id}/copy | Copy the address block.
*AddressBlockApi* | [**create**](ipam/docs/AddressBlockApi.md#create) | **POST** /ipam/address_block | Create the address block.
*AddressBlockApi* | [**create_next_available_ab**](ipam/docs/AddressBlockApi.md#create_next_available_ab) | **POST** /ipam/address_block/{id}/nextavailableaddressblock | Create the Next Available Address Block object.
*AddressBlockApi* | [**create_next_available_ip**](ipam/docs/AddressBlockApi.md#create_next_available_ip) | **POST** /ipam/address_block/{id}/nextavailableip | Allocate the next available IP address.
*AddressBlockApi* | [**create_next_available_subnet**](ipam/docs/AddressBlockApi.md#create_next_available_subnet) | **POST** /ipam/address_block/{id}/nextavailablesubnet | Create the Next Available Subnet object.
*AddressBlockApi* | [**delete**](ipam/docs/AddressBlockApi.md#delete) | **DELETE** /ipam/address_block/{id} | Move the address block to the recycle bin.
*AddressBlockApi* | [**list**](ipam/docs/AddressBlockApi.md#list) | **GET** /ipam/address_block | Retrieve the address blocks.
*AddressBlockApi* | [**list_ancestor**](ipam/docs/AddressBlockApi.md#list_ancestor) | **GET** /ipam/address_block/{id}/ancestor | Retrieve address block ancestors.
*AddressBlockApi* | [**list_next_available_ab**](ipam/docs/AddressBlockApi.md#list_next_available_ab) | **GET** /ipam/address_block/{id}/nextavailableaddressblock | List Next Available Address Block objects.
*AddressBlockApi* | [**list_next_available_ip**](ipam/docs/AddressBlockApi.md#list_next_available_ip) | **GET** /ipam/address_block/{id}/nextavailableip | Retrieve the next available IP address.
*AddressBlockApi* | [**list_next_available_subnet**](ipam/docs/AddressBlockApi.md#list_next_available_subnet) | **GET** /ipam/address_block/{id}/nextavailablesubnet | List Next Available Subnet objects.
*AddressBlockApi* | [**read**](ipam/docs/AddressBlockApi.md#read) | **GET** /ipam/address_block/{id} | Retrieve the address block.
*AddressBlockApi* | [**update**](ipam/docs/AddressBlockApi.md#update) | **PATCH** /ipam/address_block/{id} | Update the address block.
*AsmApi* | [**create**](ipam/docs/AsmApi.md#create) | **POST** /ipam/asm | Update subnet and ranges for Automated Scope Management.
*AsmApi* | [**list**](ipam/docs/AsmApi.md#list) | **GET** /ipam/asm | Retrieve suggested updates for Automated Scope Management.
*AsmApi* | [**read**](ipam/docs/AsmApi.md#read) | **GET** /ipam/asm/{id} | Retrieve the suggested update for Automated Scope Management.
*ConfigProfileApi* | [**associate_config_profile_to_objects**](ipam/docs/ConfigProfileApi.md#associate_config_profile_to_objects) | **POST** /dhcp/config_profile/link_profile | Associate a config profile to objects.
*ConfigProfileApi* | [**associate_object_to_config_profiles**](ipam/docs/ConfigProfileApi.md#associate_object_to_config_profiles) | **POST** /dhcp/config_profile/link_object | Associate an object to config profiles.
*ConfigProfileApi* | [**disassociate_config_profile_from_objects**](ipam/docs/ConfigProfileApi.md#disassociate_config_profile_from_objects) | **POST** /dhcp/config_profile/delink_profile | Disassociate a config profile from objects.
*ConfigProfileApi* | [**disassociate_object_from_config_profiles**](ipam/docs/ConfigProfileApi.md#disassociate_object_from_config_profiles) | **POST** /dhcp/config_profile/delink_object | Disassociate an object from a config profile.
*ConfigProfileApi* | [**list_config_profiles**](ipam/docs/ConfigProfileApi.md#list_config_profiles) | **GET** /dhcp/config_profile/profiles | Retrieve config profiles.
*ConfigProfileApi* | [**list_subnets**](ipam/docs/ConfigProfileApi.md#list_subnets) | **GET** /dhcp/config_profile/subnets | Retrieve subnets associated with a config profile.
*DhcpHostApi* | [**list**](ipam/docs/DhcpHostApi.md#list) | **GET** /dhcp/host | Retrieve DHCP hosts.
*DhcpHostApi* | [**list_associations**](ipam/docs/DhcpHostApi.md#list_associations) | **GET** /dhcp/host/{id}/associations | Retrieve DHCP host associations.
*DhcpHostApi* | [**read**](ipam/docs/DhcpHostApi.md#read) | **GET** /dhcp/host/{id} | Retrieve the DHCP host.
*DhcpHostApi* | [**update**](ipam/docs/DhcpHostApi.md#update) | **PATCH** /dhcp/host/{id} | Update the DHCP hosts.
*DnsUsageApi* | [**list**](ipam/docs/DnsUsageApi.md#list) | **GET** /ipam/dns_usage | Retrieve DNS usage for multiple objects.
*DnsUsageApi* | [**read**](ipam/docs/DnsUsageApi.md#read) | **GET** /ipam/dns_usage/{id} | Retrieve the DNS usage.
*FilterApi* | [**list**](ipam/docs/FilterApi.md#list) | **GET** /dhcp/filter | Retrieve DHCP filters.
*FixedAddressApi* | [**create**](ipam/docs/FixedAddressApi.md#create) | **POST** /dhcp/fixed_address | Create the fixed address.
*FixedAddressApi* | [**delete**](ipam/docs/FixedAddressApi.md#delete) | **DELETE** /dhcp/fixed_address/{id} | Move the fixed address to the recycle bin.
*FixedAddressApi* | [**list**](ipam/docs/FixedAddressApi.md#list) | **GET** /dhcp/fixed_address | Retrieve fixed addresses.
*FixedAddressApi* | [**read**](ipam/docs/FixedAddressApi.md#read) | **GET** /dhcp/fixed_address/{id} | Retrieve the fixed address.
*FixedAddressApi* | [**update**](ipam/docs/FixedAddressApi.md#update) | **PATCH** /dhcp/fixed_address/{id} | Update the fixed address.
*GlobalApi* | [**read**](ipam/docs/GlobalApi.md#read) | **GET** /dhcp/global | Retrieve the global configuration.
*GlobalApi* | [**read_by_id**](ipam/docs/GlobalApi.md#read_by_id) | **GET** /dhcp/global/{id} | Retrieve the global configuration.
*GlobalApi* | [**update**](ipam/docs/GlobalApi.md#update) | **PATCH** /dhcp/global | Update the global configuration.
*GlobalApi* | [**update_by_id**](ipam/docs/GlobalApi.md#update_by_id) | **PATCH** /dhcp/global/{id} | Update the global configuration.
*HaGroupApi* | [**create**](ipam/docs/HaGroupApi.md#create) | **POST** /dhcp/ha_group | Create the HA group.
*HaGroupApi* | [**delete**](ipam/docs/HaGroupApi.md#delete) | **DELETE** /dhcp/ha_group/{id} | Delete the HA group.
*HaGroupApi* | [**list**](ipam/docs/HaGroupApi.md#list) | **GET** /dhcp/ha_group | Retrieve HA groups.
*HaGroupApi* | [**read**](ipam/docs/HaGroupApi.md#read) | **GET** /dhcp/ha_group/{id} | Retrieve the HA group.
*HaGroupApi* | [**update**](ipam/docs/HaGroupApi.md#update) | **PATCH** /dhcp/ha_group/{id} | Update the HA group.
*HardwareFilterApi* | [**create**](ipam/docs/HardwareFilterApi.md#create) | **POST** /dhcp/hardware_filter | Create the hardware filter.
*HardwareFilterApi* | [**delete**](ipam/docs/HardwareFilterApi.md#delete) | **DELETE** /dhcp/hardware_filter/{id} | Move the hardware filter to the recycle bin.
*HardwareFilterApi* | [**list**](ipam/docs/HardwareFilterApi.md#list) | **GET** /dhcp/hardware_filter | Retrieve hardware filters.
*HardwareFilterApi* | [**read**](ipam/docs/HardwareFilterApi.md#read) | **GET** /dhcp/hardware_filter/{id} | Retrieve the hardware filter.
*HardwareFilterApi* | [**update**](ipam/docs/HardwareFilterApi.md#update) | **PATCH** /dhcp/hardware_filter/{id} | Update the hardware filter.
*IpSpaceApi* | [**bulk_copy**](ipam/docs/IpSpaceApi.md#bulk_copy) | **POST** /ipam/ip_space/bulk_copy | Copy the specified address block and subnets in the IP space.
*IpSpaceApi* | [**copy**](ipam/docs/IpSpaceApi.md#copy) | **POST** /ipam/ip_space/{id}/copy | Copy the IP space.
*IpSpaceApi* | [**create**](ipam/docs/IpSpaceApi.md#create) | **POST** /ipam/ip_space | Create the IP space.
*IpSpaceApi* | [**delete**](ipam/docs/IpSpaceApi.md#delete) | **DELETE** /ipam/ip_space/{id} | Move the IP space to the recycle bin.
*IpSpaceApi* | [**get_conflicts**](ipam/docs/IpSpaceApi.md#get_conflicts) | **GET** /ipam/ip_space/{id}/conflicts | Retrieve Conflicted __AddressBlock__ and __Subnet__ objects in Federated Realms.
*IpSpaceApi* | [**list**](ipam/docs/IpSpaceApi.md#list) | **GET** /ipam/ip_space | Retrieve IP spaces.
*IpSpaceApi* | [**read**](ipam/docs/IpSpaceApi.md#read) | **GET** /ipam/ip_space/{id} | Retrieve the IP space.
*IpSpaceApi* | [**update**](ipam/docs/IpSpaceApi.md#update) | **PATCH** /ipam/ip_space/{id} | Update the IP space.
*IpamHostApi* | [**create**](ipam/docs/IpamHostApi.md#create) | **POST** /ipam/host | Create the IPAM host.
*IpamHostApi* | [**delete**](ipam/docs/IpamHostApi.md#delete) | **DELETE** /ipam/host/{id} | Move the IPAM host to the recycle bin.
*IpamHostApi* | [**list**](ipam/docs/IpamHostApi.md#list) | **GET** /ipam/host | Retrieve the IPAM hosts.
*IpamHostApi* | [**read**](ipam/docs/IpamHostApi.md#read) | **GET** /ipam/host/{id} | Retrieve the IPAM host.
*IpamHostApi* | [**update**](ipam/docs/IpamHostApi.md#update) | **PATCH** /ipam/host/{id} | Update the IPAM host.
*LeasesCommandApi* | [**create**](ipam/docs/LeasesCommandApi.md#create) | **POST** /dhcp/leases_command | Perform actions like clearing DHCP lease(s).
*MacAddressItemApi* | [**bulk_create**](ipam/docs/MacAddressItemApi.md#bulk_create) | **POST** /dhcp/mac_address_item/bulk_create | Bulk create the mac address items.
*MacAddressItemApi* | [**create**](ipam/docs/MacAddressItemApi.md#create) | **POST** /dhcp/mac_address_item | Create the mac address item.
*MacAddressItemApi* | [**delete**](ipam/docs/MacAddressItemApi.md#delete) | **DELETE** /dhcp/mac_address_item/{id} | Delete the mac address item.
*MacAddressItemApi* | [**list**](ipam/docs/MacAddressItemApi.md#list) | **GET** /dhcp/mac_address_item | Retrieve mac address items.
*MacAddressItemApi* | [**read**](ipam/docs/MacAddressItemApi.md#read) | **GET** /dhcp/mac_address_item/{id} | Retrieve the mac address item.
*MacAddressItemApi* | [**update**](ipam/docs/MacAddressItemApi.md#update) | **PATCH** /dhcp/mac_address_item/{id} | Update the mac address item.
*MacAddressItemApi* | [**upload**](ipam/docs/MacAddressItemApi.md#upload) | **POST** /dhcp/mac_address_item/upload | Upload mac addresses to a large scale hardware filter.
*OptionCodeApi* | [**create**](ipam/docs/OptionCodeApi.md#create) | **POST** /dhcp/option_code | Create the DHCP option code.
*OptionCodeApi* | [**delete**](ipam/docs/OptionCodeApi.md#delete) | **DELETE** /dhcp/option_code/{id} | Delete the DHCP option code.
*OptionCodeApi* | [**list**](ipam/docs/OptionCodeApi.md#list) | **GET** /dhcp/option_code | Retrieve DHCP option codes.
*OptionCodeApi* | [**read**](ipam/docs/OptionCodeApi.md#read) | **GET** /dhcp/option_code/{id} | Retrieve the DHCP option code.
*OptionCodeApi* | [**update**](ipam/docs/OptionCodeApi.md#update) | **PATCH** /dhcp/option_code/{id} | Update the DHCP option code.
*OptionFilterApi* | [**create**](ipam/docs/OptionFilterApi.md#create) | **POST** /dhcp/option_filter | Create the DHCP option filter.
*OptionFilterApi* | [**delete**](ipam/docs/OptionFilterApi.md#delete) | **DELETE** /dhcp/option_filter/{id} | Move the DHCP option filter to the recycle bin.
*OptionFilterApi* | [**list**](ipam/docs/OptionFilterApi.md#list) | **GET** /dhcp/option_filter | Retrieve DHCP option filters.
*OptionFilterApi* | [**read**](ipam/docs/OptionFilterApi.md#read) | **GET** /dhcp/option_filter/{id} | Retrieve the DHCP option filter.
*OptionFilterApi* | [**update**](ipam/docs/OptionFilterApi.md#update) | **PATCH** /dhcp/option_filter/{id} | Update the DHCP option filter.
*OptionGroupApi* | [**create**](ipam/docs/OptionGroupApi.md#create) | **POST** /dhcp/option_group | Create the DHCP option group.
*OptionGroupApi* | [**delete**](ipam/docs/OptionGroupApi.md#delete) | **DELETE** /dhcp/option_group/{id} | Move the DHCP option group to the recycle bin.
*OptionGroupApi* | [**list**](ipam/docs/OptionGroupApi.md#list) | **GET** /dhcp/option_group | Retrieve DHCP option groups.
*OptionGroupApi* | [**read**](ipam/docs/OptionGroupApi.md#read) | **GET** /dhcp/option_group/{id} | Retrieve the DHCP option group.
*OptionGroupApi* | [**update**](ipam/docs/OptionGroupApi.md#update) | **PATCH** /dhcp/option_group/{id} | Update the DHCP option group.
*OptionSpaceApi* | [**create**](ipam/docs/OptionSpaceApi.md#create) | **POST** /dhcp/option_space | Create the DHCP option space.
*OptionSpaceApi* | [**delete**](ipam/docs/OptionSpaceApi.md#delete) | **DELETE** /dhcp/option_space/{id} | Move the DHCP option space to the recycle bin.
*OptionSpaceApi* | [**list**](ipam/docs/OptionSpaceApi.md#list) | **GET** /dhcp/option_space | Retrieve DHCP option spaces.
*OptionSpaceApi* | [**read**](ipam/docs/OptionSpaceApi.md#read) | **GET** /dhcp/option_space/{id} | Retrieve the DHCP option space.
*OptionSpaceApi* | [**update**](ipam/docs/OptionSpaceApi.md#update) | **PATCH** /dhcp/option_space/{id} | Update the DHCP option space.
*RangeApi* | [**create**](ipam/docs/RangeApi.md#create) | **POST** /ipam/range | Create the range.
*RangeApi* | [**create_next_available_ip**](ipam/docs/RangeApi.md#create_next_available_ip) | **POST** /ipam/range/{id}/nextavailableip | Allocate the next available IP address.
*RangeApi* | [**delete**](ipam/docs/RangeApi.md#delete) | **DELETE** /ipam/range/{id} | Move the range to the recycle bin.
*RangeApi* | [**list**](ipam/docs/RangeApi.md#list) | **GET** /ipam/range | Retrieve ranges.
*RangeApi* | [**list_next_available_ip**](ipam/docs/RangeApi.md#list_next_available_ip) | **GET** /ipam/range/{id}/nextavailableip | Retrieve the next available IP address.
*RangeApi* | [**read**](ipam/docs/RangeApi.md#read) | **GET** /ipam/range/{id} | Retrieve the range.
*RangeApi* | [**update**](ipam/docs/RangeApi.md#update) | **PATCH** /ipam/range/{id} | Update the range.
*ServerApi* | [**create**](ipam/docs/ServerApi.md#create) | **POST** /dhcp/server | Create the DHCP configuration profile.
*ServerApi* | [**delete**](ipam/docs/ServerApi.md#delete) | **DELETE** /dhcp/server/{id} | Move the DHCP configuration profile to the recycle bin.
*ServerApi* | [**list**](ipam/docs/ServerApi.md#list) | **GET** /dhcp/server | Retrieve DHCP configuration profiles.
*ServerApi* | [**read**](ipam/docs/ServerApi.md#read) | **GET** /dhcp/server/{id} | Retrieve the DHCP configuration profile.
*ServerApi* | [**update**](ipam/docs/ServerApi.md#update) | **PATCH** /dhcp/server/{id} | Update the DHCP configuration profile.
*ServiceApi* | [**list**](ipam/docs/ServiceApi.md#list) | **GET** /dhcp/service | List DHCP service instance objects.
*ServiceApi* | [**read**](ipam/docs/ServiceApi.md#read) | **GET** /dhcp/service/{id} | Read the DHCP service instance object.
*SubnetApi* | [**copy**](ipam/docs/SubnetApi.md#copy) | **POST** /ipam/subnet/{id}/copy | Copy the subnet.
*SubnetApi* | [**create**](ipam/docs/SubnetApi.md#create) | **POST** /ipam/subnet | Create the subnet.
*SubnetApi* | [**create_next_available_ip**](ipam/docs/SubnetApi.md#create_next_available_ip) | **POST** /ipam/subnet/{id}/nextavailableip | Allocate the next available IP address.
*SubnetApi* | [**delete**](ipam/docs/SubnetApi.md#delete) | **DELETE** /ipam/subnet/{id} | Move the subnet to the recycle bin.
*SubnetApi* | [**list**](ipam/docs/SubnetApi.md#list) | **GET** /ipam/subnet | Retrieve subnets.
*SubnetApi* | [**list_ancestor**](ipam/docs/SubnetApi.md#list_ancestor) | **GET** /ipam/subnet/{id}/ancestor | Retrieve subnet ancestors.
*SubnetApi* | [**list_next_available_ip**](ipam/docs/SubnetApi.md#list_next_available_ip) | **GET** /ipam/subnet/{id}/nextavailableip | Retrieve the next available IP address.
*SubnetApi* | [**read**](ipam/docs/SubnetApi.md#read) | **GET** /ipam/subnet/{id} | Retrieve the subnet.
*SubnetApi* | [**update**](ipam/docs/SubnetApi.md#update) | **PATCH** /ipam/subnet/{id} | Update the subnet.


## Documentation For Models

 - [ASM](ipam/docs/ASM.md)
 - [ASMConfig](ipam/docs/ASMConfig.md)
 - [AccessFilter](ipam/docs/AccessFilter.md)
 - [Address](ipam/docs/Address.md)
 - [AddressBlock](ipam/docs/AddressBlock.md)
 - [AsmEnableBlock](ipam/docs/AsmEnableBlock.md)
 - [AsmGrowthBlock](ipam/docs/AsmGrowthBlock.md)
 - [AssociateConfigProfileToObjectsRequest](ipam/docs/AssociateConfigProfileToObjectsRequest.md)
 - [AssociateObjectToConfigProfilesRequest](ipam/docs/AssociateObjectToConfigProfilesRequest.md)
 - [AssociatedHost](ipam/docs/AssociatedHost.md)
 - [BulkCopyError](ipam/docs/BulkCopyError.md)
 - [BulkCopyIPSpace](ipam/docs/BulkCopyIPSpace.md)
 - [BulkCopyIPSpaceResponse](ipam/docs/BulkCopyIPSpaceResponse.md)
 - [BulkCreateMacAddressItemResponse](ipam/docs/BulkCreateMacAddressItemResponse.md)
 - [BulkMacAddressItem](ipam/docs/BulkMacAddressItem.md)
 - [CPSubnet](ipam/docs/CPSubnet.md)
 - [CidrBlock](ipam/docs/CidrBlock.md)
 - [CopyAddressBlock](ipam/docs/CopyAddressBlock.md)
 - [CopyAddressBlockResponse](ipam/docs/CopyAddressBlockResponse.md)
 - [CopyIPSpace](ipam/docs/CopyIPSpace.md)
 - [CopyIPSpaceResponse](ipam/docs/CopyIPSpaceResponse.md)
 - [CopyResponse](ipam/docs/CopyResponse.md)
 - [CopySubnet](ipam/docs/CopySubnet.md)
 - [CopySubnetResponse](ipam/docs/CopySubnetResponse.md)
 - [CreateASMResponse](ipam/docs/CreateASMResponse.md)
 - [CreateAddressBlockResponse](ipam/docs/CreateAddressBlockResponse.md)
 - [CreateAddressResponse](ipam/docs/CreateAddressResponse.md)
 - [CreateFixedAddressResponse](ipam/docs/CreateFixedAddressResponse.md)
 - [CreateHAGroupResponse](ipam/docs/CreateHAGroupResponse.md)
 - [CreateHardwareFilterResponse](ipam/docs/CreateHardwareFilterResponse.md)
 - [CreateIPSpaceResponse](ipam/docs/CreateIPSpaceResponse.md)
 - [CreateIpamHostResponse](ipam/docs/CreateIpamHostResponse.md)
 - [CreateLeasesCommandResponse](ipam/docs/CreateLeasesCommandResponse.md)
 - [CreateMacAddressItemResponse](ipam/docs/CreateMacAddressItemResponse.md)
 - [CreateNextAvailableABResponse](ipam/docs/CreateNextAvailableABResponse.md)
 - [CreateNextAvailableIPResponse](ipam/docs/CreateNextAvailableIPResponse.md)
 - [CreateNextAvailableSubnetResponse](ipam/docs/CreateNextAvailableSubnetResponse.md)
 - [CreateOptionCodeResponse](ipam/docs/CreateOptionCodeResponse.md)
 - [CreateOptionFilterResponse](ipam/docs/CreateOptionFilterResponse.md)
 - [CreateOptionGroupResponse](ipam/docs/CreateOptionGroupResponse.md)
 - [CreateOptionSpaceResponse](ipam/docs/CreateOptionSpaceResponse.md)
 - [CreateRangeResponse](ipam/docs/CreateRangeResponse.md)
 - [CreateServerResponse](ipam/docs/CreateServerResponse.md)
 - [CreateSubnetResponse](ipam/docs/CreateSubnetResponse.md)
 - [DDNSBlock](ipam/docs/DDNSBlock.md)
 - [DDNSHostnameBlock](ipam/docs/DDNSHostnameBlock.md)
 - [DDNSUpdateBlock](ipam/docs/DDNSUpdateBlock.md)
 - [DDNSZone](ipam/docs/DDNSZone.md)
 - [DHCPConfig](ipam/docs/DHCPConfig.md)
 - [DHCPGlobal](ipam/docs/DHCPGlobal.md)
 - [DHCPInfo](ipam/docs/DHCPInfo.md)
 - [DHCPInheritance](ipam/docs/DHCPInheritance.md)
 - [DHCPOptionsInheritance](ipam/docs/DHCPOptionsInheritance.md)
 - [DHCPPacketStats](ipam/docs/DHCPPacketStats.md)
 - [DHCPServiceInstance](ipam/docs/DHCPServiceInstance.md)
 - [DHCPUtilization](ipam/docs/DHCPUtilization.md)
 - [DHCPUtilizationThreshold](ipam/docs/DHCPUtilizationThreshold.md)
 - [DNSUsage](ipam/docs/DNSUsage.md)
 - [DisassociateConfigProfileFromObjectsRequest](ipam/docs/DisassociateConfigProfileFromObjectsRequest.md)
 - [DisassociateObjectFromConfigProfilesRequest](ipam/docs/DisassociateObjectFromConfigProfilesRequest.md)
 - [ExclusionRange](ipam/docs/ExclusionRange.md)
 - [Filter](ipam/docs/Filter.md)
 - [FixedAddress](ipam/docs/FixedAddress.md)
 - [FixedAddressInheritance](ipam/docs/FixedAddressInheritance.md)
 - [HAGroup](ipam/docs/HAGroup.md)
 - [HAGroupHeartbeats](ipam/docs/HAGroupHeartbeats.md)
 - [HAGroupHost](ipam/docs/HAGroupHost.md)
 - [HardwareFilter](ipam/docs/HardwareFilter.md)
 - [Host](ipam/docs/Host.md)
 - [HostAddress](ipam/docs/HostAddress.md)
 - [HostAssociatedServer](ipam/docs/HostAssociatedServer.md)
 - [HostAssociationsResponse](ipam/docs/HostAssociationsResponse.md)
 - [HostName](ipam/docs/HostName.md)
 - [HostnameRewriteBlock](ipam/docs/HostnameRewriteBlock.md)
 - [IPSpace](ipam/docs/IPSpace.md)
 - [IPSpaceInheritance](ipam/docs/IPSpaceInheritance.md)
 - [IgnoreItem](ipam/docs/IgnoreItem.md)
 - [InheritanceAssignedHost](ipam/docs/InheritanceAssignedHost.md)
 - [InheritanceInheritedBool](ipam/docs/InheritanceInheritedBool.md)
 - [InheritanceInheritedFloat](ipam/docs/InheritanceInheritedFloat.md)
 - [InheritanceInheritedIdentifier](ipam/docs/InheritanceInheritedIdentifier.md)
 - [InheritanceInheritedString](ipam/docs/InheritanceInheritedString.md)
 - [InheritanceInheritedUInt32](ipam/docs/InheritanceInheritedUInt32.md)
 - [InheritedASMConfig](ipam/docs/InheritedASMConfig.md)
 - [InheritedAsmEnableBlock](ipam/docs/InheritedAsmEnableBlock.md)
 - [InheritedAsmGrowthBlock](ipam/docs/InheritedAsmGrowthBlock.md)
 - [InheritedDDNSBlock](ipam/docs/InheritedDDNSBlock.md)
 - [InheritedDDNSHostnameBlock](ipam/docs/InheritedDDNSHostnameBlock.md)
 - [InheritedDDNSUpdateBlock](ipam/docs/InheritedDDNSUpdateBlock.md)
 - [InheritedDHCPConfig](ipam/docs/InheritedDHCPConfig.md)
 - [InheritedDHCPConfigFilterList](ipam/docs/InheritedDHCPConfigFilterList.md)
 - [InheritedDHCPConfigIgnoreItemList](ipam/docs/InheritedDHCPConfigIgnoreItemList.md)
 - [InheritedDHCPOption](ipam/docs/InheritedDHCPOption.md)
 - [InheritedDHCPOptionItem](ipam/docs/InheritedDHCPOptionItem.md)
 - [InheritedDHCPOptionList](ipam/docs/InheritedDHCPOptionList.md)
 - [InheritedHostnameRewriteBlock](ipam/docs/InheritedHostnameRewriteBlock.md)
 - [IpamHost](ipam/docs/IpamHost.md)
 - [KerberosKey](ipam/docs/KerberosKey.md)
 - [LeaseAddress](ipam/docs/LeaseAddress.md)
 - [LeaseRange](ipam/docs/LeaseRange.md)
 - [LeaseSubnet](ipam/docs/LeaseSubnet.md)
 - [LeasesCommand](ipam/docs/LeasesCommand.md)
 - [ListASMResponse](ipam/docs/ListASMResponse.md)
 - [ListAddressBlockResponse](ipam/docs/ListAddressBlockResponse.md)
 - [ListAddressResponse](ipam/docs/ListAddressResponse.md)
 - [ListAncestorResponse](ipam/docs/ListAncestorResponse.md)
 - [ListCPSubnetResponse](ipam/docs/ListCPSubnetResponse.md)
 - [ListConfigProfileResponse](ipam/docs/ListConfigProfileResponse.md)
 - [ListDHCPServiceInstanceResponse](ipam/docs/ListDHCPServiceInstanceResponse.md)
 - [ListDNSUsageResponse](ipam/docs/ListDNSUsageResponse.md)
 - [ListFilterResponse](ipam/docs/ListFilterResponse.md)
 - [ListFixedAddressResponse](ipam/docs/ListFixedAddressResponse.md)
 - [ListHAGroupResponse](ipam/docs/ListHAGroupResponse.md)
 - [ListHardwareFilterResponse](ipam/docs/ListHardwareFilterResponse.md)
 - [ListHostResponse](ipam/docs/ListHostResponse.md)
 - [ListIPSpaceResponse](ipam/docs/ListIPSpaceResponse.md)
 - [ListIpamHostResponse](ipam/docs/ListIpamHostResponse.md)
 - [ListMacAddressItemResponse](ipam/docs/ListMacAddressItemResponse.md)
 - [ListOptionCodeResponse](ipam/docs/ListOptionCodeResponse.md)
 - [ListOptionFilterResponse](ipam/docs/ListOptionFilterResponse.md)
 - [ListOptionGroupResponse](ipam/docs/ListOptionGroupResponse.md)
 - [ListOptionSpaceResponse](ipam/docs/ListOptionSpaceResponse.md)
 - [ListRangeResponse](ipam/docs/ListRangeResponse.md)
 - [ListServerResponse](ipam/docs/ListServerResponse.md)
 - [ListSubnetResponse](ipam/docs/ListSubnetResponse.md)
 - [MacAddressItem](ipam/docs/MacAddressItem.md)
 - [MacAddressItemUpload](ipam/docs/MacAddressItemUpload.md)
 - [MacAddressItemUploadResponse](ipam/docs/MacAddressItemUploadResponse.md)
 - [Name](ipam/docs/Name.md)
 - [Nameserver](ipam/docs/Nameserver.md)
 - [NextAvailableABResponse](ipam/docs/NextAvailableABResponse.md)
 - [NextAvailableIPResponse](ipam/docs/NextAvailableIPResponse.md)
 - [NextAvailableSubnetResponse](ipam/docs/NextAvailableSubnetResponse.md)
 - [OptionCode](ipam/docs/OptionCode.md)
 - [OptionFilter](ipam/docs/OptionFilter.md)
 - [OptionFilterRule](ipam/docs/OptionFilterRule.md)
 - [OptionFilterRuleList](ipam/docs/OptionFilterRuleList.md)
 - [OptionGroup](ipam/docs/OptionGroup.md)
 - [OptionItem](ipam/docs/OptionItem.md)
 - [OptionSpace](ipam/docs/OptionSpace.md)
 - [ProtobufFieldMask](ipam/docs/ProtobufFieldMask.md)
 - [Range](ipam/docs/Range.md)
 - [ReadASMResponse](ipam/docs/ReadASMResponse.md)
 - [ReadAddressBlockResponse](ipam/docs/ReadAddressBlockResponse.md)
 - [ReadAddressResponse](ipam/docs/ReadAddressResponse.md)
 - [ReadDHCPServiceInstanceResponse](ipam/docs/ReadDHCPServiceInstanceResponse.md)
 - [ReadDNSUsageResponse](ipam/docs/ReadDNSUsageResponse.md)
 - [ReadFixedAddressResponse](ipam/docs/ReadFixedAddressResponse.md)
 - [ReadGlobalResponse](ipam/docs/ReadGlobalResponse.md)
 - [ReadHAGroupResponse](ipam/docs/ReadHAGroupResponse.md)
 - [ReadHardwareFilterResponse](ipam/docs/ReadHardwareFilterResponse.md)
 - [ReadHostResponse](ipam/docs/ReadHostResponse.md)
 - [ReadIPSpaceResponse](ipam/docs/ReadIPSpaceResponse.md)
 - [ReadIpamHostResponse](ipam/docs/ReadIpamHostResponse.md)
 - [ReadMacAddressItemResponse](ipam/docs/ReadMacAddressItemResponse.md)
 - [ReadOptionCodeResponse](ipam/docs/ReadOptionCodeResponse.md)
 - [ReadOptionFilterResponse](ipam/docs/ReadOptionFilterResponse.md)
 - [ReadOptionGroupResponse](ipam/docs/ReadOptionGroupResponse.md)
 - [ReadOptionSpaceResponse](ipam/docs/ReadOptionSpaceResponse.md)
 - [ReadRangeResponse](ipam/docs/ReadRangeResponse.md)
 - [ReadServerResponse](ipam/docs/ReadServerResponse.md)
 - [ReadSubnetResponse](ipam/docs/ReadSubnetResponse.md)
 - [RealmsConflict](ipam/docs/RealmsConflict.md)
 - [RealmsConflictResponse](ipam/docs/RealmsConflictResponse.md)
 - [Server](ipam/docs/Server.md)
 - [ServerInheritance](ipam/docs/ServerInheritance.md)
 - [Subnet](ipam/docs/Subnet.md)
 - [TSIGKey](ipam/docs/TSIGKey.md)
 - [UpdateAddressBlockResponse](ipam/docs/UpdateAddressBlockResponse.md)
 - [UpdateAddressResponse](ipam/docs/UpdateAddressResponse.md)
 - [UpdateFixedAddressResponse](ipam/docs/UpdateFixedAddressResponse.md)
 - [UpdateGlobalResponse](ipam/docs/UpdateGlobalResponse.md)
 - [UpdateHAGroupResponse](ipam/docs/UpdateHAGroupResponse.md)
 - [UpdateHardwareFilterResponse](ipam/docs/UpdateHardwareFilterResponse.md)
 - [UpdateHostResponse](ipam/docs/UpdateHostResponse.md)
 - [UpdateIPSpaceResponse](ipam/docs/UpdateIPSpaceResponse.md)
 - [UpdateIpamHostResponse](ipam/docs/UpdateIpamHostResponse.md)
 - [UpdateMacAddressItemResponse](ipam/docs/UpdateMacAddressItemResponse.md)
 - [UpdateOptionCodeResponse](ipam/docs/UpdateOptionCodeResponse.md)
 - [UpdateOptionFilterResponse](ipam/docs/UpdateOptionFilterResponse.md)
 - [UpdateOptionGroupResponse](ipam/docs/UpdateOptionGroupResponse.md)
 - [UpdateOptionSpaceResponse](ipam/docs/UpdateOptionSpaceResponse.md)
 - [UpdateRangeResponse](ipam/docs/UpdateRangeResponse.md)
 - [UpdateServerResponse](ipam/docs/UpdateServerResponse.md)
 - [UpdateSubnetResponse](ipam/docs/UpdateSubnetResponse.md)
 - [Utilization](ipam/docs/Utilization.md)
 - [UtilizationThreshold](ipam/docs/UtilizationThreshold.md)
 - [UtilizationV6](ipam/docs/UtilizationV6.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




