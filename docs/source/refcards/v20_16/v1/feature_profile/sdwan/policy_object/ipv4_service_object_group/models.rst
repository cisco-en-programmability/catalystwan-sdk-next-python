======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class Entries1:
        object_group: ParcelReferenceDef


    class Protocol:
        value: Optional[Any]


    class OneOfEntriesOperatorLtOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesPortLtValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesPortLtValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourcePorts1:
        lt_value: Union[
            OneOfEntriesPortLtValueOptionsDef1,
            OneOfEntriesPortLtValueOptionsDef2,
        ]
        operator: OneOfEntriesOperatorLtOptionsDef


    class OneOfEntriesOperatorEqOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesTcpPortEqValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfEntriesTcpPortEqValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class EqValue1:
        tcp_eq_value: Union[
            OneOfEntriesTcpPortEqValueOptionsDef1,
            OneOfEntriesTcpPortEqValueOptionsDef2,
        ]


    class OneOfEntriesUdpPortEqValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfEntriesUdpPortEqValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class EqValue2:
        udp_eq_value: Union[
            OneOfEntriesUdpPortEqValueOptionsDef1,
            OneOfEntriesUdpPortEqValueOptionsDef2,
        ]


    class OneOfEntriesTcpUdpPortEqValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfEntriesTcpUdpPortEqValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class EqValue3:
        tcp_udp_eq_value: Union[
            OneOfEntriesTcpUdpPortEqValueOptionsDef1,
            OneOfEntriesTcpUdpPortEqValueOptionsDef2,
        ]


    class SourcePorts2:
        # Source Port That is Equal to This Value
        eq_value: Union[EqValue1, EqValue2, EqValue3]
        operator: OneOfEntriesOperatorEqOptionsDef


    class OneOfEntriesOperatorGtOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesPortGtValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesPortGtValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourcePorts3:
        gt_value: Union[
            OneOfEntriesPortGtValueOptionsDef1,
            OneOfEntriesPortGtValueOptionsDef2,
        ]
        operator: OneOfEntriesOperatorGtOptionsDef


    class OneOfEntriesOperatorRangeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesPortRangeStartOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesPortRangeStartOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEntriesPortRangeEndOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesPortRangeEndOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Range:
        """
        Source Port Range
        """

        end: Union[
            OneOfEntriesPortRangeEndOptionsDef1,
            OneOfEntriesPortRangeEndOptionsDef2,
        ]
        start: Union[
            OneOfEntriesPortRangeStartOptionsDef1,
            OneOfEntriesPortRangeStartOptionsDef2,
        ]


    class SourcePorts4:
        operator: OneOfEntriesOperatorRangeOptionsDef
        # Source Port Range
        range: Range


    class DestinationPorts:
        eq_value: Optional[Any]


    class OneOfEntriesIcmpMsgOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfEntriesIcmpMsgOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Entries21:
        protocol: Protocol
        destination_ports: Optional[DestinationPorts]
        icmp_msg: Optional[
            Union[
                OneOfEntriesIcmpMsgOptionsDef1,
                OneOfEntriesIcmpMsgOptionsDef2,
            ]
        ]
        # Source Ports
        source_ports: Optional[
            Union[SourcePorts1, SourcePorts2, SourcePorts3, SourcePorts4]
        ]


    class OneOfEntriesProtocolOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class DestinationPorts1:
        lt_value: Union[
            OneOfEntriesPortLtValueOptionsDef1,
            OneOfEntriesPortLtValueOptionsDef2,
        ]
        operator: OneOfEntriesOperatorLtOptionsDef


    class DestinationPorts2:
        # Destination Port That is Equal to This Value
        eq_value: Union[EqValue1, EqValue2, EqValue3]
        operator: OneOfEntriesOperatorEqOptionsDef


    class DestinationPorts3:
        gt_value: Union[
            OneOfEntriesPortGtValueOptionsDef1,
            OneOfEntriesPortGtValueOptionsDef2,
        ]
        operator: OneOfEntriesOperatorGtOptionsDef


    class Ipv4ServiceObjectGroupRange:
        """
        Destination Port Range
        """

        end: Union[
            OneOfEntriesPortRangeEndOptionsDef1,
            OneOfEntriesPortRangeEndOptionsDef2,
        ]
        start: Union[
            OneOfEntriesPortRangeStartOptionsDef1,
            OneOfEntriesPortRangeStartOptionsDef2,
        ]


    class DestinationPorts4:
        operator: OneOfEntriesOperatorRangeOptionsDef
        # Destination Port Range
        range: Ipv4ServiceObjectGroupRange


    class Entries22:
        protocol: OneOfEntriesProtocolOptionsDef
        # Destination Ports
        destination_ports: Optional[
            Union[
                DestinationPorts1,
                DestinationPorts2,
                DestinationPorts3,
                DestinationPorts4,
            ]
        ]
        icmp_msg: Optional[
            Union[
                OneOfEntriesIcmpMsgOptionsDef1,
                OneOfEntriesIcmpMsgOptionsDef2,
            ]
        ]
        # Source Ports
        source_ports: Optional[
            Union[SourcePorts1, SourcePorts2, SourcePorts3, SourcePorts4]
        ]


    class Data:
        # object-group Entries
        entries: List[Union[Entries1, Union[Entries21, Entries22]]]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Ipv4 Service Object Group profile parcel schema
        payload: Optional[Payload]


