======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

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

    DefaultOptionTypeDef = Literal["default"]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


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


    class AddressPool:
        """
        Configure IPv4 prefix range of the DHCP address pool
        """

        network_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfExcludeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[Any, Any]]


    class OneOfExcludeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExcludeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLeaseTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLeaseTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLeaseTimeOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceMtuOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDomainNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDomainNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDomainNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDefaultGatewayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDefaultGatewayOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDnsServersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfDnsServersOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDnsServersOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTftpServersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfTftpServersOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTftpServersOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfStaticLeaseMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfStaticLeaseMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticLeaseIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticLeaseIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class StaticLease:
        ip: Union[
            OneOfStaticLeaseIpOptionsDef1, OneOfStaticLeaseIpOptionsDef2
        ]
        mac_address: Union[
            OneOfStaticLeaseMacAddressOptionsDef1,
            OneOfStaticLeaseMacAddressOptionsDef2,
        ]


    class OneOfOptionCodeCodeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOptionCodeCodeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOptionCodeAsciiOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfOptionCodeAsciiOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OptionCode1:
        ascii: Union[
            OneOfOptionCodeAsciiOptionsDef1,
            OneOfOptionCodeAsciiOptionsDef2,
        ]
        code: Union[
            OneOfOptionCodeCodeOptionsDef1, OneOfOptionCodeCodeOptionsDef2
        ]


    class OneOfOptionCodeHexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfOptionCodeHexOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OptionCode2:
        code: Union[
            OneOfOptionCodeCodeOptionsDef1, OneOfOptionCodeCodeOptionsDef2
        ]
        hex: Union[
            OneOfOptionCodeHexOptionsDef1, OneOfOptionCodeHexOptionsDef2
        ]


    class OneOfOptionCodeIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfOptionCodeIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OptionCode3:
        code: Union[
            OneOfOptionCodeCodeOptionsDef1, OneOfOptionCodeCodeOptionsDef2
        ]
        ip: Union[
            OneOfOptionCodeIpOptionsDef1, OneOfOptionCodeIpOptionsDef2
        ]


    class Data:
        # Configure IPv4 prefix range of the DHCP address pool
        address_pool: AddressPool
        default_gateway: Optional[
            Union[
                OneOfDefaultGatewayOptionsDef1,
                OneOfDefaultGatewayOptionsDef2,
                OneOfDefaultGatewayOptionsDef3,
            ]
        ]
        dns_servers: Optional[
            Union[
                OneOfDnsServersOptionsDef1,
                OneOfDnsServersOptionsDef2,
                OneOfDnsServersOptionsDef3,
            ]
        ]
        domain_name: Optional[
            Union[
                OneOfDomainNameOptionsDef1,
                OneOfDomainNameOptionsDef2,
                OneOfDomainNameOptionsDef3,
            ]
        ]
        exclude: Optional[
            Union[
                OneOfExcludeOptionsDef1,
                OneOfExcludeOptionsDef2,
                OneOfExcludeOptionsDef3,
            ]
        ]
        interface_mtu: Optional[
            Union[
                OneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
                OneOfInterfaceMtuOptionsDef3,
            ]
        ]
        lease_time: Optional[
            Union[
                OneOfLeaseTimeOptionsDef1,
                OneOfLeaseTimeOptionsDef2,
                OneOfLeaseTimeOptionsDef3,
            ]
        ]
        # Configure Options Code
        option_code: Optional[
            List[Union[OptionCode1, OptionCode2, OptionCode3]]
        ]
        # Configure static IP addresses
        static_lease: Optional[List[StaticLease]]
        tftp_servers: Optional[
            Union[
                OneOfTftpServersOptionsDef1,
                OneOfTftpServersOptionsDef2,
                OneOfTftpServersOptionsDef3,
            ]
        ]


    class Payload:
        """
        LAN VPN DHCP Server profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransportGetResponse:
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
        # LAN VPN DHCP Server profile parcel schema for POST request
        payload: Optional[Payload]


    class DhcpServerOneOfExcludeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[Any, Any]]


    class DhcpServerOneOfLeaseTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class DhcpServerOneOfLeaseTimeOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class DhcpServerOneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class DhcpServerOneOfDomainNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class DhcpServerOneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class DhcpServerOneOfDnsServersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class DhcpServerOneOfTftpServersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class DhcpServerOneOfStaticLeaseMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class DhcpServerOneOfStaticLeaseIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class DhcpServerStaticLease:
        ip: Union[
            DhcpServerOneOfStaticLeaseIpOptionsDef1,
            OneOfStaticLeaseIpOptionsDef2,
        ]
        mac_address: Union[
            DhcpServerOneOfStaticLeaseMacAddressOptionsDef1,
            OneOfStaticLeaseMacAddressOptionsDef2,
        ]


    class DhcpServerOneOfOptionCodeCodeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class DhcpServerOneOfOptionCodeAsciiOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class DhcpServerOptionCode1:
        ascii: Union[
            DhcpServerOneOfOptionCodeAsciiOptionsDef1,
            OneOfOptionCodeAsciiOptionsDef2,
        ]
        code: Union[
            DhcpServerOneOfOptionCodeCodeOptionsDef1,
            OneOfOptionCodeCodeOptionsDef2,
        ]


    class IpsecDhcpServerOneOfOptionCodeCodeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class DhcpServerOneOfOptionCodeHexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class DhcpServerOptionCode2:
        code: Union[
            IpsecDhcpServerOneOfOptionCodeCodeOptionsDef1,
            OneOfOptionCodeCodeOptionsDef2,
        ]
        hex: Union[
            DhcpServerOneOfOptionCodeHexOptionsDef1,
            OneOfOptionCodeHexOptionsDef2,
        ]


    class InterfaceIpsecDhcpServerOneOfOptionCodeCodeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class DhcpServerOneOfOptionCodeIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class DhcpServerOptionCode3:
        code: Union[
            InterfaceIpsecDhcpServerOneOfOptionCodeCodeOptionsDef1,
            OneOfOptionCodeCodeOptionsDef2,
        ]
        ip: Union[
            DhcpServerOneOfOptionCodeIpOptionsDef1,
            OneOfOptionCodeIpOptionsDef2,
        ]


    class DhcpServerData:
        # Configure IPv4 prefix range of the DHCP address pool
        address_pool: AddressPool
        default_gateway: Optional[
            Union[
                DhcpServerOneOfDefaultGatewayOptionsDef1,
                OneOfDefaultGatewayOptionsDef2,
                OneOfDefaultGatewayOptionsDef3,
            ]
        ]
        dns_servers: Optional[
            Union[
                DhcpServerOneOfDnsServersOptionsDef1,
                OneOfDnsServersOptionsDef2,
                OneOfDnsServersOptionsDef3,
            ]
        ]
        domain_name: Optional[
            Union[
                DhcpServerOneOfDomainNameOptionsDef1,
                OneOfDomainNameOptionsDef2,
                OneOfDomainNameOptionsDef3,
            ]
        ]
        exclude: Optional[
            Union[
                DhcpServerOneOfExcludeOptionsDef1,
                OneOfExcludeOptionsDef2,
                OneOfExcludeOptionsDef3,
            ]
        ]
        interface_mtu: Optional[
            Union[
                DhcpServerOneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
                OneOfInterfaceMtuOptionsDef3,
            ]
        ]
        lease_time: Optional[
            Union[
                DhcpServerOneOfLeaseTimeOptionsDef1,
                OneOfLeaseTimeOptionsDef2,
                DhcpServerOneOfLeaseTimeOptionsDef3,
            ]
        ]
        # Configure Options Code
        option_code: Optional[
            List[
                Union[
                    DhcpServerOptionCode1,
                    DhcpServerOptionCode2,
                    DhcpServerOptionCode3,
                ]
            ]
        ]
        # Configure static IP addresses
        static_lease: Optional[List[DhcpServerStaticLease]]
        tftp_servers: Optional[
            Union[
                DhcpServerOneOfTftpServersOptionsDef1,
                OneOfTftpServersOptionsDef2,
                OneOfTftpServersOptionsDef3,
            ]
        ]


    class DhcpServerPayload:
        """
        LAN VPN DHCP Server profile parcel schema for PUT request
        """

        data: DhcpServerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceLanVpnInterfaceIpsecDhcpServerPayload:
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
        # LAN VPN DHCP Server profile parcel schema for PUT request
        payload: Optional[DhcpServerPayload]


    class EditLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


