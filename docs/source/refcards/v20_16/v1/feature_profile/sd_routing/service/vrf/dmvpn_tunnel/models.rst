======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

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

    ModeTypeDef = Literal["ipv4", "ipv6"]


    class OneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfVpnNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVpnNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVpnNameOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Overlay:
        """
        overlay Attributes
        """

        ipv4_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        ipv6_prefix: Optional[
            Union[
                OneOfIpv6PrefixGlobalVariableWithoutDefault1,
                OneOfIpv6PrefixGlobalVariableWithoutDefault2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]


    class OneOfTunnelKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTunnelKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfModeTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ModeTypeDef


    class OneOfInterfaceNameV2OptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameV2OptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class TunnelVrf1:
        vrf: Union[
            OneOfVrfOptionsWithoutDefault1, OneOfVrfOptionsWithoutDefault2
        ]


    class BooleanDefaultTrueOptionsDef:
        option_type: DefaultOptionTypeDef
        value: bool


    class TunnelVrf2:
        global_vrf: BooleanDefaultTrueOptionsDef


    class Underlay:
        """
        BFD Attributes
        """

        tunnel_source: Union[
            OneOfInterfaceNameV2OptionsNoDefaultDef1,
            OneOfInterfaceNameV2OptionsNoDefaultDef2,
        ]
        type_: OneOfModeTypeOptionsDef
        tunnel_vrf: Optional[Union[TunnelVrf1, TunnelVrf2]]


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRefIdOptionsWithDefault1:
        ref_id: RefId


    class OneOfRefIdOptionsWithDefault2:
        option_type: DefaultOptionTypeDef


    class TunnelAttribute:
        """
        DMVPN tunnel basic Attributes
        """

        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        ipsec_profile: Union[
            OneOfRefIdOptionsWithDefault1, OneOfRefIdOptionsWithDefault2
        ]
        # overlay Attributes
        overlay: Overlay
        tunnel_key: Union[
            OneOfTunnelKeyOptionsDef1,
            OneOfTunnelKeyOptionsDef2,
            OneOfTunnelKeyOptionsDef3,
        ]
        # BFD Attributes
        underlay: Underlay
        description: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class OneOfNetworkIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNetworkIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHoldTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHoldTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfKeyAuthKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeyAuthKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyAuthKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpv4PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class NhrpSummaryMap:
        ipv4_prefix: Union[
            OneOfIpv4PrefixOptionsDef1, OneOfIpv4PrefixOptionsDef2
        ]


    class Ipv4:
        """
        ipv4 Attributes
        """

        # IPv4 NHS summary Map
        nhrp_summary_map: Optional[List[NhrpSummaryMap]]


    class DmvpnTunnelNhrpSummaryMap:
        ipv6_prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class Ipv6:
        """
        ipv6 Attributes
        """

        # IPv6 NHS summary Map
        nhrp_summary_map: Optional[List[DmvpnTunnelNhrpSummaryMap]]


    class Common:
        """
        common Attributes
        """

        network_id: Union[
            OneOfNetworkIdOptionsDef1, OneOfNetworkIdOptionsDef2
        ]
        auth_key: Optional[
            Union[
                OneOfKeyAuthKeyOptionsDef1,
                OneOfKeyAuthKeyOptionsDef2,
                OneOfKeyAuthKeyOptionsDef3,
            ]
        ]
        hold_time: Optional[
            Union[
                OneOfHoldTimeOptionsDef1,
                OneOfHoldTimeOptionsDef2,
                OneOfHoldTimeOptionsDef3,
            ]
        ]
        # ipv4 Attributes
        ipv4: Optional[Ipv4]
        # ipv6 Attributes
        ipv6: Optional[Ipv6]


    class OneOfOnBooleanDefaultTrueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultTrueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Hub:
        """
        hub Attributes
        """

        redirect: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]


    class NbmaMap:
        nbma_ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        nhs_ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        multicast: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]


    class DmvpnTunnelIpv4:
        """
        ipv4 Attributes
        """

        # IPv4 NHS NBMA Map
        nbma_map: Optional[List[NbmaMap]]


    class OneOfIpv6AddrGlobalVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddrGlobalVariableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class DmvpnTunnelNbmaMap:
        nbma_ip_address: Union[
            OneOfIpAddressOptionsDef1, OneOfIpAddressOptionsDef2
        ]
        nhs_ip_address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        multicast: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]


    class DmvpnTunnelIpv6:
        """
        ipv6 Attributes
        """

        # IPv6 NHS NBMA Map
        nbma_map: Optional[List[DmvpnTunnelNbmaMap]]


    class Spoke:
        """
        spoke Attributes
        """

        # ipv4 Attributes
        ipv4: Optional[DmvpnTunnelIpv4]
        # ipv6 Attributes
        ipv6: Optional[DmvpnTunnelIpv6]
        shortcut: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]


    class Nhrp:
        """
        NHRP
        """

        # common Attributes
        common: Common
        # hub Attributes
        hub: Optional[Hub]
        # spoke Attributes
        spoke: Optional[Spoke]


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfTransmitIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTransmitIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTransmitIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfReceiveIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfReceiveIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfReceiveIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMultiplierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Bfd:
        """
        BFD Attributes
        """

        enable: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        multiplier: Optional[
            Union[
                OneOfMultiplierOptionsDef1,
                OneOfMultiplierOptionsDef2,
                OneOfMultiplierOptionsDef3,
            ]
        ]
        receive_interval: Optional[
            Union[
                OneOfReceiveIntervalOptionsDef1,
                OneOfReceiveIntervalOptionsDef2,
                OneOfReceiveIntervalOptionsDef3,
            ]
        ]
        transmit_interval: Optional[
            Union[
                OneOfTransmitIntervalOptionsDef1,
                OneOfTransmitIntervalOptionsDef2,
                OneOfTransmitIntervalOptionsDef3,
            ]
        ]


    class OneOfIpv4MtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4MtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4MtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv6MtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6MtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6MtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv4TcpMssMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4TcpMssMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4TcpMssMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv6TcpMssMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6TcpMssMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6TcpMssMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDelayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDelayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDelayOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfBandwidthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Advanced:
        """
        DMVPN tunnel advance Attributes
        """

        bandwidth: Optional[
            Union[
                OneOfBandwidthOptionsDef1,
                OneOfBandwidthOptionsDef2,
                OneOfBandwidthOptionsDef3,
            ]
        ]
        delay: Optional[
            Union[
                OneOfDelayOptionsDef1,
                OneOfDelayOptionsDef2,
                OneOfDelayOptionsDef3,
            ]
        ]
        ipv4_mtu: Optional[
            Union[
                OneOfIpv4MtuOptionsDef1,
                OneOfIpv4MtuOptionsDef2,
                OneOfIpv4MtuOptionsDef3,
            ]
        ]
        ipv4_tcp_mss: Optional[
            Union[
                OneOfIpv4TcpMssMtuOptionsDef1,
                OneOfIpv4TcpMssMtuOptionsDef2,
                OneOfIpv4TcpMssMtuOptionsDef3,
            ]
        ]
        ipv6_mtu: Optional[
            Union[
                OneOfIpv6MtuOptionsDef1,
                OneOfIpv6MtuOptionsDef2,
                OneOfIpv6MtuOptionsDef3,
            ]
        ]
        ipv6_tcp_mss: Optional[
            Union[
                OneOfIpv6TcpMssMtuOptionsDef1,
                OneOfIpv6TcpMssMtuOptionsDef2,
                OneOfIpv6TcpMssMtuOptionsDef3,
            ]
        ]


    class DmvpnTunnelData:
        # NHRP
        nhrp: Nhrp
        # DMVPN tunnel basic Attributes
        tunnel_attribute: TunnelAttribute
        # DMVPN tunnel advance Attributes
        advanced: Optional[Advanced]
        # BFD Attributes
        bfd: Optional[Bfd]


    class Payload:
        """
        SD-Routing DMVPN tunnel feature schema
        """

        data: DmvpnTunnelData
        name: str
        # Set the feature description
        description: Optional[str]
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
        # SD-Routing DMVPN tunnel feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceVrfLanDmvpnTunnelPayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceVrfDmvpnTunnelFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class VrfDmvpnTunnelData:
        # NHRP
        nhrp: Nhrp
        # DMVPN tunnel basic Attributes
        tunnel_attribute: TunnelAttribute
        # DMVPN tunnel advance Attributes
        advanced: Optional[Advanced]
        # BFD Attributes
        bfd: Optional[Bfd]


    class CreateSdroutingServiceVrfDmvpnTunnelFeaturePostRequest:
        """
        SD-Routing DMVPN tunnel feature schema
        """

        data: VrfDmvpnTunnelData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceVrfLanDmvpnTunnelPayload:
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
        # SD-Routing DMVPN tunnel feature schema
        payload: Optional[Payload]


    class EditSdroutingServiceVrfDmvpnTunnelFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ServiceVrfDmvpnTunnelData:
        # NHRP
        nhrp: Nhrp
        # DMVPN tunnel basic Attributes
        tunnel_attribute: TunnelAttribute
        # DMVPN tunnel advance Attributes
        advanced: Optional[Advanced]
        # BFD Attributes
        bfd: Optional[Bfd]


    class EditSdroutingServiceVrfDmvpnTunnelFeaturePutRequest:
        """
        SD-Routing DMVPN tunnel feature schema
        """

        data: ServiceVrfDmvpnTunnelData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


