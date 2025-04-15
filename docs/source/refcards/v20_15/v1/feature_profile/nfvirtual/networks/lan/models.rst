======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

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

    ModeDef = Literal["access", "trunk"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultModeDef = Literal["trunk"]

    LanModeDef = Literal["access", "trunk"]

    LanDefaultModeDef = Literal["trunk"]

    NetworksLanModeDef = Literal["access", "trunk"]

    NetworksLanDefaultModeDef = Literal["trunk"]


    class CreateNfvirtualLanParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpAddressOptionsDef2:
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
        value: ModeDef


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[DefaultModeDef]


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
        interface_name: Optional[
            Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        ]
        ip_address: Optional[
            Union[OneOfIpAddressOptionsDef1, OneOfIpAddressOptionsDef2]
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
        vlan: Optional[Union[OneOfVlanOptionsDef1, OneOfVlanOptionsDef2]]


    class CreateNfvirtualLanParcelPostRequest:
        """
        LAN profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class LanOneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanOneOfIpAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class LanOneOfNetworkNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanOneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LanModeDef


    class LanOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[LanDefaultModeDef]


    class LanOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanOneOfNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanData:
        bridge: Optional[
            Union[LanOneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2]
        ]
        interface_name: Optional[
            Union[LanOneOfPortOptionsDef1, OneOfPortOptionsDef2]
        ]
        ip_address: Optional[
            Union[LanOneOfIpAddressOptionsDef1, OneOfIpAddressOptionsDef2]
        ]
        mode: Optional[
            Union[
                LanOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                LanOneOfModeOptionsDef3,
            ]
        ]
        native_vlan: Optional[
            Union[
                LanOneOfNativeVlanOptionsDef1, OneOfNativeVlanOptionsDef2
            ]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        network_name: Optional[
            Union[
                LanOneOfNetworkNameOptionsDef1,
                OneOfNetworkNameOptionsDef2,
            ]
        ]
        vlan: Optional[
            Union[LanOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class Payload:
        """
        LAN profile parcel schema for PUT request
        """

        data: LanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksLanPayload:
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
        # LAN profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualLanParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class NetworksLanOneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksLanOneOfIpAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NetworksLanOneOfNetworkNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksLanOneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksLanOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: NetworksLanModeDef


    class NetworksLanOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[NetworksLanDefaultModeDef]


    class NetworksLanOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksLanOneOfNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class NetworksLanData:
        bridge: Optional[
            Union[
                NetworksLanOneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2
            ]
        ]
        interface_name: Optional[
            Union[NetworksLanOneOfPortOptionsDef1, OneOfPortOptionsDef2]
        ]
        ip_address: Optional[
            Union[
                NetworksLanOneOfIpAddressOptionsDef1,
                OneOfIpAddressOptionsDef2,
            ]
        ]
        mode: Optional[
            Union[
                NetworksLanOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                NetworksLanOneOfModeOptionsDef3,
            ]
        ]
        native_vlan: Optional[
            Union[
                NetworksLanOneOfNativeVlanOptionsDef1,
                OneOfNativeVlanOptionsDef2,
            ]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        network_name: Optional[
            Union[
                NetworksLanOneOfNetworkNameOptionsDef1,
                OneOfNetworkNameOptionsDef2,
            ]
        ]
        vlan: Optional[
            Union[NetworksLanOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class EditNfvirtualLanParcelPutRequest:
        """
        LAN profile parcel schema for PUT request
        """

        data: NetworksLanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


