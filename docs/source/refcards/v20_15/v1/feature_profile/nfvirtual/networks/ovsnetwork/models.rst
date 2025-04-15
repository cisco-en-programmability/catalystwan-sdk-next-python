======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    ModeDef = Literal["access", "trunk"]

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

    OvsnetworkModeDef = Literal["access", "trunk"]


    class OneOfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
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


    class OneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNativeLanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNativeLanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfAddressOptionsDef2:
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


    class OneOfDhcpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDhcpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfGatewayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data:
        network_name: Union[OneOfNameOptionsDef1, OneOfNameOptionsDef2]
        bridge: Optional[
            Union[OneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2]
        ]
        dhcp: Optional[Union[OneOfDhcpOptionsDef1, OneOfDhcpOptionsDef2]]
        gateway: Optional[
            Union[OneOfGatewayOptionsDef1, OneOfGatewayOptionsDef2]
        ]
        interface_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
            ]
        ]
        ip_address: Optional[
            Union[OneOfAddressOptionsDef1, OneOfAddressOptionsDef2]
        ]
        mode: Optional[Union[OneOfModeOptionsDef1, OneOfModeOptionsDef2]]
        native_vlan: Optional[
            Union[OneOfNativeLanOptionsDef1, OneOfNativeLanOptionsDef2]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        vlan: Optional[Union[OneOfVlanOptionsDef1, OneOfVlanOptionsDef2]]


    class Payload:
        """
        Network profile parcel schema for PUT request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksOvsnetworkPayload:
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
        # Network profile parcel schema for PUT request
        payload: Optional[Payload]


    class CreateNfvirtualOvsNetworkParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OvsnetworkOneOfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OvsnetworkOneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OvsnetworkOneOfBridgeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OvsnetworkOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            OvsnetworkModeDef  # pytype: disable=annotation-type-mismatch
        )


    class OvsnetworkOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OvsnetworkOneOfNativeLanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OvsnetworkOneOfAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OvsnetworkOneOfGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OvsnetworkData:
        network_name: Union[
            OvsnetworkOneOfNameOptionsDef1, OneOfNameOptionsDef2
        ]
        bridge: Optional[
            Union[
                OvsnetworkOneOfBridgeOptionsDef1, OneOfBridgeOptionsDef2
            ]
        ]
        dhcp: Optional[Union[OneOfDhcpOptionsDef1, OneOfDhcpOptionsDef2]]
        gateway: Optional[
            Union[
                OvsnetworkOneOfGatewayOptionsDef1, OneOfGatewayOptionsDef2
            ]
        ]
        interface_name: Optional[
            Union[
                OvsnetworkOneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
            ]
        ]
        ip_address: Optional[
            Union[
                OvsnetworkOneOfAddressOptionsDef1, OneOfAddressOptionsDef2
            ]
        ]
        mode: Optional[
            Union[OvsnetworkOneOfModeOptionsDef1, OneOfModeOptionsDef2]
        ]
        native_vlan: Optional[
            Union[
                OvsnetworkOneOfNativeLanOptionsDef1,
                OneOfNativeLanOptionsDef2,
            ]
        ]
        netmask: Optional[
            Union[OneOfNetmaskOptionsDef1, OneOfNetmaskOptionsDef2]
        ]
        vlan: Optional[
            Union[OvsnetworkOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class CreateNfvirtualOvsNetworkParcelPostRequest:
        """
        Network profile parcel schema for POST request
        """

        data: OvsnetworkData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class EditNfvirtualOvsNetworkParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditNfvirtualOvsNetworkParcelPutRequest:
        """
        Network profile parcel schema for PUT request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


