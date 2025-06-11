======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

    SharedLomTypeDef = Literal[
        "console", "failover", "ge1", "ge2", "ge3", "te2", "te3"
    ]

    SharedFailOverTypeDef = Literal["ge2", "te2"]

    VariableOptionTypeDef = Literal["variable"]


    class OneOfBayOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSlotOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfSharedLomOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            SharedLomTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSharedFailOverOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SharedFailOverTypeDef  # pytype: disable=annotation-type-mismatch


    class SharedLom:
        fail_over_type: Optional[OneOfSharedFailOverOptionsDef]
        lom_type: Optional[OneOfSharedLomOptionsDef]


    class AccessPort:
        dedicated: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        shared_lom: Optional[SharedLom]


    class OneOfIpv4PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDefaultGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfDefaultGatewayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDefaultGatewayOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Ip:
        address: Union[
            OneOfIpv4PrefixOptionsDef1, OneOfIpv4PrefixOptionsDef2
        ]
        default_gateway: Union[
            OneOfDefaultGatewayOptionsDef1,
            OneOfDefaultGatewayOptionsDef2,
            OneOfDefaultGatewayOptionsDef3,
        ]


    class OneOfVlanIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVlanIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVlanIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Vlan:
        priority: Optional[
            Union[
                OneOfPriorityOptionsDef1,
                OneOfPriorityOptionsDef2,
                OneOfPriorityOptionsDef3,
            ]
        ]
        vlan_id: Optional[
            Union[
                OneOfVlanIdOptionsDef1,
                OneOfVlanIdOptionsDef2,
                OneOfVlanIdOptionsDef3,
            ]
        ]


    class Imc:
        access_port: Optional[AccessPort]
        ip: Optional[Ip]
        vlan: Optional[Vlan]


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Onel3DefaultOptionsDef:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceUcseInterfaceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceUcseInterfaceVpnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceUcseInterfaceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Interface:
        if_name: Union[
            OneOfInterfaceNameOptionsDef1,
            OneOfInterfaceNameOptionsDef2,
            OneOfInterfaceNameOptionsDef3,
        ]
        address: Optional[
            Union[OneOfIpv4PrefixOptionsDef1, OneOfIpv4PrefixOptionsDef2]
        ]
        l3: Optional[Onel3DefaultOptionsDef]
        ucse_interface_vpn: Optional[
            Union[
                OneOfInterfaceUcseInterfaceVpnOptionsDef1,
                OneOfInterfaceUcseInterfaceVpnOptionsDef2,
                OneOfInterfaceUcseInterfaceVpnOptionsDef3,
            ]
        ]


    class UcseData:
        bay: OneOfBayOptionsDef
        slot: OneOfSlotOptionsDef
        imc: Optional[Imc]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[Interface]]


    class Payload:
        """
        ucse profile feature schema for  request
        """

        data: UcseData
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
        # ucse profile feature schema for  request
        payload: Optional[Payload]


    class GetListSdwanOtherUcsePayload:
        data: Optional[List[Data]]


    class CreateUcseProfileFeatureForOtherPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OtherUcseData:
        bay: OneOfBayOptionsDef
        slot: OneOfSlotOptionsDef
        imc: Optional[Imc]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[Interface]]


    class CreateUcseProfileFeatureForOtherPostRequest:
        """
        ucse profile feature schema for  request
        """

        data: OtherUcseData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanOtherUcsePayload:
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
        # ucse profile feature schema for  request
        payload: Optional[Payload]


    class EditUcseProfileFeatureForOtherPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanOtherUcseData:
        bay: OneOfBayOptionsDef
        slot: OneOfSlotOptionsDef
        imc: Optional[Imc]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[Interface]]


    class EditUcseProfileFeatureForOtherPutRequest:
        """
        ucse profile feature schema for  request
        """

        data: SdwanOtherUcseData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


