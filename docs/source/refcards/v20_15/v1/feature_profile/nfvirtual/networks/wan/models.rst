======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    ColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    VariableOptionTypeDef = Literal["variable"]

    ModeDef = Literal["access", "trunk"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultModeDef = Literal["trunk"]

    BooleanFalseDef = Literal[False]

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

    TypeDef = Literal["none", "primary", "secondary(1)"]

    WanColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    WanModeDef = Literal["access", "trunk"]

    WanDefaultModeDef = Literal["trunk"]

    WanTypeDef = Literal["none", "primary", "secondary(1)"]

    NetworksWanColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    NetworksWanModeDef = Literal["access", "trunk"]

    NetworksWanDefaultModeDef = Literal["trunk"]

    NetworksWanTypeDef = Literal["none", "primary", "secondary(1)"]


    class CreateNfvirtualWanParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfColorOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfWanInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfWanInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNetworkNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNetworkNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBridgeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[DefaultModeDef]


    class OneOfDhcpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDhcpOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Optional[BooleanFalseDef]


    class OneOfIpv4AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpv4AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNetmaskOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfNetmaskOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Optional[BooleanFalseDef]


    class OneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfDefaultGatewayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNativeVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data:
        bridge: Optional[
            Union[OneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2]
        ]
        color: Optional[
            Union[OneOfColorOptionsDef1, OneOfColorOptionsDef2]
        ]
        default_gateway: Optional[
            Union[
                OneOfDefaultGatewayOptionsDef1,
                OneOfDefaultGatewayOptionsDef2,
            ]
        ]
        dhcp: Optional[Union[OneOfDhcpOptionsDef1, OneOfDhcpOptionsDef2]]
        interface_name: Optional[
            Union[
                OneOfWanInterfaceNameOptionsDef1,
                OneOfWanInterfaceNameOptionsDef2,
            ]
        ]
        ip_address: Optional[
            Union[
                OneOfIpv4AddressOptionsDef1, OneOfIpv4AddressOptionsDef2
            ]
        ]
        mode: Optional[
            Union[
                OneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                OneOfModeOptionsDef3,
            ]
        ]
        native_vlan: Optional[
            Union[OneOfNativeVlanOptionsDef1, OneOfNativeVlanOptionsDef2]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        network_name: Optional[
            Union[
                OneOfNetworkNameOptionsDef1, OneOfNetworkNameOptionsDef2
            ]
        ]
        shutdown: Optional[
            Union[OneOfShutdownOptionsDef1, OneOfShutdownOptionsDef2]
        ]
        type_: Optional[OneOfTypeOptionsDef]
        vlan: Optional[Union[OneOfVlanOptionsDef1, OneOfVlanOptionsDef2]]


    class CreateNfvirtualWanParcelPostRequest:
        """
        WAN  profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class WanOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WanColorDef  # pytype: disable=annotation-type-mismatch


    class WanOneOfWanInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WanOneOfNetworkNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WanOneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WanOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WanModeDef  # pytype: disable=annotation-type-mismatch


    class WanOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[WanDefaultModeDef]


    class WanOneOfIpv4AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class WanOneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class WanOneOfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: WanTypeDef  # pytype: disable=annotation-type-mismatch


    class WanOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WanOneOfNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanData:
        bridge: Optional[
            Union[WanOneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2]
        ]
        color: Optional[
            Union[WanOneOfColorOptionsDef1, OneOfColorOptionsDef2]
        ]
        default_gateway: Optional[
            Union[
                WanOneOfDefaultGatewayOptionsDef1,
                OneOfDefaultGatewayOptionsDef2,
            ]
        ]
        dhcp: Optional[Union[OneOfDhcpOptionsDef1, OneOfDhcpOptionsDef2]]
        interface_name: Optional[
            Union[
                WanOneOfWanInterfaceNameOptionsDef1,
                OneOfWanInterfaceNameOptionsDef2,
            ]
        ]
        ip_address: Optional[
            Union[
                WanOneOfIpv4AddressOptionsDef1,
                OneOfIpv4AddressOptionsDef2,
            ]
        ]
        mode: Optional[
            Union[
                WanOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                WanOneOfModeOptionsDef3,
            ]
        ]
        native_vlan: Optional[
            Union[
                WanOneOfNativeVlanOptionsDef1, OneOfNativeVlanOptionsDef2
            ]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        network_name: Optional[
            Union[
                WanOneOfNetworkNameOptionsDef1,
                OneOfNetworkNameOptionsDef2,
            ]
        ]
        shutdown: Optional[
            Union[OneOfShutdownOptionsDef1, OneOfShutdownOptionsDef2]
        ]
        type_: Optional[WanOneOfTypeOptionsDef]
        vlan: Optional[
            Union[WanOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class Payload:
        """
        WAN  profile parcel schema for PUT request
        """

        data: WanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksWanPayload:
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
        # WAN  profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualWanParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class NetworksWanOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: NetworksWanColorDef  # pytype: disable=annotation-type-mismatch


    class NetworksWanOneOfWanInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksWanOneOfNetworkNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksWanOneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksWanOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            NetworksWanModeDef  # pytype: disable=annotation-type-mismatch
        )


    class NetworksWanOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[NetworksWanDefaultModeDef]


    class NetworksWanOneOfIpv4AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NetworksWanOneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NetworksWanOneOfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            NetworksWanTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class NetworksWanOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksWanOneOfNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class NetworksWanData:
        bridge: Optional[
            Union[
                NetworksWanOneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2
            ]
        ]
        color: Optional[
            Union[NetworksWanOneOfColorOptionsDef1, OneOfColorOptionsDef2]
        ]
        default_gateway: Optional[
            Union[
                NetworksWanOneOfDefaultGatewayOptionsDef1,
                OneOfDefaultGatewayOptionsDef2,
            ]
        ]
        dhcp: Optional[Union[OneOfDhcpOptionsDef1, OneOfDhcpOptionsDef2]]
        interface_name: Optional[
            Union[
                NetworksWanOneOfWanInterfaceNameOptionsDef1,
                OneOfWanInterfaceNameOptionsDef2,
            ]
        ]
        ip_address: Optional[
            Union[
                NetworksWanOneOfIpv4AddressOptionsDef1,
                OneOfIpv4AddressOptionsDef2,
            ]
        ]
        mode: Optional[
            Union[
                NetworksWanOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                NetworksWanOneOfModeOptionsDef3,
            ]
        ]
        native_vlan: Optional[
            Union[
                NetworksWanOneOfNativeVlanOptionsDef1,
                OneOfNativeVlanOptionsDef2,
            ]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        network_name: Optional[
            Union[
                NetworksWanOneOfNetworkNameOptionsDef1,
                OneOfNetworkNameOptionsDef2,
            ]
        ]
        shutdown: Optional[
            Union[OneOfShutdownOptionsDef1, OneOfShutdownOptionsDef2]
        ]
        type_: Optional[NetworksWanOneOfTypeOptionsDef]
        vlan: Optional[
            Union[NetworksWanOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class EditNfvirtualWanParcelPutRequest:
        """
        WAN  profile parcel schema for PUT request
        """

        data: NetworksWanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


