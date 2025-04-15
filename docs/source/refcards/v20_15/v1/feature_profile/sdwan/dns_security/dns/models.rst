======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class DnsData:
        target_vpns: Optional[Any]


    class Payload1:
        data: DnsData
        description: str
        name: str
        metadata: Optional[Any]


    class RefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef:
        ref_id: RefIdDef


    class BooleanDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDnsServerIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfChildOrgIdOptionsDef:
        option_type: GlobalOptionTypeDef
        # can be empty string
        value: str


    class VpnsObjDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfUidOptionsDef:
        option_type: GlobalOptionTypeDef
        # An Integer and cannot be empty string
        value: str


    class TargetVpns:
        local_domain_bypass_enabled: BooleanDef
        uid: OneOfUidOptionsDef
        umbrella_default: BooleanDef
        vpns: VpnsObjDef
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]


    class DnsSecurityDnsData:
        dns_crypt: BooleanDef
        match_all_vpn: BooleanDef
        child_org_id: Optional[OneOfChildOrgIdOptionsDef]
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]
        local_domain_bypass_enabled: Optional[BooleanDef]
        local_domain_bypass_list: Optional[ReferenceDef]
        # Will be under data field only if matchAllVpn is false, if matchAllVpn is true field should not be in payload
        target_vpns: Optional[List[TargetVpns]]
        umbrella_default: Optional[BooleanDef]


    class Payload2:
        data: DnsSecurityDnsData
        description: str
        name: str
        metadata: Optional[Any]


    class Data:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # dns profile parcel schema for POST request
        payload: Optional[Union[Payload1, Payload2]]


    class GetListSdwanDnsSecurityDnsPayload:
        data: Optional[List[Data]]


    class CreateSigSecurityProfileParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SdwanDnsSecurityDnsData:
        target_vpns: Optional[Any]


    class CreateSigSecurityProfileParcelPostRequest1:
        data: SdwanDnsSecurityDnsData
        description: str
        name: str
        metadata: Optional[Any]


    class FeatureProfileSdwanDnsSecurityDnsData:
        dns_crypt: BooleanDef
        match_all_vpn: BooleanDef
        child_org_id: Optional[OneOfChildOrgIdOptionsDef]
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]
        local_domain_bypass_enabled: Optional[BooleanDef]
        local_domain_bypass_list: Optional[ReferenceDef]
        # Will be under data field only if matchAllVpn is false, if matchAllVpn is true field should not be in payload
        target_vpns: Optional[List[TargetVpns]]
        umbrella_default: Optional[BooleanDef]


    class CreateSigSecurityProfileParcelPostRequest2:
        data: FeatureProfileSdwanDnsSecurityDnsData
        description: str
        name: str
        metadata: Optional[Any]


    class V1FeatureProfileSdwanDnsSecurityDnsData:
        target_vpns: Optional[Any]


    class DnsPayload1:
        data: V1FeatureProfileSdwanDnsSecurityDnsData
        description: str
        name: str
        cg_fp_pp_name_def: Optional[str]
        metadata: Optional[Any]


    class DnsRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class DnsReferenceDef:
        ref_id: DnsRefIdDef


    class DnsOneOfChildOrgIdOptionsDef:
        option_type: GlobalOptionTypeDef
        # can be empty string
        value: str


    class DnsOneOfUidOptionsDef:
        option_type: GlobalOptionTypeDef
        # An Integer and cannot be empty string
        value: str


    class DnsTargetVpns:
        local_domain_bypass_enabled: BooleanDef
        uid: DnsOneOfUidOptionsDef
        umbrella_default: BooleanDef
        vpns: VpnsObjDef
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]


    class Data1:
        dns_crypt: BooleanDef
        match_all_vpn: BooleanDef
        child_org_id: Optional[DnsOneOfChildOrgIdOptionsDef]
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]
        local_domain_bypass_enabled: Optional[BooleanDef]
        local_domain_bypass_list: Optional[DnsReferenceDef]
        # Will be under data field only if matchAllVpn is false, if matchAllVpn is true field should not be in payload
        target_vpns: Optional[List[DnsTargetVpns]]
        umbrella_default: Optional[BooleanDef]


    class DnsPayload2:
        data: Data1
        description: str
        name: str
        cg_fp_pp_name_def: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanDnsSecurityDnsPayload:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # dns profile parcel schema for PUT request
        payload: Optional[Union[DnsPayload1, DnsPayload2]]


    class EditSigSecurityProfileParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class Data2:
        target_vpns: Optional[Any]


    class EditSigSecurityProfileParcelPutRequest1:
        data: Data2
        description: str
        name: str
        cg_fp_pp_name_def: Optional[str]
        metadata: Optional[Any]


    class DnsSecurityDnsRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class DnsSecurityDnsReferenceDef:
        ref_id: DnsSecurityDnsRefIdDef


    class DnsSecurityDnsOneOfChildOrgIdOptionsDef:
        option_type: GlobalOptionTypeDef
        # can be empty string
        value: str


    class DnsSecurityDnsOneOfUidOptionsDef:
        option_type: GlobalOptionTypeDef
        # An Integer and cannot be empty string
        value: str


    class DnsSecurityDnsTargetVpns:
        local_domain_bypass_enabled: BooleanDef
        uid: DnsSecurityDnsOneOfUidOptionsDef
        umbrella_default: BooleanDef
        vpns: VpnsObjDef
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]


    class Data3:
        dns_crypt: BooleanDef
        match_all_vpn: BooleanDef
        child_org_id: Optional[DnsSecurityDnsOneOfChildOrgIdOptionsDef]
        dns_server_ip: Optional[OneOfDnsServerIpOptionsDef]
        local_domain_bypass_enabled: Optional[BooleanDef]
        local_domain_bypass_list: Optional[DnsSecurityDnsReferenceDef]
        # Will be under data field only if matchAllVpn is false, if matchAllVpn is true field should not be in payload
        target_vpns: Optional[List[DnsSecurityDnsTargetVpns]]
        umbrella_default: Optional[BooleanDef]


    class EditSigSecurityProfileParcelPutRequest2:
        data: Data3
        description: str
        name: str
        cg_fp_pp_name_def: Optional[str]
        metadata: Optional[Any]


