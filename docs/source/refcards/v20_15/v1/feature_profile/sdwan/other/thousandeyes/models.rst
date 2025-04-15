======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    OptionType = Literal["variable"]

    Ipv4SubnetMaskDef = Literal[
        "0.0.0.0",
        "128.0.0.0",
        "192.0.0.0",
        "224.0.0.0",
        "240.0.0.0",
        "248.0.0.0",
        "252.0.0.0",
        "254.0.0.0",
        "255.0.0.0",
        "255.128.0.0",
        "255.192.0.0",
        "255.224.0.0",
        "255.240.0.0",
        "255.252.0.0",
        "255.254.0.0",
        "255.255.0.0",
        "255.255.128.0",
        "255.255.192.0",
        "255.255.224.0",
        "255.255.240.0",
        "255.255.248.0",
        "255.255.252.0",
        "255.255.254.0",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
        "255.255.255.254",
        "255.255.255.255",
    ]


    class OneOfVirtualApplicationTokenOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationTokenOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVirtualApplicationVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVirtualApplicationVpnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVirtualApplicationVpnOptionsDef3:
        option_type: DefaultOptionTypeDef


    class TeMgmtIp:
        option_type: Optional[OptionType]


    class TeMgmtSubnetMask:
        option_type: Optional[OptionType]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationNameServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVirtualApplicationNameServerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationHostnameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationHostnameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVirtualApplicationHostnameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class ProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationProxyHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationProxyHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ProxyConfig1:
        proxy_host: Union[
            OneOfVirtualApplicationProxyHostOptionsDef1,
            OneOfVirtualApplicationProxyHostOptionsDef2,
        ]
        proxy_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        # Select Web Proxy Type
        proxy_type: ProxyType


    class ThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationPacUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationPacUrlOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ProxyConfig2:
        pac_url: Union[
            OneOfVirtualApplicationPacUrlOptionsDef1,
            OneOfVirtualApplicationPacUrlOptionsDef2,
        ]
        # Select Web Proxy Type
        proxy_type: ThousandeyesProxyType


    class OtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class ProxyConfig3:
        # Select Web Proxy Type
        proxy_type: OtherThousandeyesProxyType


    class VirtualApplication1:
        # Web Proxy Type Config
        proxy_config: Union[ProxyConfig1, ProxyConfig2, ProxyConfig3]
        token: Union[
            OneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                OneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                OneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[TeMgmtIp]
        te_mgmt_subnet_mask: Optional[TeMgmtSubnetMask]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class OneOfIpV4SubnetMaskOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class VirtualApplication2:
        # Web Proxy Type Config
        proxy_config: Union[ProxyConfig1, ProxyConfig2, ProxyConfig3]
        token: Union[
            OneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                OneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                OneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        te_mgmt_subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class ThousandeyesData:
        # Virtual application Instance
        virtual_application: Optional[
            List[Union[VirtualApplication1, VirtualApplication2]]
        ]


    class Payload:
        """
        thousandeyes profile parcel schema for POST request
        """

        data: ThousandeyesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


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
        # thousandeyes profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanOtherThousandeyesPayload:
        data: Optional[List[Data]]


    class CreateThousandeyesProfileParcelForOtherPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OtherThousandeyesData:
        # Virtual application Instance
        virtual_application: Optional[
            List[Union[VirtualApplication1, VirtualApplication2]]
        ]


    class CreateThousandeyesProfileParcelForOtherPostRequest:
        """
        thousandeyes profile parcel schema for POST request
        """

        data: OtherThousandeyesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class ThousandeyesOneOfVirtualApplicationTokenOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ThousandeyesOneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ThousandeyesOneOfVirtualApplicationHostnameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ThousandeyesProxyConfig1:
        proxy_host: Union[
            ThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1,
            OneOfVirtualApplicationProxyHostOptionsDef2,
        ]
        proxy_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        # Select Web Proxy Type
        proxy_type: ProxyType


    class SdwanOtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class ThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ThousandeyesProxyConfig2:
        pac_url: Union[
            ThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1,
            OneOfVirtualApplicationPacUrlOptionsDef2,
        ]
        # Select Web Proxy Type
        proxy_type: SdwanOtherThousandeyesProxyType


    class ThousandeyesVirtualApplication1:
        # Web Proxy Type Config
        proxy_config: Union[
            ThousandeyesProxyConfig1,
            ThousandeyesProxyConfig2,
            ProxyConfig3,
        ]
        token: Union[
            ThousandeyesOneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                ThousandeyesOneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                ThousandeyesOneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[TeMgmtIp]
        te_mgmt_subnet_mask: Optional[TeMgmtSubnetMask]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class OtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OtherThousandeyesProxyConfig1:
        proxy_host: Union[
            OtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1,
            OneOfVirtualApplicationProxyHostOptionsDef2,
        ]
        proxy_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        # Select Web Proxy Type
        proxy_type: ProxyType


    class FeatureProfileSdwanOtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OtherThousandeyesProxyConfig2:
        pac_url: Union[
            OtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1,
            OneOfVirtualApplicationPacUrlOptionsDef2,
        ]
        # Select Web Proxy Type
        proxy_type: FeatureProfileSdwanOtherThousandeyesProxyType


    class ThousandeyesVirtualApplication2:
        # Web Proxy Type Config
        proxy_config: Union[
            OtherThousandeyesProxyConfig1,
            OtherThousandeyesProxyConfig2,
            ProxyConfig3,
        ]
        token: Union[
            OtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                OtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                OtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        te_mgmt_subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class SdwanOtherThousandeyesData:
        # Virtual application Instance
        virtual_application: Optional[
            List[
                Union[
                    ThousandeyesVirtualApplication1,
                    ThousandeyesVirtualApplication2,
                ]
            ]
        ]


    class ThousandeyesPayload:
        """
        thousandeyes profile parcel schema for PUT request
        """

        data: SdwanOtherThousandeyesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanOtherThousandeyesPayload:
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
        # thousandeyes profile parcel schema for PUT request
        payload: Optional[ThousandeyesPayload]


    class EditThousandeyesProfileParcelForOtherPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanOtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanOtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanOtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanOtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanOtherThousandeyesProxyConfig1:
        proxy_host: Union[
            SdwanOtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1,
            OneOfVirtualApplicationProxyHostOptionsDef2,
        ]
        proxy_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        # Select Web Proxy Type
        proxy_type: ProxyType


    class V1FeatureProfileSdwanOtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class SdwanOtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanOtherThousandeyesProxyConfig2:
        pac_url: Union[
            SdwanOtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1,
            OneOfVirtualApplicationPacUrlOptionsDef2,
        ]
        # Select Web Proxy Type
        proxy_type: V1FeatureProfileSdwanOtherThousandeyesProxyType


    class OtherThousandeyesVirtualApplication1:
        # Web Proxy Type Config
        proxy_config: Union[
            SdwanOtherThousandeyesProxyConfig1,
            SdwanOtherThousandeyesProxyConfig2,
            ProxyConfig3,
        ]
        token: Union[
            SdwanOtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                SdwanOtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                SdwanOtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[TeMgmtIp]
        te_mgmt_subnet_mask: Optional[TeMgmtSubnetMask]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanOtherThousandeyesProxyConfig1:
        proxy_host: Union[
            FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationProxyHostOptionsDef1,
            OneOfVirtualApplicationProxyHostOptionsDef2,
        ]
        proxy_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        # Select Web Proxy Type
        proxy_type: ProxyType


    class ProxyType1:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanOtherThousandeyesProxyConfig2:
        pac_url: Union[
            FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationPacUrlOptionsDef1,
            OneOfVirtualApplicationPacUrlOptionsDef2,
        ]
        # Select Web Proxy Type
        proxy_type: ProxyType1


    class OtherThousandeyesVirtualApplication2:
        # Web Proxy Type Config
        proxy_config: Union[
            FeatureProfileSdwanOtherThousandeyesProxyConfig1,
            FeatureProfileSdwanOtherThousandeyesProxyConfig2,
            ProxyConfig3,
        ]
        token: Union[
            FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationTokenOptionsDef1,
            OneOfVirtualApplicationTokenOptionsDef2,
        ]
        hostname: Optional[
            Union[
                FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationHostnameOptionsDef1,
                OneOfVirtualApplicationHostnameOptionsDef2,
                OneOfVirtualApplicationHostnameOptionsDef3,
            ]
        ]
        name_server: Optional[
            Union[
                FeatureProfileSdwanOtherThousandeyesOneOfVirtualApplicationNameServerOptionsDef1,
                OneOfVirtualApplicationNameServerOptionsDef2,
                OneOfVirtualApplicationNameServerOptionsDef3,
            ]
        ]
        te_mgmt_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        te_mgmt_subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]
        te_vpg_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        vpn: Optional[
            Union[
                OneOfVirtualApplicationVpnOptionsDef1,
                OneOfVirtualApplicationVpnOptionsDef2,
                OneOfVirtualApplicationVpnOptionsDef3,
            ]
        ]


    class FeatureProfileSdwanOtherThousandeyesData:
        # Virtual application Instance
        virtual_application: Optional[
            List[
                Union[
                    OtherThousandeyesVirtualApplication1,
                    OtherThousandeyesVirtualApplication2,
                ]
            ]
        ]


    class EditThousandeyesProfileParcelForOtherPutRequest:
        """
        thousandeyes profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanOtherThousandeyesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


