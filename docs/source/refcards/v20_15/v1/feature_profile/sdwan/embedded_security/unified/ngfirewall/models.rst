======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

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


    class CreateNgfirewallProfileParcelPostResponse:
        parcel_id: Optional[str]


    class OneOfDefaultActionTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DefaultActionTypeDef


    class OneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SequencesBaseActionDef


    class OneOfSequencesSequenceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef:
        ref_id: RefIdArrayValue


    class Ipv4InputDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class Ipv4InputDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv4MatchDef:
        ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2]


    class FqdnInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class FqdnMatchDef:
        fqdn_value: Union[FqdnInputDef1, Ipv4InputDef2]


    class SourcePortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class SourcePortMatchDef:
        port_value: Union[SourcePortInputDef1, Ipv4InputDef2]


    class AppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class DestinationPortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]
        app: Optional[AppMatchDef]


    class DestinationPortMatchDef:
        port_value: Union[DestinationPortInputDef1, Ipv4InputDef2]


    class GeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[Value]  # pytype: disable=annotation-type-mismatch


    class IdentityUserMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class IdentityUsergroupMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ProtocolMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]
        app: Optional[AppMatchDef]


    class ProtocolNameMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[
            NgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class Entries:
        app: Optional[AppMatchDef]
        app_family: Optional[AppMatchDef]
        app_list: Optional[ListDef]
        app_list_flat: Optional[ListDef]
        destination_data_prefix_list: Optional[ListDef]
        destination_fqdn: Optional[FqdnMatchDef]
        destination_fqdn_list: Optional[ListDef]
        destination_geo_location: Optional[
            Union[GeoLocationMatchDef1, Ipv4InputDef2]
        ]
        destination_geo_location_list: Optional[ListDef]
        destination_ip: Optional[Ipv4MatchDef]
        destination_port: Optional[DestinationPortMatchDef]
        destination_port_list: Optional[ListDef]
        destination_scalable_group_tag_list: Optional[ListDef]
        destination_security_group: Optional[ListDef]
        protocol: Optional[ProtocolMatchDef]
        protocol_name: Optional[ProtocolNameMatchDef]
        protocol_name_list: Optional[ListDef]
        rule_set_list: Optional[ListDef]
        source_data_prefix_list: Optional[ListDef]
        source_geo_location: Optional[
            Union[GeoLocationMatchDef1, Ipv4InputDef2]
        ]
        source_geo_location_list: Optional[ListDef]
        source_identity_list: Optional[ListDef]
        source_identity_user: Optional[IdentityUserMatchDef]
        source_identity_usergroup: Optional[IdentityUsergroupMatchDef]
        source_ip: Optional[Ipv4MatchDef]
        source_port: Optional[SourcePortMatchDef]
        source_port_list: Optional[ListDef]
        source_scalable_group_tag_list: Optional[ListDef]
        source_security_group: Optional[ListDef]


    class Match:
        entries: List[Entries]


    class OneOfSequencesActionsTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SequencesActionsTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesActionsParameterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Actions1:
        parameter: OneOfSequencesActionsParameterOptionsDef
        type_: OneOfSequencesActionsTypeOptionsDef


    class Type:
        option_type: GlobalOptionTypeDef
        value: str


    class RefId:
        option_type: str
        value: str


    class Parameter:
        ref_id: RefId


    class Actions2:
        parameter: Parameter
        type_: Type


    class OneOfdisableSequenceDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class Sequences:
        # can be empty array or with type or parameter
        actions: List[Union[Actions1, Actions2]]
        base_action: OneOfSequencesBaseActionOptionsDef
        match_: Match
        sequence_id: OneOfSequencesSequenceIdOptionsDef
        sequence_name: OneOfSequencesSequenceNameOptionsDef
        sequence_type: OneOfSequencesSequenceTypeOptionsDef
        disable_sequence: Optional[OneOfdisableSequenceDef]


    class Data:
        default_action_type: OneOfDefaultActionTypeOptionsDef
        sequences: List[Sequences]


    class CreateNgfirewallProfileParcelPostRequest:
        """
        ngfirewall profile parcel schema for POST request
        """

        data: Data
        description: str
        name: str
        contains_tls: Optional[bool]
        contains_utd: Optional[bool]
        # This is the documentation for POST request schema for ngfirewall profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]
        optimized: Optional[bool]


