======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    AddressFamilyRedistributeProtocolDef = Literal[
        "bgp", "connected", "ospf", "ospfv3", "static"
    ]

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

    TypeDef = Literal["hmac-sha-256", "md5"]


    class OneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAsNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfAddressFamilyRedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


    class Redistribute:
        protocol: Union[
            OneOfAddressFamilyRedistributeProtocolOptionsDef1,
            OneOfAddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


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


    class Ipv4AddressAndMaskDef:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class Network:
        prefix: Ipv4AddressAndMaskDef


    class AddressFamily:
        """
        Set EIGRP address family
        """

        # Configure the networks for EIGRP to advertise
        network: List[Network]
        # Redistribute routes into EIGRP
        redistribute: Optional[List[Redistribute]]


    class OneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class Type:
        value: Any


    class OneOfAuthKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAuthKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyKeyIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeyKeyIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyKeystringOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeyKeystringOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Key:
        key_id: Union[OneOfKeyKeyIdOptionsDef1, OneOfKeyKeyIdOptionsDef2]
        keystring: Union[
            OneOfKeyKeystringOptionsDef1, OneOfKeyKeystringOptionsDef2
        ]


    class Authentication1:
        auth_key: Union[OneOfAuthKeyOptionsDef1, OneOfAuthKeyOptionsDef2]
        type_: Type
        # Set keychain details
        key: Optional[List[Key]]


    class OneOfTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfTypeOptionsDef2:
        option_type: DefaultOptionTypeDef


    class Authentication2:
        type_: Union[OneOfTypeOptionsDef1, OneOfTypeOptionsDef2]
        auth_key: Optional[
            Union[OneOfAuthKeyOptionsDef1, OneOfAuthKeyOptionsDef2]
        ]
        # Set keychain details
        key: Optional[List[Key]]


    class OneOfAfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAfInterfaceNameOptionsDef2:
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


    class SummaryAddress:
        prefix: Ipv4AddressAndMaskDef


    class AfInterface:
        name: Union[
            OneOfAfInterfaceNameOptionsDef1,
            OneOfAfInterfaceNameOptionsDef2,
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        split_horizon: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        # Set summary addresses
        summary_address: Optional[List[SummaryAddress]]


    class TableMap:
        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class EigrpData:
        # Set EIGRP address family
        address_family: AddressFamily
        # Configure af-interface
        af_interface: List[AfInterface]
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        hello_interval: Union[
            OneOfHelloIntervalOptionsDef1,
            OneOfHelloIntervalOptionsDef2,
            OneOfHelloIntervalOptionsDef3,
        ]
        hold_time: Union[
            OneOfHoldTimeOptionsDef1,
            OneOfHoldTimeOptionsDef2,
            OneOfHoldTimeOptionsDef3,
        ]
        table_map: TableMap
        # Set EIGRP authentication detaile
        authentication: Optional[Union[Authentication1, Authentication2]]


    class Payload:
        """
        SD-Routing EIGRP feature schema
        """

        data: EigrpData
        name: str
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
        # SD-Routing EIGRP feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceVrfRoutingEigrpPayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceVrfEigrpFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class RoutingEigrpData:
        # Set EIGRP address family
        address_family: AddressFamily
        # Configure af-interface
        af_interface: List[AfInterface]
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        hello_interval: Union[
            OneOfHelloIntervalOptionsDef1,
            OneOfHelloIntervalOptionsDef2,
            OneOfHelloIntervalOptionsDef3,
        ]
        hold_time: Union[
            OneOfHoldTimeOptionsDef1,
            OneOfHoldTimeOptionsDef2,
            OneOfHoldTimeOptionsDef3,
        ]
        table_map: TableMap
        # Set EIGRP authentication detaile
        authentication: Optional[Union[Authentication1, Authentication2]]


    class CreateSdroutingServiceVrfEigrpFeaturePostRequest:
        """
        SD-Routing EIGRP feature schema
        """

        data: RoutingEigrpData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceVrfRoutingEigrpPayload:
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
        # SD-Routing EIGRP feature schema
        payload: Optional[Payload]


    class EditSdroutingServiceVrfEigrpFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class VrfRoutingEigrpData:
        # Set EIGRP address family
        address_family: AddressFamily
        # Configure af-interface
        af_interface: List[AfInterface]
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        hello_interval: Union[
            OneOfHelloIntervalOptionsDef1,
            OneOfHelloIntervalOptionsDef2,
            OneOfHelloIntervalOptionsDef3,
        ]
        hold_time: Union[
            OneOfHoldTimeOptionsDef1,
            OneOfHoldTimeOptionsDef2,
            OneOfHoldTimeOptionsDef3,
        ]
        table_map: TableMap
        # Set EIGRP authentication detaile
        authentication: Optional[Union[Authentication1, Authentication2]]


    class EditSdroutingServiceVrfEigrpFeaturePutRequest:
        """
        SD-Routing EIGRP feature schema
        """

        data: VrfRoutingEigrpData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetServiceVrfAssociatedRoutingEigrpFeaturesGetResponse:
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
        # SD-Routing EIGRP feature schema
        payload: Optional[Payload]


    class CreateServiceVrfAndRoutingEigrpFeatureAssociationPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateServiceVrfAndRoutingEigrpFeatureAssociationPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceVrfVrfRoutingEigrpPayload:
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
        # SD-Routing EIGRP feature schema
        payload: Optional[Payload]


    class EditServiceVrfAndRoutingEigrpFeatureAssociationPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditServiceVrfAndRoutingEigrpFeatureAssociationPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


