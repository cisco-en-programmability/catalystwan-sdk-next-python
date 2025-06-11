======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    AddressFamilyRedistributeProtocolDef = Literal[
        "bgp", "connected", "nat-route", "omp", "ospf", "ospfv3", "static"
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

    BooleanFalseDef = Literal[False]


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


    class OneOfTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAuthKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAuthKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfKeyKeyIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeyKeyIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyKeyIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfKeyKeystringOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeyKeystringOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyKeystringOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Key:
        key_id: Union[
            OneOfKeyKeyIdOptionsDef1,
            OneOfKeyKeyIdOptionsDef2,
            OneOfKeyKeyIdOptionsDef3,
        ]
        keystring: Union[
            OneOfKeyKeystringOptionsDef1,
            OneOfKeyKeystringOptionsDef2,
            OneOfKeyKeystringOptionsDef3,
        ]


    class Authentication:
        """
        Set EIGRP authentication detaile
        """

        type_: Union[
            OneOfTypeOptionsDef1,
            OneOfTypeOptionsDef2,
            OneOfTypeOptionsDef3,
        ]
        auth_key: Optional[
            Union[
                OneOfAuthKeyOptionsDef1,
                OneOfAuthKeyOptionsDef2,
                OneOfAuthKeyOptionsDef3,
            ]
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


    class OneOfAfInterfaceShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAfInterfaceShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAfInterfaceShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class SummaryAddress:
        prefix: Ipv4AddressAndMaskDef


    class AfInterface:
        name: Union[
            OneOfAfInterfaceNameOptionsDef1,
            OneOfAfInterfaceNameOptionsDef2,
        ]
        shutdown: Optional[
            Union[
                OneOfAfInterfaceShutdownOptionsDef1,
                OneOfAfInterfaceShutdownOptionsDef2,
                OneOfAfInterfaceShutdownOptionsDef3,
            ]
        ]
        # Set summary addresses
        summary_address: Optional[List[SummaryAddress]]


    class OneOfFilterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfFilterOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfFilterOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class TableMap:
        filter: Optional[
            Union[
                OneOfFilterOptionsDef1,
                OneOfFilterOptionsDef2,
                OneOfFilterOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class Data:
        # Set EIGRP address family
        address_family: AddressFamily
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
        # Configure IPv4 Static Routes
        af_interface: Optional[List[AfInterface]]
        # Set EIGRP authentication detaile
        authentication: Optional[Authentication]


    class Payload:
        """
        EIGRP profile feature schema
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetLanVpnAssociatedRoutingEigrpParcelsForServiceGetResponse:
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
        # EIGRP profile feature schema
        payload: Optional[Payload]


    class CreateLanVpnAndRoutingEigrpParcelAssociationForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnAndRoutingEigrpParcelAssociationForServicePostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GetSingleSdwanServiceLanVpnRoutingEigrpPayload:
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
        # EIGRP profile feature schema
        payload: Optional[Payload]


    class EditLanVpnAndRoutingEigrpParcelAssociationForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditLanVpnAndRoutingEigrpParcelAssociationForServicePutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


