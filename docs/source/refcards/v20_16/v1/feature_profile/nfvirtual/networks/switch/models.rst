======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    InterfacesInterfaceNameDef = Literal[
        "gigabitEthernet1/0",
        "gigabitEthernet1/1",
        "gigabitEthernet1/2",
        "gigabitEthernet1/3",
        "gigabitEthernet1/4",
        "gigabitEthernet1/5",
        "gigabitEthernet1/6",
        "gigabitEthernet1/7",
    ]

    VariableOptionTypeDef = Literal["variable"]

    InterfacesModeDef = Literal["access", "trunk"]

    SwitchInterfacesInterfaceNameDef = Literal[
        "gigabitEthernet1/0",
        "gigabitEthernet1/1",
        "gigabitEthernet1/2",
        "gigabitEthernet1/3",
        "gigabitEthernet1/4",
        "gigabitEthernet1/5",
        "gigabitEthernet1/6",
        "gigabitEthernet1/7",
    ]

    SwitchInterfacesModeDef = Literal["access", "trunk"]

    NetworksSwitchInterfacesInterfaceNameDef = Literal[
        "gigabitEthernet1/0",
        "gigabitEthernet1/1",
        "gigabitEthernet1/2",
        "gigabitEthernet1/3",
        "gigabitEthernet1/4",
        "gigabitEthernet1/5",
        "gigabitEthernet1/6",
        "gigabitEthernet1/7",
    ]

    NetworksSwitchInterfacesModeDef = Literal["access", "trunk"]


    class CreateNfvirtualSwitchParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfInterfacesInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfacesInterfaceNameDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfacesInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacesVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfacesVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacesModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfacesModeDef


    class OneOfInterfacesNativeVlanOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Interfaces:
        interface_name: Union[
            OneOfInterfacesInterfaceNameOptionsDef1,
            OneOfInterfacesInterfaceNameOptionsDef2,
        ]
        mode: Optional[OneOfInterfacesModeOptionsDef]
        native_vlan: Optional[OneOfInterfacesNativeVlanOptionsDef]
        vlan: Optional[
            Union[
                OneOfInterfacesVlanOptionsDef1,
                OneOfInterfacesVlanOptionsDef2,
            ]
        ]


    class Data:
        # List of Interfaces
        interfaces: Optional[List[Interfaces]]


    class CreateNfvirtualSwitchParcelPostRequest:
        """
        Switch profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SwitchOneOfInterfacesInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchInterfacesInterfaceNameDef  # pytype: disable=annotation-type-mismatch


    class SwitchOneOfInterfacesVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SwitchOneOfInterfacesModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SwitchInterfacesModeDef


    class SwitchOneOfInterfacesNativeVlanOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchInterfaces:
        interface_name: Union[
            SwitchOneOfInterfacesInterfaceNameOptionsDef1,
            OneOfInterfacesInterfaceNameOptionsDef2,
        ]
        mode: Optional[SwitchOneOfInterfacesModeOptionsDef]
        native_vlan: Optional[SwitchOneOfInterfacesNativeVlanOptionsDef]
        vlan: Optional[
            Union[
                SwitchOneOfInterfacesVlanOptionsDef1,
                OneOfInterfacesVlanOptionsDef2,
            ]
        ]


    class SwitchData:
        # List of Interfaces
        interfaces: Optional[List[SwitchInterfaces]]


    class Payload:
        """
        Switch profile parcel schema for PUT request
        """

        data: SwitchData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksSwitchPayload:
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
        # Switch profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualSwitchParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class NetworksSwitchOneOfInterfacesInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: NetworksSwitchInterfacesInterfaceNameDef  # pytype: disable=annotation-type-mismatch


    class NetworksSwitchOneOfInterfacesVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksSwitchOneOfInterfacesModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NetworksSwitchInterfacesModeDef


    class NetworksSwitchOneOfInterfacesNativeVlanOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class NetworksSwitchInterfaces:
        interface_name: Union[
            NetworksSwitchOneOfInterfacesInterfaceNameOptionsDef1,
            OneOfInterfacesInterfaceNameOptionsDef2,
        ]
        mode: Optional[NetworksSwitchOneOfInterfacesModeOptionsDef]
        native_vlan: Optional[
            NetworksSwitchOneOfInterfacesNativeVlanOptionsDef
        ]
        vlan: Optional[
            Union[
                NetworksSwitchOneOfInterfacesVlanOptionsDef1,
                OneOfInterfacesVlanOptionsDef2,
            ]
        ]


    class NetworksSwitchData:
        # List of Interfaces
        interfaces: Optional[List[NetworksSwitchInterfaces]]


    class EditNfvirtualSwitchParcelPutRequest:
        """
        Switch profile parcel schema for PUT request
        """

        data: NetworksSwitchData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


