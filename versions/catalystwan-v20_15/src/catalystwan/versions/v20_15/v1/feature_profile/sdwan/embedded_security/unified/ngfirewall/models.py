# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Literal, Optional, Union

GlobalOptionTypeDef = Literal["global"]

DefaultActionTypeDef = Literal["drop", "pass"]

SequencesBaseActionDef = Literal["drop", "inspect", "pass"]

VariableOptionTypeDef = Literal["variable"]

Value = Literal[
    "ABW",
    "AF",
    "AFG",
    "AGO",
    "AIA",
    "ALA",
    "ALB",
    "AN",
    "AND",
    "ANT",
    "ARE",
    "ARG",
    "ARM",
    "AS",
    "ASM",
    "ATA",
    "ATF",
    "ATG",
    "AUS",
    "AUT",
    "AZE",
    "BDI",
    "BEL",
    "BEN",
    "BES",
    "BFA",
    "BGD",
    "BGR",
    "BHR",
    "BHS",
    "BIH",
    "BLM",
    "BLR",
    "BLZ",
    "BMU",
    "BOL",
    "BRA",
    "BRB",
    "BRN",
    "BTN",
    "BVT",
    "BWA",
    "CAF",
    "CAN",
    "CCK",
    "CHE",
    "CHL",
    "CHN",
    "CIV",
    "CMR",
    "COD",
    "COG",
    "COK",
    "COL",
    "COM",
    "CPV",
    "CRI",
    "CUB",
    "CUW",
    "CXR",
    "CYM",
    "CYP",
    "CZE",
    "DEU",
    "DJI",
    "DMA",
    "DNK",
    "DOM",
    "DZA",
    "ECU",
    "EGY",
    "ERI",
    "ESH",
    "ESP",
    "EST",
    "ETH",
    "EU",
    "FIN",
    "FJI",
    "FLK",
    "FRA",
    "FRO",
    "FSM",
    "GAB",
    "GBR",
    "GEO",
    "GGY",
    "GHA",
    "GIB",
    "GIN",
    "GLP",
    "GMB",
    "GNB",
    "GNQ",
    "GRC",
    "GRD",
    "GRL",
    "GTM",
    "GUF",
    "GUM",
    "GUY",
    "HKG",
    "HMD",
    "HND",
    "HRV",
    "HTI",
    "HUN",
    "IDN",
    "IMN",
    "IND",
    "IOT",
    "IRL",
    "IRN",
    "IRQ",
    "ISL",
    "ISR",
    "ITA",
    "JAM",
    "JEY",
    "JOR",
    "JPN",
    "KAZ",
    "KEN",
    "KGZ",
    "KHM",
    "KIR",
    "KNA",
    "KOR",
    "KWT",
    "LAO",
    "LBN",
    "LBR",
    "LBY",
    "LCA",
    "LIE",
    "LKA",
    "LSO",
    "LTU",
    "LUX",
    "LVA",
    "MAC",
    "MAF",
    "MAR",
    "MCO",
    "MDA",
    "MDG",
    "MDV",
    "MEX",
    "MHL",
    "MKD",
    "MLI",
    "MLT",
    "MMR",
    "MNE",
    "MNG",
    "MNP",
    "MOZ",
    "MRT",
    "MSR",
    "MTQ",
    "MUS",
    "MWI",
    "MYS",
    "MYT",
    "NA",
    "NAM",
    "NCL",
    "NER",
    "NFK",
    "NGA",
    "NIC",
    "NIU",
    "NLD",
    "NOR",
    "NPL",
    "NRU",
    "NZL",
    "OC",
    "OMN",
    "PAK",
    "PAN",
    "PCN",
    "PER",
    "PHL",
    "PLW",
    "PNG",
    "POL",
    "PRI",
    "PRK",
    "PRT",
    "PRY",
    "PSE",
    "PYF",
    "QAT",
    "REU",
    "ROU",
    "RUS",
    "RWA",
    "SA",
    "SAU",
    "SDN",
    "SEN",
    "SGP",
    "SGS",
    "SHN",
    "SJM",
    "SLB",
    "SLE",
    "SLV",
    "SMR",
    "SOM",
    "SPM",
    "SRB",
    "SSD",
    "STP",
    "SUR",
    "SVK",
    "SVN",
    "SWE",
    "SWZ",
    "SXM",
    "SYC",
    "SYR",
    "TCA",
    "TCD",
    "TGO",
    "THA",
    "TJK",
    "TKL",
    "TKM",
    "TLS",
    "TON",
    "TTO",
    "TUN",
    "TUR",
    "TUV",
    "TWN",
    "TZA",
    "UGA",
    "UKR",
    "UMI",
    "URY",
    "USA",
    "UZB",
    "VAT",
    "VCT",
    "VEN",
    "VGB",
    "VIR",
    "VNM",
    "VUT",
    "WLF",
    "WSM",
    "YEM",
    "ZAF",
    "ZMB",
    "ZWE",
]

NgfirewallValue = Literal[
    "802-11-iapp",
    "ace-svr",
    "aol",
    "appleqtc",
    "bgp",
    "biff",
    "bootpc",
    "bootps",
    "cddbp",
    "cifs",
    "cisco-fna",
    "cisco-net-mgmt",
    "cisco-svcs",
    "cisco-sys",
    "cisco-tdp",
    "cisco-tna",
    "citrix",
    "citriximaclient",
    "clp",
    "creativepartnr",
    "creativeserver",
    "cuseeme",
    "daytime",
    "dbase",
    "dbcontrol_agent",
    "ddns-v3",
    "dhcp-failover",
    "discard",
    "dns",
    "dnsix",
    "echo",
    "entrust-svc-hand",
    "entrust-svcs",
    "exec",
    "fcip-port",
    "finger",
    "ftp",
    "ftps",
    "gdoi",
    "giop",
    "gopher",
    "gtpv0",
    "gtpv1",
    "h225ras",
    "h323",
    "h323callsigalt",
    "hp-alarm-mgr",
    "hp-collector",
    "hp-managed-node",
    "hsrp",
    "http",
    "https",
    "ica",
    "icabrowser",
    "icmp",
    "ident",
    "igmpv3lite",
    "imap",
    "imap3",
    "imaps",
    "ipass",
    "ipsec-msft",
    "ipx",
    "irc",
    "irc-serv",
    "ircs",
    "ircu",
    "isakmp",
    "iscsi",
    "iscsi-target",
    "kazaa",
    "kerberos",
    "kermit",
    "l2tp",
    "ldap",
    "ldap-admin",
    "ldaps",
    "login",
    "lotusmtap",
    "lotusnote",
    "mgcp",
    "microsoft-ds",
    "ms-cluster-net",
    "ms-dotnetster",
    "ms-sna",
    "ms-sql",
    "ms-sql-m",
    "msexch-routing",
    "msnmsgr",
    "msrpc",
    "mysql",
    "n2h2server",
    "ncp",
    "net8-cman",
    "netbios-dgm",
    "netbios-ns",
    "netshow",
    "netstat",
    "nfs",
    "nntp",
    "ntp",
    "oem-agent",
    "oracle",
    "oracle-em-vp",
    "oraclenames",
    "orasrv",
    "pcanywheredata",
    "pcanywherestat",
    "pop3",
    "pop3s",
    "pptp",
    "pwdgen",
    "qmtp",
    "r-winsock",
    "radius",
    "rdb-dbs-disp",
    "realmedia",
    "realsecure",
    "router",
    "rsvd",
    "rsvp-encap",
    "rsvp_tunnel",
    "rtc-pm-port",
    "rtelnet",
    "rtsp",
    "send",
    "shell",
    "sip",
    "sip-tls",
    "skinny",
    "sms",
    "smtp",
    "snmp",
    "snmptrap",
    "socks",
    "sql-net",
    "sqlserv",
    "sqlsrv",
    "ssh",
    "sshell",
    "ssp",
    "streamworks",
    "stun",
    "sunrpc",
    "syslog",
    "syslog-conn",
    "tacacs",
    "tacacs-ds",
    "tarantella",
    "tcp",
    "telnet",
    "telnets",
    "tftp",
    "time",
    "timed",
    "tr-rsrb",
    "ttc",
    "udp",
    "uucp",
    "vdolive",
    "vqp",
    "webster",
    "who",
    "wins",
    "x11",
    "xdmcp",
    "ymsgr",
]

SequencesActionsTypeDef = Literal["connectionEvents", "log"]


@dataclass
class CreateNgfirewallProfileParcelPostResponse:
    parcel_id: Optional[str] = _field(default=None, metadata={"alias": "parcelId"})


@dataclass
class OneOfDefaultActionTypeOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: DefaultActionTypeDef


@dataclass
class OneOfSequencesSequenceIdOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfSequencesSequenceNameOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfSequencesBaseActionOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: SequencesBaseActionDef


@dataclass
class OneOfSequencesSequenceTypeOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class RefIdArrayValue:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class ListDef:
    ref_id: RefIdArrayValue = _field(metadata={"alias": "refId"})


@dataclass
class Ipv4InputDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class Ipv4InputDef2:
    option_type: VariableOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str
    default: Optional[str] = _field(default=None)
    description: Optional[str] = _field(default=None)


@dataclass
class Ipv4MatchDef:
    ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2] = _field(metadata={"alias": "ipv4Value"})


@dataclass
class FqdnInputDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class FqdnMatchDef:
    fqdn_value: Union[FqdnInputDef1, Ipv4InputDef2] = _field(metadata={"alias": "fqdnValue"})


@dataclass
class SourcePortInputDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[Union[str, str]]


@dataclass
class SourcePortMatchDef:
    port_value: Union[SourcePortInputDef1, Ipv4InputDef2] = _field(metadata={"alias": "portValue"})


@dataclass
class AppMatchDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class DestinationPortInputDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[Union[str, str]]
    app: Optional[AppMatchDef] = _field(default=None)


@dataclass
class DestinationPortMatchDef:
    port_value: Union[DestinationPortInputDef1, Ipv4InputDef2] = _field(
        metadata={"alias": "portValue"}
    )


@dataclass
class GeoLocationMatchDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[Value]  # pytype: disable=annotation-type-mismatch


@dataclass
class IdentityUserMatchDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class IdentityUsergroupMatchDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]


@dataclass
class ProtocolMatchDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[str]
    app: Optional[AppMatchDef] = _field(default=None)


@dataclass
class ProtocolNameMatchDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: List[NgfirewallValue]  # pytype: disable=annotation-type-mismatch


@dataclass
class Entries:
    app: Optional[AppMatchDef] = _field(default=None)
    app_family: Optional[AppMatchDef] = _field(default=None, metadata={"alias": "appFamily"})
    app_list: Optional[ListDef] = _field(default=None, metadata={"alias": "appList"})
    app_list_flat: Optional[ListDef] = _field(default=None, metadata={"alias": "appListFlat"})
    destination_data_prefix_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationDataPrefixList"}
    )
    destination_fqdn: Optional[FqdnMatchDef] = _field(
        default=None, metadata={"alias": "destinationFqdn"}
    )
    destination_fqdn_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationFqdnList"}
    )
    destination_geo_location: Optional[Union[GeoLocationMatchDef1, Ipv4InputDef2]] = _field(
        default=None, metadata={"alias": "destinationGeoLocation"}
    )
    destination_geo_location_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationGeoLocationList"}
    )
    destination_ip: Optional[Ipv4MatchDef] = _field(
        default=None, metadata={"alias": "destinationIp"}
    )
    destination_port: Optional[DestinationPortMatchDef] = _field(
        default=None, metadata={"alias": "destinationPort"}
    )
    destination_port_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationPortList"}
    )
    destination_scalable_group_tag_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationScalableGroupTagList"}
    )
    destination_security_group: Optional[ListDef] = _field(
        default=None, metadata={"alias": "destinationSecurityGroup"}
    )
    protocol: Optional[ProtocolMatchDef] = _field(default=None)
    protocol_name: Optional[ProtocolNameMatchDef] = _field(
        default=None, metadata={"alias": "protocolName"}
    )
    protocol_name_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "protocolNameList"}
    )
    rule_set_list: Optional[ListDef] = _field(default=None, metadata={"alias": "ruleSetList"})
    source_data_prefix_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "sourceDataPrefixList"}
    )
    source_geo_location: Optional[Union[GeoLocationMatchDef1, Ipv4InputDef2]] = _field(
        default=None, metadata={"alias": "sourceGeoLocation"}
    )
    source_geo_location_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "sourceGeoLocationList"}
    )
    source_identity_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "sourceIdentityList"}
    )
    source_identity_user: Optional[IdentityUserMatchDef] = _field(
        default=None, metadata={"alias": "sourceIdentityUser"}
    )
    source_identity_usergroup: Optional[IdentityUsergroupMatchDef] = _field(
        default=None, metadata={"alias": "sourceIdentityUsergroup"}
    )
    source_ip: Optional[Ipv4MatchDef] = _field(default=None, metadata={"alias": "sourceIp"})
    source_port: Optional[SourcePortMatchDef] = _field(
        default=None, metadata={"alias": "sourcePort"}
    )
    source_port_list: Optional[ListDef] = _field(default=None, metadata={"alias": "sourcePortList"})
    source_scalable_group_tag_list: Optional[ListDef] = _field(
        default=None, metadata={"alias": "sourceScalableGroupTagList"}
    )
    source_security_group: Optional[ListDef] = _field(
        default=None, metadata={"alias": "sourceSecurityGroup"}
    )


@dataclass
class Match:
    entries: List[Entries]


@dataclass
class OneOfSequencesActionsTypeOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: SequencesActionsTypeDef  # pytype: disable=annotation-type-mismatch


@dataclass
class OneOfSequencesActionsParameterOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class Actions1:
    parameter: OneOfSequencesActionsParameterOptionsDef
    type_: OneOfSequencesActionsTypeOptionsDef = _field(metadata={"alias": "type"})


@dataclass
class Type:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class RefId:
    option_type: str = _field(metadata={"alias": "optionType"})
    value: str


@dataclass
class Parameter:
    ref_id: RefId = _field(metadata={"alias": "refId"})


@dataclass
class Actions2:
    parameter: Parameter
    type_: Type = _field(metadata={"alias": "type"})


@dataclass
class OneOfdisableSequenceDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: bool


@dataclass
class Sequences:
    # can be empty array or with type or parameter
    actions: List[Union[Actions1, Actions2]]
    base_action: OneOfSequencesBaseActionOptionsDef = _field(metadata={"alias": "baseAction"})
    match_: Match = _field(metadata={"alias": "match"})
    sequence_id: OneOfSequencesSequenceIdOptionsDef = _field(metadata={"alias": "sequenceId"})
    sequence_name: OneOfSequencesSequenceNameOptionsDef = _field(metadata={"alias": "sequenceName"})
    sequence_type: OneOfSequencesSequenceTypeOptionsDef = _field(metadata={"alias": "sequenceType"})
    disable_sequence: Optional[OneOfdisableSequenceDef] = _field(
        default=None, metadata={"alias": "disableSequence"}
    )


@dataclass
class Data:
    default_action_type: OneOfDefaultActionTypeOptionsDef = _field(
        metadata={"alias": "defaultActionType"}
    )
    sequences: List[Sequences]


@dataclass
class CreateNgfirewallProfileParcelPostRequest:
    """
    ngfirewall profile parcel schema for POST request
    """

    data: Data
    description: str
    name: str
    contains_tls: Optional[bool] = _field(default=False, metadata={"alias": "containsTls"})
    contains_utd: Optional[bool] = _field(default=False, metadata={"alias": "containsUtd"})
    # This is the documentation for POST request schema for ngfirewall profile parcel
    documentation: Optional[Any] = _field(default=None)
    metadata: Optional[Any] = _field(default=None)
    optimized: Optional[bool] = _field(default=True)
