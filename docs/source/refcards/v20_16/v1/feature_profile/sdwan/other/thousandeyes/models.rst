======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    OptionType = Literal["variable"]


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
        value: Union[Any, str]


    class OneOfVirtualApplicationNameServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[Any, str]


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
        # Select Web Proxy Type
        proxy_type: ProxyType
        proxy_host: Optional[
            Union[
                OneOfVirtualApplicationProxyHostOptionsDef1,
                OneOfVirtualApplicationProxyHostOptionsDef2,
            ]
        ]
        proxy_port: Optional[
            Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        ]


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
        # Select Web Proxy Type
        proxy_type: ThousandeyesProxyType
        pac_url: Optional[
            Union[
                OneOfVirtualApplicationPacUrlOptionsDef1,
                OneOfVirtualApplicationPacUrlOptionsDef2,
            ]
        ]


    class OtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class ProxyConfig3:
        # Select Web Proxy Type
        proxy_type: OtherThousandeyesProxyType


    class SdwanOtherThousandeyesProxyType:
        """
        Select Web Proxy Type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class VariableOptionTypeObjectDef:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ProxyConfig4:
        # Select Web Proxy Type
        proxy_type: SdwanOtherThousandeyesProxyType
        pac_url: Optional[VariableOptionTypeObjectDef]
        proxy_host: Optional[VariableOptionTypeObjectDef]
        proxy_port: Optional[VariableOptionTypeObjectDef]


    class VirtualApplication1:
        # Web Proxy Type Config
        proxy_config: Union[
            ProxyConfig1, ProxyConfig2, ProxyConfig3, ProxyConfig4
        ]
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
        name_server1: Optional[
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
        value: str


    class VirtualApplication2:
        # Web Proxy Type Config
        proxy_config: Union[
            ProxyConfig1, ProxyConfig2, ProxyConfig3, ProxyConfig4
        ]
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
        name_server1: Optional[
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
        thousandeyes profile parcel schema for POST/PUT request
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
        # thousandeyes profile parcel schema for POST/PUT request
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
        thousandeyes profile parcel schema for POST/PUT request
        """

        data: OtherThousandeyesData
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
        # thousandeyes profile parcel schema for POST/PUT request
        payload: Optional[Payload]


    class EditThousandeyesProfileParcelForOtherPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanOtherThousandeyesData:
        # Virtual application Instance
        virtual_application: Optional[
            List[Union[VirtualApplication1, VirtualApplication2]]
        ]


    class EditThousandeyesProfileParcelForOtherPutRequest:
        """
        thousandeyes profile parcel schema for POST/PUT request
        """

        data: SdwanOtherThousandeyesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


