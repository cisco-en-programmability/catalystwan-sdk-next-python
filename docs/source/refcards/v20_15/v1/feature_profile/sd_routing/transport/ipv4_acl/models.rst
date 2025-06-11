======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    AclTypeDef = Literal["extended", "standard"]

    DefaultActionDef = Literal["accept", "drop"]

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["drop"]

    VariableOptionTypeDef = Literal["variable"]

    SequencesActionTypeDef = Literal["accept", "drop"]

    Ipv4AclValue = Literal["accept"]

    BooleanTrueDef = Literal[True]

    SequencesMatchEntriesTcpPortEqAppNamesDef = Literal[
        "bgp",
        "chargen",
        "cmd",
        "daytime",
        "discard",
        "domain",
        "echo",
        "exec",
        "finger",
        "ftp",
        "ftp-data",
        "gopher",
        "hostname",
        "ident",
        "irc",
        "klogin",
        "kshell",
        "login",
        "lpd",
        "msrpc",
        "nntp",
        "onep-plain",
        "onep-tls",
        "pim-auto-rp",
        "pop2",
        "pop3",
        "smtp",
        "sunrpc",
        "syslog",
        "tacacs",
        "talk",
        "telnet",
        "time",
        "uucp",
        "whois",
        "www",
    ]

    SequencesMatchEntriesUdpPortEqAppNamesDef = Literal[
        "biff",
        "bootpc",
        "bootps",
        "discard",
        "dnsix",
        "domain",
        "echo",
        "isakmp",
        "mobile-ip",
        "nameserver",
        "netbios-dgm",
        "netbios-ns",
        "netbios-ss",
        "non500-isakmp",
        "ntp",
        "pim-auto-rp",
        "rip",
        "ripv6",
        "snmp",
        "snmptrap",
        "sunrpc",
        "syslog",
        "tacacs",
        "talk",
        "tftp",
        "time",
        "who",
        "xdmcp",
    ]

    SequencesMatchEntriesPortOperatorDef = Literal[
        "eq", "gt", "lt", "range"
    ]

    SequencesMatchEntriesTcpBitDef = Literal[
        "ack", "fin", "psh", "rst", "syn", "urg"
    ]


    class OneOfAclTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AclTypeDef


    class OneOfDefaultActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: DefaultActionDef


    class OneOfDefaultActionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesMatchEntriesSourceTypeHostOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesSourceHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesSourceHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourceAddress1:
        source_host: Union[
            OneOfSequencesMatchEntriesSourceHostOptionsDef1,
            OneOfSequencesMatchEntriesSourceHostOptionsDef2,
        ]
        source_type: OneOfSequencesMatchEntriesSourceTypeHostOptionsDef


    class OneOfSequencesMatchEntriesSourceTypeIpPrefixOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourceAddress2:
        source_ip_prefix: Union[
            OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef1,
            OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef2,
        ]
        source_type: (
            OneOfSequencesMatchEntriesSourceTypeIpPrefixOptionsDef
        )


    class MatchEntries:
        """
        Define match conditions
        """

        # Source Address
        source_address: Union[SourceAddress1, SourceAddress2]


    class OneOfSequencesActionTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SequencesActionTypeDef


    class OneOfSequencesActionTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Ipv4AclValue  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesActionsLogOptionsDef:
        option_type: GlobalOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class Actions:
        """
        Actions
        """

        log: OneOfSequencesActionsLogOptionsDef


    class StandardAclSequences:
        action_type: Union[
            OneOfSequencesActionTypeOptionsDef1,
            OneOfSequencesActionTypeOptionsDef2,
        ]
        sequence_name: OneOfSequencesSequenceNameOptionsDef
        # Actions
        actions: Optional[Actions]
        # Define match conditions
        match_entries: Optional[MatchEntries]


    class Protocol:
        value: Optional[Any]


    class OneOfSequencesMatchEntriesSourceAddressOptionsDef1:
        source_host: Union[
            OneOfSequencesMatchEntriesSourceHostOptionsDef1,
            OneOfSequencesMatchEntriesSourceHostOptionsDef2,
        ]
        source_type: OneOfSequencesMatchEntriesSourceTypeHostOptionsDef


    class OneOfSequencesMatchEntriesSourceAddressOptionsDef2:
        source_ip_prefix: Union[
            OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef1,
            OneOfSequencesMatchEntriesSourceIpPrefixOptionsDef2,
        ]
        source_type: (
            OneOfSequencesMatchEntriesSourceTypeIpPrefixOptionsDef
        )


    class Operator:
        value: Optional[Any]


    class OneOfSequencesMatchEntriesPortLtValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesMatchEntriesPortLtValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesPortGtValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesMatchEntriesPortGtValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesPortEqNumbersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfSequencesMatchEntriesPortEqNumbersOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            SequencesMatchEntriesTcpPortEqAppNamesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class TcpEqValue1:
        port_numbers: Union[
            OneOfSequencesMatchEntriesPortEqNumbersOptionsDef1,
            OneOfSequencesMatchEntriesPortEqNumbersOptionsDef2,
        ]
        app_names: Optional[
            Union[
                OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef1,
                OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef2,
            ]
        ]


    class TcpEqValue2:
        app_names: Union[
            OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef1,
            OneOfSequencesMatchEntriesTcpPortEqAppNamesOptionsDef2,
        ]
        port_numbers: Optional[
            Union[
                OneOfSequencesMatchEntriesPortEqNumbersOptionsDef1,
                OneOfSequencesMatchEntriesPortEqNumbersOptionsDef2,
            ]
        ]


    class EqValue1:
        # Match Source TCP Ports That is Equal to Any Value in This List
        tcp_eq_value: Union[TcpEqValue1, TcpEqValue2]


    class OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            SequencesMatchEntriesUdpPortEqAppNamesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class UdpEqValue1:
        port_numbers: Union[
            OneOfSequencesMatchEntriesPortEqNumbersOptionsDef1,
            OneOfSequencesMatchEntriesPortEqNumbersOptionsDef2,
        ]
        app_names: Optional[
            Union[
                OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef1,
                OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef2,
            ]
        ]


    class UdpEqValue2:
        app_names: Union[
            OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef1,
            OneOfSequencesMatchEntriesUdpPortEqAppNamesOptionsDef2,
        ]
        port_numbers: Optional[
            Union[
                OneOfSequencesMatchEntriesPortEqNumbersOptionsDef1,
                OneOfSequencesMatchEntriesPortEqNumbersOptionsDef2,
            ]
        ]


    class EqValue2:
        # Match Source UDP Ports That is Equal to Any Value in This List
        udp_eq_value: Union[UdpEqValue1, UdpEqValue2]


    class OneOfSequencesMatchEntriesPortRangeStartOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesMatchEntriesPortRangeStartOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesPortRangeEndOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesMatchEntriesPortRangeEndOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Range:
        """
        Source Port Range
        """

        end: Union[
            OneOfSequencesMatchEntriesPortRangeEndOptionsDef1,
            OneOfSequencesMatchEntriesPortRangeEndOptionsDef2,
        ]
        start: Union[
            OneOfSequencesMatchEntriesPortRangeStartOptionsDef1,
            OneOfSequencesMatchEntriesPortRangeStartOptionsDef2,
        ]


    class SourcePorts1:
        operator: Operator
        # Source Port Range
        range: Range
        # Match Source Ports That is Equal to Any Value in This List
        eq_value: Optional[Union[EqValue1, EqValue2]]
        gt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortGtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortGtValueOptionsDef2,
            ]
        ]
        lt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortLtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortLtValueOptionsDef2,
            ]
        ]


    class OneOfSequencesMatchEntriesPortOperatorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SequencesMatchEntriesPortOperatorDef


    class SourcePorts2:
        operator: OneOfSequencesMatchEntriesPortOperatorOptionsDef
        # Match Source Ports That is Equal to Any Value in This List
        eq_value: Optional[Union[EqValue1, EqValue2]]
        gt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortGtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortGtValueOptionsDef2,
            ]
        ]
        lt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortLtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortLtValueOptionsDef2,
            ]
        ]
        # Source Port Range
        range: Optional[Range]


    class OneOfSequencesMatchEntriesDestinationTypeHostOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesDestinationHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesDestinationHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesDestinationAddressOptionsDef1:
        destination_host: Union[
            OneOfSequencesMatchEntriesDestinationHostOptionsDef1,
            OneOfSequencesMatchEntriesDestinationHostOptionsDef2,
        ]
        destination_type: (
            OneOfSequencesMatchEntriesDestinationTypeHostOptionsDef
        )


    class OneOfSequencesMatchEntriesDestinationTypeIpPrefixOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSequencesMatchEntriesDestinationIpPrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesMatchEntriesDestinationIpPrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesDestinationAddressOptionsDef2:
        destination_ip_prefix: Union[
            OneOfSequencesMatchEntriesDestinationIpPrefixOptionsDef1,
            OneOfSequencesMatchEntriesDestinationIpPrefixOptionsDef2,
        ]
        destination_type: (
            OneOfSequencesMatchEntriesDestinationTypeIpPrefixOptionsDef
        )


    class DestinationPorts:
        eq_value: Optional[Any]


    class OneOfSequencesMatchEntriesIcmpMsgOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfSequencesMatchEntriesIcmpMsgOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSequencesMatchEntriesTcpBitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            SequencesMatchEntriesTcpBitDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesMatchEntriesDscpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfSequencesMatchEntriesDscpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MatchEntries1:
        protocol: Protocol
        destination_address: Optional[
            Union[
                OneOfSequencesMatchEntriesDestinationAddressOptionsDef1,
                OneOfSequencesMatchEntriesDestinationAddressOptionsDef2,
            ]
        ]
        destination_ports: Optional[DestinationPorts]
        dscp: Optional[
            Union[
                OneOfSequencesMatchEntriesDscpOptionsDef1,
                OneOfSequencesMatchEntriesDscpOptionsDef2,
            ]
        ]
        icmp_msg: Optional[
            Union[
                OneOfSequencesMatchEntriesIcmpMsgOptionsDef1,
                OneOfSequencesMatchEntriesIcmpMsgOptionsDef2,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSequencesMatchEntriesSourceAddressOptionsDef1,
                OneOfSequencesMatchEntriesSourceAddressOptionsDef2,
            ]
        ]
        # Source Ports
        source_ports: Optional[Union[SourcePorts1, SourcePorts2]]
        tcp_bit: Optional[OneOfSequencesMatchEntriesTcpBitOptionsDef]


    class OneOfSequencesMatchEntriesProtocolOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class Ipv4AclEqValue1:
        # Match Destination TCP Ports That is Equal to Any Value in This List
        tcp_eq_value: Union[TcpEqValue1, TcpEqValue2]


    class Ipv4AclEqValue2:
        # Match Destination UDP Ports That is Equal to Any Value in This List
        udp_eq_value: Union[UdpEqValue1, UdpEqValue2]


    class Ipv4AclRange:
        """
        Destination Port Range
        """

        end: Optional[
            Union[
                OneOfSequencesMatchEntriesPortRangeEndOptionsDef1,
                OneOfSequencesMatchEntriesPortRangeEndOptionsDef2,
            ]
        ]
        start: Optional[
            Union[
                OneOfSequencesMatchEntriesPortRangeStartOptionsDef1,
                OneOfSequencesMatchEntriesPortRangeStartOptionsDef2,
            ]
        ]


    class DestinationPorts1:
        operator: Operator
        # Destination Port Range
        range: Ipv4AclRange
        # Match Destination Ports That is Equal to Any Value in This List
        eq_value: Optional[Union[Ipv4AclEqValue1, Ipv4AclEqValue2]]
        gt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortGtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortGtValueOptionsDef2,
            ]
        ]
        lt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortLtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortLtValueOptionsDef2,
            ]
        ]


    class TransportIpv4AclEqValue1:
        # Match Destination TCP Ports That is Equal to Any Value in This List
        tcp_eq_value: Union[TcpEqValue1, TcpEqValue2]


    class TransportIpv4AclEqValue2:
        # Match Destination UDP Ports That is Equal to Any Value in This List
        udp_eq_value: Union[UdpEqValue1, UdpEqValue2]


    class TransportIpv4AclRange:
        """
        Destination Port Range
        """

        end: Optional[
            Union[
                OneOfSequencesMatchEntriesPortRangeEndOptionsDef1,
                OneOfSequencesMatchEntriesPortRangeEndOptionsDef2,
            ]
        ]
        start: Optional[
            Union[
                OneOfSequencesMatchEntriesPortRangeStartOptionsDef1,
                OneOfSequencesMatchEntriesPortRangeStartOptionsDef2,
            ]
        ]


    class DestinationPorts2:
        operator: OneOfSequencesMatchEntriesPortOperatorOptionsDef
        # Match Destination Ports That is Equal to Any Value in This List
        eq_value: Optional[
            Union[TransportIpv4AclEqValue1, TransportIpv4AclEqValue2]
        ]
        gt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortGtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortGtValueOptionsDef2,
            ]
        ]
        lt_value: Optional[
            Union[
                OneOfSequencesMatchEntriesPortLtValueOptionsDef1,
                OneOfSequencesMatchEntriesPortLtValueOptionsDef2,
            ]
        ]
        # Destination Port Range
        range: Optional[TransportIpv4AclRange]


    class MatchEntries2:
        protocol: OneOfSequencesMatchEntriesProtocolOptionsDef
        destination_address: Optional[
            Union[
                OneOfSequencesMatchEntriesDestinationAddressOptionsDef1,
                OneOfSequencesMatchEntriesDestinationAddressOptionsDef2,
            ]
        ]
        # Destination Ports
        destination_ports: Optional[
            Union[DestinationPorts1, DestinationPorts2]
        ]
        dscp: Optional[
            Union[
                OneOfSequencesMatchEntriesDscpOptionsDef1,
                OneOfSequencesMatchEntriesDscpOptionsDef2,
            ]
        ]
        icmp_msg: Optional[
            Union[
                OneOfSequencesMatchEntriesIcmpMsgOptionsDef1,
                OneOfSequencesMatchEntriesIcmpMsgOptionsDef2,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSequencesMatchEntriesSourceAddressOptionsDef1,
                OneOfSequencesMatchEntriesSourceAddressOptionsDef2,
            ]
        ]
        # Source Ports
        source_ports: Optional[Union[SourcePorts1, SourcePorts2]]
        tcp_bit: Optional[OneOfSequencesMatchEntriesTcpBitOptionsDef]


    class Actions1:
        log: OneOfSequencesActionsLogOptionsDef


    class OneOfSequencesActionsLogInputOptionsDef:
        option_type: GlobalOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class Actions2:
        log_input: OneOfSequencesActionsLogInputOptionsDef


    class ExtendedAclSequences:
        action_type: Union[
            OneOfSequencesActionTypeOptionsDef1,
            OneOfSequencesActionTypeOptionsDef2,
        ]
        # Define match conditions
        match_entries: Union[MatchEntries1, MatchEntries2]
        sequence_name: OneOfSequencesSequenceNameOptionsDef
        # Actions
        actions: Optional[Union[Actions1, Actions2]]


    class Ipv4AclData:
        acl_type: OneOfAclTypeOptionsDef
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Sequences for extended ACL
        extended_acl_sequences: Optional[List[ExtendedAclSequences]]
        # Sequences for extended ACL
        standard_acl_sequences: Optional[List[StandardAclSequences]]


    class Payload:
        """
        SD-Routing IPv4 ACL feature schema
        """

        data: Ipv4AclData
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
        # SD-Routing IPv4 ACL feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportIpv4AclPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportIpv4AclFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportIpv4AclData:
        acl_type: OneOfAclTypeOptionsDef
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Sequences for extended ACL
        extended_acl_sequences: Optional[List[ExtendedAclSequences]]
        # Sequences for extended ACL
        standard_acl_sequences: Optional[List[StandardAclSequences]]


    class CreateSdroutingTransportIpv4AclFeaturePostRequest:
        """
        SD-Routing IPv4 ACL feature schema
        """

        data: TransportIpv4AclData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportIpv4AclPayload:
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
        # SD-Routing IPv4 ACL feature schema
        payload: Optional[Payload]


    class EditSdroutingTransportIpv4AclFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportIpv4AclData:
        acl_type: OneOfAclTypeOptionsDef
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Sequences for extended ACL
        extended_acl_sequences: Optional[List[ExtendedAclSequences]]
        # Sequences for extended ACL
        standard_acl_sequences: Optional[List[StandardAclSequences]]


    class EditSdroutingTransportIpv4AclFeaturePutRequest:
        """
        SD-Routing IPv4 ACL feature schema
        """

        data: SdRoutingTransportIpv4AclData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


