======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    Type = Literal["urlallowed", "urlblocked"]

    EntriesProtocolNameDef = Literal[
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

    EntriesCountryDef = Literal[
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ANT",
        "ARE",
        "ARG",
        "ARM",
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

    EntriesContinentDef = Literal[
        "AF", "AN", "AS", "EU", "NA", "OC", "SA"
    ]

    EntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    EntriesQueueDef = Literal["0", "1", "2", "3", "4", "5", "6", "7"]

    DefaultOptionTypeDef = Literal["default"]

    EntriesExceedDef = Literal["drop", "remark"]

    EntriesMapColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesEncapDef = Literal["gre", "ipsec"]

    PolicyObjectEntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    Value = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    PolicyObjectListTypeParam = Literal[
        "app-list",
        "app-probe",
        "as-path",
        "class",
        "color",
        "data-ipv6-prefix",
        "data-prefix",
        "expanded-community",
        "ext-community",
        "ipv4-network-object-group",
        "ipv4-service-object-group",
        "ipv6-prefix",
        "mirror",
        "policer",
        "preferred-color-group",
        "prefix",
        "security-data-ip-prefix",
        "security-fqdn",
        "security-geolocation",
        "security-identity",
        "security-ipssignature",
        "security-localapp",
        "security-localdomain",
        "security-port",
        "security-protocolname",
        "security-scalablegrouptag",
        "security-urllist",
        "security-zone",
        "sla-class",
        "standard-community",
        "tloc",
        "vpn-group",
    ]

    SdwanPolicyObjectEntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    PolicyObjectEntriesProtocolNameDef = Literal[
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

    PolicyObjectEntriesCountryDef = Literal[
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ANT",
        "ARE",
        "ARG",
        "ARM",
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

    PolicyObjectEntriesContinentDef = Literal[
        "AF", "AN", "AS", "EU", "NA", "OC", "SA"
    ]

    SdwanPolicyObjectEntriesCountryDef = Literal[
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ANT",
        "ARE",
        "ARG",
        "ARM",
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

    SdwanPolicyObjectEntriesContinentDef = Literal[
        "AF", "AN", "AS", "EU", "NA", "OC", "SA"
    ]

    PolicyObjectEntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    SdwanPolicyObjectEntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    FeatureProfileSdwanPolicyObjectEntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    PolicyObjectEntriesQueueDef = Literal[
        "0", "1", "2", "3", "4", "5", "6", "7"
    ]

    PolicyObjectEntriesExceedDef = Literal["drop", "remark"]

    PolicyObjectEntriesMapColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    FeatureProfileSdwanPolicyObjectEntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    PolicyObjectEntriesEncapDef = Literal["gre", "ipsec"]

    V1FeatureProfileSdwanPolicyObjectEntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    PolicyObjectValue = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    PolicyObjectEntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    SdwanPolicyObjectValue = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    SdwanPolicyObjectEntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    FeatureProfileSdwanPolicyObjectValue = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    FeatureProfileSdwanPolicyObjectEntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    V1FeatureProfileSdwanPolicyObjectValue = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    V1FeatureProfileSdwanPolicyObjectEntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    SdwanPolicyObjectEntriesProtocolNameDef = Literal[
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

    FeatureProfileSdwanPolicyObjectEntriesCountryDef = Literal[
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ANT",
        "ARE",
        "ARG",
        "ARM",
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

    FeatureProfileSdwanPolicyObjectEntriesContinentDef = Literal[
        "AF", "AN", "AS", "EU", "NA", "OC", "SA"
    ]

    V1FeatureProfileSdwanPolicyObjectEntriesCountryDef = Literal[
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ANT",
        "ARE",
        "ARG",
        "ARM",
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

    V1FeatureProfileSdwanPolicyObjectEntriesContinentDef = Literal[
        "AF", "AN", "AS", "EU", "NA", "OC", "SA"
    ]

    V1FeatureProfileSdwanPolicyObjectEntriesCriteriaDef = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    EntriesCriteriaDef1 = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    EntriesCriteriaDef2 = Literal[
        "jitter",
        "jitter-latency",
        "jitter-latency-loss",
        "jitter-loss",
        "jitter-loss-latency",
        "latency",
        "latency-jitter",
        "latency-jitter-loss",
        "latency-loss",
        "latency-loss-jitter",
        "loss",
        "loss-jitter",
        "loss-jitter-latency",
        "loss-latency",
        "loss-latency-jitter",
    ]

    SdwanPolicyObjectEntriesQueueDef = Literal[
        "0", "1", "2", "3", "4", "5", "6", "7"
    ]

    SdwanPolicyObjectEntriesExceedDef = Literal["drop", "remark"]

    SdwanPolicyObjectEntriesMapColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesColorDef1 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    SdwanPolicyObjectEntriesEncapDef = Literal["gre", "ipsec"]

    EntriesColorDef2 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    Value1 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesPathPreferenceDef1 = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    Value2 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesPathPreferenceDef2 = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    Value3 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesPathPreferenceDef3 = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]

    Value4 = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EntriesPathPreferenceDef4 = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]


    class OneOfIpv4PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Entries:
        ip_prefix: Union[
            OneOfIpv4PrefixOptionsDef1, OneOfIpv4PrefixOptionsDef2
        ]


    class PolicyObjectData:
        entries: List[Entries]


    class Schema2HubGeneratedPolicyobjectlisttypePost1:
        """
        security-data-ip-prefix profile parcel schema for POST request
        """

        data: PolicyObjectData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesPatternOptionsDef:
        option_type: GlobalOptionTypeDef
        # Must be valid FQDN
        value: str


    class PolicyObjectEntries:
        pattern: OneOfEntriesPatternOptionsDef


    class SdwanPolicyObjectData:
        entries: List[PolicyObjectEntries]


    class Schema2HubGeneratedPolicyobjectlisttypePost2:
        """
        security-data-fqdn-prefix profile parcel schema for POST request
        """

        data: SdwanPolicyObjectData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectEntries:
        port: OneOfEntriesPortOptionsDef


    class FeatureProfileSdwanPolicyObjectData:
        # Port List
        entries: List[SdwanPolicyObjectEntries]


    class Schema2HubGeneratedPolicyobjectlisttypePost3:
        """
        Port profile parcel schema for POST request
        """

        data: FeatureProfileSdwanPolicyObjectData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries1:
        app: OneOfEntriesAppOptionsDef
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef]


    class Entries2:
        app_family: OneOfEntriesAppFamilyOptionsDef
        app: Optional[OneOfEntriesAppOptionsDef]


    class V1FeatureProfileSdwanPolicyObjectData:
        # Localapp list
        entries: List[Union[Entries1, Entries2]]


    class Schema2HubGeneratedPolicyobjectlisttypePost4:
        """
        security-localapp profile parcel schema for POST request
        """

        data: V1FeatureProfileSdwanPolicyObjectData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesNameServerOptionsDef:
        option_type: GlobalOptionTypeDef
        # Must be valid utd regex. String cannot start with a '*' or a '+', be empty, or be more than 240 characters
        value: str


    class FeatureProfileSdwanPolicyObjectEntries:
        name_server: OneOfEntriesNameServerOptionsDef


    class Data1:
        entries: List[FeatureProfileSdwanPolicyObjectEntries]


    class Schema2HubGeneratedPolicyobjectlisttypePost5:
        """
        security-localdomain profile parcel schema for POST request
        """

        data: Data1
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesGeneratorIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesSignatureIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanPolicyObjectEntries:
        generator_id: OneOfEntriesGeneratorIdOptionsDef
        signature_id: OneOfEntriesSignatureIdOptionsDef


    class Data2:
        # Ips Signature
        entries: List[V1FeatureProfileSdwanPolicyObjectEntries]


    class Schema2HubGeneratedPolicyobjectlisttypePost6:
        """
        security-ipssignature profile parcel schema for POST request
        """

        data: Data2
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesUrlListOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries11:
        pattern: EntriesUrlListOptionsDef


    class Data3:
        # URL List
        entries: List[Entries11]
        type_: Type


    class Schema2HubGeneratedPolicyobjectlisttypePost7:
        """
        URL List profile parcel schema for POST request
        """

        data: Data3
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesProtocolNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesProtocolNameDef  # pytype: disable=annotation-type-mismatch


    class Entries21:
        protocol_name: OneOfEntriesProtocolNameOptionsDef


    class Data4:
        entries: List[Entries21]


    class Schema2HubGeneratedPolicyobjectlisttypePost8:
        """
        security-protocolname profile parcel schema for POST request
        """

        data: Data4
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesCountryOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesCountryDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfEntriesContinentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesContinentDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectEntries1:
        country: OneOfEntriesCountryOptionsDef
        continent: Optional[OneOfEntriesContinentOptionsDef]


    class PolicyObjectEntries2:
        continent: OneOfEntriesContinentOptionsDef
        country: Optional[OneOfEntriesCountryOptionsDef]


    class Data5:
        # Geolocation  List
        entries: List[Union[PolicyObjectEntries1, PolicyObjectEntries2]]


    class Schema2HubGeneratedPolicyobjectlisttypePost9:
        """
        Geolocation profile parcel schema for POST request
        """

        data: Data5
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class OneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class SdwanPolicyObjectEntries1:
        user: OneOfEntriesUserOptionsDef
        user_group: Optional[OneOfEntriesUserGroupOptionsDef]


    class SdwanPolicyObjectEntries2:
        user_group: OneOfEntriesUserGroupOptionsDef
        user: Optional[OneOfEntriesUserOptionsDef]


    class Data6:
        # Array of Users and User Groups
        entries: List[
            Union[SdwanPolicyObjectEntries1, SdwanPolicyObjectEntries2]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost10:
        """
        security-identity profile parcel schema for POST request
        """

        data: Data6
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesSgtNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries3:
        sgt_name: OneOfEntriesSgtNameOptionsDef
        tag: OneOfEntriesTagOptionsDef


    class Data7:
        entries: List[Entries3]


    class Schema2HubGeneratedPolicyobjectlisttypePost11:
        """
        security-scalablegrouptag profile parcel schema for POST request
        """

        data: Data7
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data8:
        entries: List[None]


    class Schema2HubGeneratedPolicyobjectlisttypePost12:
        """
        security-zone profile parcel schema for POST request
        """

        data: Data8
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectOneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectEntries1:
        app: PolicyObjectOneOfEntriesAppOptionsDef
        app_family: Optional[PolicyObjectOneOfEntriesAppFamilyOptionsDef]


    class SdwanPolicyObjectOneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectEntries2:
        app_family: SdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef
        app: Optional[SdwanPolicyObjectOneOfEntriesAppOptionsDef]


    class Data9:
        # Centralized Policy App List
        entries: List[
            Union[
                FeatureProfileSdwanPolicyObjectEntries1,
                FeatureProfileSdwanPolicyObjectEntries2,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost13:
        """
        Centralized Policy App List profile parcel schema for POST request
        """

        data: Data9
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesCriteriaDef


    class FallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[OneOfEntriesCriteriaOptionsDef]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef]
        loss_variance: Optional[OneOfEntriesLossOptionsDef]


    class V1FeatureProfileSdwanPolicyObjectEntries1:
        latency: OneOfEntriesLatencyOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class V1FeatureProfileSdwanPolicyObjectEntries2:
        loss: OneOfEntriesLossOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        latency: Optional[OneOfEntriesLatencyOptionsDef]


    class PolicyObjectEntries3:
        jitter: OneOfEntriesJitterOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        latency: Optional[OneOfEntriesLatencyOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class Data10:
        # Sla class List
        entries: List[
            Union[
                V1FeatureProfileSdwanPolicyObjectEntries1,
                V1FeatureProfileSdwanPolicyObjectEntries2,
                PolicyObjectEntries3,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost14:
        """
        Sla class profile parcel schema for POST request
        """

        data: Data10
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class AsPathListNum:
        """
        As path List Number
        """

        option_type: Optional[GlobalOptionTypeDef]
        value: Optional[int]


    class EntriesAsPathOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries4:
        as_path: EntriesAsPathOptionsDef


    class Data11:
        # As path List Number
        as_path_list_num: AsPathListNum
        # AS Path List
        entries: List[Entries4]


    class Schema2HubGeneratedPolicyobjectlisttypePost15:
        """
        as path profile parcel schema
        """

        data: Data11
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesQueueDef  # pytype: disable=annotation-type-mismatch


    class Entries5:
        queue: EntriesQueueOptionsDef


    class Data12:
        # class map List
        entries: List[Entries5]


    class Schema2HubGeneratedPolicyobjectlisttypePost16:
        """
        class profile parcel schema
        """

        data: Data12
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries6:
        ipv6_address: EntriesIpv6AddressOptionsDef
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef


    class Data13:
        # IPv6 Prefix List
        entries: Optional[List[Entries6]]


    class Schema2HubGeneratedPolicyobjectlisttypePost17:
        """
        Ipv6 data prefix profile parcel schema for POST request
        """

        data: Data13
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries7:
        ipv4_address: EntriesIpv4AddressOptionsDef
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef


    class Data14:
        # IPv4 Data Prefix List
        entries: Optional[List[Entries7]]


    class Schema2HubGeneratedPolicyobjectlisttypePost18:
        """
        ipv4 data prefix profile parcel schema for POST request
        """

        data: Data14
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfExpandedCommunityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfExpandedCommunityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data15:
        expanded_community_list: Union[
            OneOfExpandedCommunityOptionsDef1,
            OneOfExpandedCommunityOptionsDef2,
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost19:
        """
        expanded Community list profile parcel schema
        """

        data: Data15
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesExtCommunityOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries8:
        ext_community: EntriesExtCommunityOptionsDef


    class Data16:
        # Extended Community List
        entries: List[Entries8]


    class Schema2HubGeneratedPolicyobjectlisttypePost20:
        """
        extended community list profile parcel schema
        """

        data: Data16
        name: str
        description: Optional[str]
        metadata: Optional[Any]


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


    class OneOfEntriesAddressTypeHostOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Entries12:
        address_type: OneOfEntriesAddressTypeHostOptionsDef
        host: Union[
            OneOfEntriesHostOptionsDef1, OneOfEntriesHostOptionsDef2
        ]


    class OneOfEntriesAddressTypeIpPrefixOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesIpPrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesIpPrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Entries22:
        address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef
        ip_prefix: Union[
            OneOfEntriesIpPrefixOptionsDef1,
            OneOfEntriesIpPrefixOptionsDef2,
        ]


    class OneOfEntriesAddressTypeObjectGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class SdwanPolicyObjectEntries3:
        address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef
        object_group: ParcelReferenceDef


    class OneOfEntriesAddressTypeHostRangeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostRangeStartOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostRangeStartOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEntriesHostRangeEndOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostRangeEndOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class HostRange:
        """
        Host Address Range
        """

        end: Union[
            OneOfEntriesHostRangeEndOptionsDef1,
            OneOfEntriesHostRangeEndOptionsDef2,
        ]
        start: Union[
            OneOfEntriesHostRangeStartOptionsDef1,
            OneOfEntriesHostRangeStartOptionsDef2,
        ]


    class PolicyObjectEntries4:
        address_type: OneOfEntriesAddressTypeHostRangeOptionsDef
        # Host Address Range
        host_range: HostRange


    class Data17:
        # object-group Entries
        entries: List[
            Union[
                Entries12,
                Entries22,
                SdwanPolicyObjectEntries3,
                PolicyObjectEntries4,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost21:
        """
        Ipv4 Network Object Group profile parcel schema
        """

        data: Data17
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries13:
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


    class PolicyObjectEntries21:
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


    class PolicyObjectRange:
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
        range: PolicyObjectRange


    class PolicyObjectEntries22:
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


    class Data18:
        # object-group Entries
        entries: List[
            Union[
                Entries13,
                Union[PolicyObjectEntries21, PolicyObjectEntries22],
            ]
        ]
        description: Optional[
            Union[
                PolicyObjectOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePost22:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data18
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectEntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectEntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries9:
        ipv6_address: PolicyObjectEntriesIpv6AddressOptionsDef
        ipv6_prefix_length: PolicyObjectEntriesIpv6PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data19:
        # IPv6 Prefix List
        entries: List[Entries9]


    class Schema2HubGeneratedPolicyobjectlisttypePost23:
        """
        Ipv6 prefix profile parcel schema
        """

        data: Data19
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesRemoteDestIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class EntriesSourceIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class Entries10:
        remote_dest_ip: EntriesRemoteDestIpOptionsDef
        source_ip: EntriesSourceIpOptionsDef


    class Data20:
        # Mirror List
        entries: List[Entries10]


    class Schema2HubGeneratedPolicyobjectlisttypePost24:
        """
        mirror profile parcel schema for POST request
        """

        data: Data20
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesBurstOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesExceedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesExceedDef  # pytype: disable=annotation-type-mismatch
        )


    class EntriesRateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries11_1:
        burst: EntriesBurstOptionsDef
        exceed: EntriesExceedOptionsDef
        rate: EntriesRateOptionsDef


    class Data21:
        # Policer Entries
        entries: List[Entries11_1]


    class Schema2HubGeneratedPolicyobjectlisttypePost25:
        """
        policer profile parcel schema for POST request
        """

        data: Data21
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectEntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectEntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectEntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectEntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries12_1:
        ipv4_address: PolicyObjectEntriesIpv4AddressOptionsDef
        ipv4_prefix_length: PolicyObjectEntriesIpv4PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            PolicyObjectEntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            PolicyObjectEntriesLeRangePrefixLengthOptionsDef
        ]


    class Data22:
        # IPv4 Prefix List
        entries: List[Entries12_1]


    class Schema2HubGeneratedPolicyobjectlisttypePost26:
        """
        Ipv4 prefix profile parcel schema
        """

        data: Data22
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class StandardCommunityOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries13_1:
        standard_community: StandardCommunityOptionsDef


    class Data23:
        # Standard Community List
        entries: List[Entries13_1]


    class Schema2HubGeneratedPolicyobjectlisttypePost27:
        """
        standard Community list profile parcel schema
        """

        data: Data23
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class Entries14:
        vpn: EntriesVpnOptionsDef


    class Data24:
        # VPN List
        entries: List[Entries14]


    class Schema2HubGeneratedPolicyobjectlisttypePost28:
        """
        vpn list profile parcel schema
        """

        data: Data24
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesMapColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesMapColorDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfEntriesMapDscpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Map:
        color: OneOfEntriesMapColorOptionsDef
        dscp: Optional[OneOfEntriesMapDscpOptionsDef]


    class ForwardingClass1:
        option_type: GlobalOptionTypeDef
        value: str


    class ForwardingClass2:
        ref_id: RefId


    class Entries15:
        # Forwarding Class Name
        forwarding_class: Union[ForwardingClass1, ForwardingClass2]
        # Map
        map: List[Map]


    class Data25:
        # App Probe List
        entries: List[Entries15]


    class Schema2HubGeneratedPolicyobjectlisttypePost29:
        """
        app-probe profile parcel schema for POST request
        """

        data: Data25
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesTlocOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesEncapDef  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries16:
        color: OneOfEntriesColorOptionsDef
        encap: OneOfEntriesEncapOptionsDef
        tloc: OneOfEntriesTlocOptionsDef
        preference: Optional[OneOfEntriesPreferenceOptionsDef]


    class Data26:
        # TLOC List
        entries: Optional[List[Entries16]]


    class Schema2HubGeneratedPolicyobjectlisttypePost30:
        """
        tloc profile parcel schema for POST request
        """

        data: Data26
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesColorDef  # pytype: disable=annotation-type-mismatch


    class Entries17:
        color: PolicyObjectOneOfEntriesColorOptionsDef


    class Data27:
        # Color List
        entries: Optional[List[Entries17]]


    class Schema2HubGeneratedPolicyobjectlisttypePost31:
        """
        color profile parcel schema for POST request
        """

        data: Data27
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class OneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Value]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PrimaryPreference1:
        color_preference: OneOfEntriesColorPreferenceOptionsDef
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef]


    class PrimaryPreference2:
        path_preference: OneOfEntriesPathPreferenceOptionsDef
        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef]


    class SecondaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef]
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef]


    class TertiaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef]
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef]


    class Entries18:
        # Object with an color and path preference
        primary_preference: Union[PrimaryPreference1, PrimaryPreference2]
        # Object with an color and path preference
        secondary_preference: Optional[SecondaryPreference]
        # Object with an color and path preference
        tertiary_preference: Optional[TertiaryPreference]


    class Data28:
        # Preferred Color Group List
        entries: Optional[List[Entries18]]


    class Schema2HubGeneratedPolicyobjectlisttypePost32:
        """
        preferred-color-group profile parcel schema for POST request
        """

        data: Data28
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
        payload: Optional[
            Union[
                Schema2HubGeneratedPolicyobjectlisttypePost1,
                Schema2HubGeneratedPolicyobjectlisttypePost2,
                Schema2HubGeneratedPolicyobjectlisttypePost3,
                Schema2HubGeneratedPolicyobjectlisttypePost4,
                Schema2HubGeneratedPolicyobjectlisttypePost5,
                Schema2HubGeneratedPolicyobjectlisttypePost6,
                Schema2HubGeneratedPolicyobjectlisttypePost7,
                Schema2HubGeneratedPolicyobjectlisttypePost8,
                Schema2HubGeneratedPolicyobjectlisttypePost9,
                Schema2HubGeneratedPolicyobjectlisttypePost10,
                Schema2HubGeneratedPolicyobjectlisttypePost11,
                Schema2HubGeneratedPolicyobjectlisttypePost12,
                Schema2HubGeneratedPolicyobjectlisttypePost13,
                Schema2HubGeneratedPolicyobjectlisttypePost14,
                Schema2HubGeneratedPolicyobjectlisttypePost15,
                Schema2HubGeneratedPolicyobjectlisttypePost16,
                Schema2HubGeneratedPolicyobjectlisttypePost17,
                Schema2HubGeneratedPolicyobjectlisttypePost18,
                Schema2HubGeneratedPolicyobjectlisttypePost19,
                Schema2HubGeneratedPolicyobjectlisttypePost20,
                Schema2HubGeneratedPolicyobjectlisttypePost21,
                Schema2HubGeneratedPolicyobjectlisttypePost22,
                Schema2HubGeneratedPolicyobjectlisttypePost23,
                Schema2HubGeneratedPolicyobjectlisttypePost24,
                Schema2HubGeneratedPolicyobjectlisttypePost25,
                Schema2HubGeneratedPolicyobjectlisttypePost26,
                Schema2HubGeneratedPolicyobjectlisttypePost27,
                Schema2HubGeneratedPolicyobjectlisttypePost28,
                Schema2HubGeneratedPolicyobjectlisttypePost29,
                Schema2HubGeneratedPolicyobjectlisttypePost30,
                Schema2HubGeneratedPolicyobjectlisttypePost31,
                Schema2HubGeneratedPolicyobjectlisttypePost32,
            ]
        ]


    class GetListSdwanPolicyObjectSecurityDataIpPrefixPayload:
        data: Optional[List[Data]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class Data29:
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest1:
        """
        security-data-ip-prefix profile parcel schema for POST request
        """

        data: Data29
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries19:
        pattern: OneOfEntriesPatternOptionsDef


    class Data30:
        entries: List[Entries19]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest2:
        """
        security-data-fqdn-prefix profile parcel schema for POST request
        """

        data: Data30
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries20:
        port: OneOfEntriesPortOptionsDef


    class Data31:
        # Port List
        entries: List[Entries20]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest3:
        """
        Port profile parcel schema for POST request
        """

        data: Data31
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data32:
        # Localapp list
        entries: List[Union[Entries1, Entries2]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest4:
        """
        security-localapp profile parcel schema for POST request
        """

        data: Data32
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries21_1:
        name_server: OneOfEntriesNameServerOptionsDef


    class Data33:
        entries: List[Entries21_1]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest5:
        """
        security-localdomain profile parcel schema for POST request
        """

        data: Data33
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries22_1:
        generator_id: OneOfEntriesGeneratorIdOptionsDef
        signature_id: OneOfEntriesSignatureIdOptionsDef


    class Data34:
        # Ips Signature
        entries: List[Entries22_1]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest6:
        """
        security-ipssignature profile parcel schema for POST request
        """

        data: Data34
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries23:
        pattern: EntriesUrlListOptionsDef


    class Data35:
        # URL List
        entries: List[Entries23]
        type_: Type


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest7:
        """
        URL List profile parcel schema for POST request
        """

        data: Data35
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries24:
        protocol_name: OneOfEntriesProtocolNameOptionsDef


    class Data36:
        entries: List[Entries24]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest8:
        """
        security-protocolname profile parcel schema for POST request
        """

        data: Data36
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries14_1:
        country: OneOfEntriesCountryOptionsDef
        continent: Optional[OneOfEntriesContinentOptionsDef]


    class Entries23_1:
        continent: OneOfEntriesContinentOptionsDef
        country: Optional[OneOfEntriesCountryOptionsDef]


    class Data37:
        # Geolocation  List
        entries: List[Union[Entries14_1, Entries23_1]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest9:
        """
        Geolocation profile parcel schema for POST request
        """

        data: Data37
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries15_1:
        user: OneOfEntriesUserOptionsDef
        user_group: Optional[OneOfEntriesUserGroupOptionsDef]


    class Entries24_1:
        user_group: OneOfEntriesUserGroupOptionsDef
        user: Optional[OneOfEntriesUserOptionsDef]


    class Data38:
        # Array of Users and User Groups
        entries: List[Union[Entries15_1, Entries24_1]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest10:
        """
        security-identity profile parcel schema for POST request
        """

        data: Data38
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries25:
        sgt_name: OneOfEntriesSgtNameOptionsDef
        tag: OneOfEntriesTagOptionsDef


    class Data39:
        entries: List[Entries25]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest11:
        """
        security-scalablegrouptag profile parcel schema for POST request
        """

        data: Data39
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data40:
        entries: List[None]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest12:
        """
        security-zone profile parcel schema for POST request
        """

        data: Data40
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class FeatureProfileSdwanPolicyObjectOneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries16_1:
        app: FeatureProfileSdwanPolicyObjectOneOfEntriesAppOptionsDef
        app_family: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef
        ]


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries25_1:
        app_family: V1FeatureProfileSdwanPolicyObjectOneOfEntriesAppFamilyOptionsDef
        app: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesAppOptionsDef
        ]


    class Data41:
        # Centralized Policy App List
        entries: List[Union[Entries16_1, Entries25_1]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest13:
        """
        Centralized Policy App List profile parcel schema for POST request
        """

        data: Data41
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries17_1:
        latency: OneOfEntriesLatencyOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class Entries26:
        loss: OneOfEntriesLossOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        jitter: Optional[OneOfEntriesJitterOptionsDef]
        latency: Optional[OneOfEntriesLatencyOptionsDef]


    class FeatureProfileSdwanPolicyObjectEntries3:
        jitter: OneOfEntriesJitterOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel]
        latency: Optional[OneOfEntriesLatencyOptionsDef]
        loss: Optional[OneOfEntriesLossOptionsDef]


    class Data42:
        # Sla class List
        entries: List[
            Union[
                Entries17_1,
                Entries26,
                FeatureProfileSdwanPolicyObjectEntries3,
            ]
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest14:
        """
        Sla class profile parcel schema for POST request
        """

        data: Data42
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries26_1:
        as_path: EntriesAsPathOptionsDef


    class Data43:
        # As path List Number
        as_path_list_num: AsPathListNum
        # AS Path List
        entries: List[Entries26_1]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest15:
        """
        as path profile parcel schema
        """

        data: Data43
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries27:
        queue: EntriesQueueOptionsDef


    class Data44:
        # class map List
        entries: List[Entries27]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest16:
        """
        class profile parcel schema
        """

        data: Data44
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries28:
        ipv6_address: EntriesIpv6AddressOptionsDef
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef


    class Data45:
        # IPv6 Prefix List
        entries: Optional[List[Entries28]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest17:
        """
        Ipv6 data prefix profile parcel schema for POST request
        """

        data: Data45
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries29:
        ipv4_address: EntriesIpv4AddressOptionsDef
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef


    class Data46:
        # IPv4 Data Prefix List
        entries: Optional[List[Entries29]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest18:
        """
        ipv4 data prefix profile parcel schema for POST request
        """

        data: Data46
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data47:
        expanded_community_list: Union[
            OneOfExpandedCommunityOptionsDef1,
            OneOfExpandedCommunityOptionsDef2,
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest19:
        """
        expanded Community list profile parcel schema
        """

        data: Data47
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries30:
        ext_community: EntriesExtCommunityOptionsDef


    class Data48:
        # Extended Community List
        entries: List[Entries30]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest20:
        """
        extended community list profile parcel schema
        """

        data: Data48
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries18_1:
        address_type: OneOfEntriesAddressTypeHostOptionsDef
        host: Union[
            OneOfEntriesHostOptionsDef1, OneOfEntriesHostOptionsDef2
        ]


    class Entries27_1:
        address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef
        ip_prefix: Union[
            OneOfEntriesIpPrefixOptionsDef1,
            OneOfEntriesIpPrefixOptionsDef2,
        ]


    class V1FeatureProfileSdwanPolicyObjectEntries3:
        address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef
        object_group: ParcelReferenceDef


    class SdwanPolicyObjectEntries4:
        address_type: OneOfEntriesAddressTypeHostRangeOptionsDef
        # Host Address Range
        host_range: HostRange


    class Data49:
        # object-group Entries
        entries: List[
            Union[
                Entries18_1,
                Entries27_1,
                V1FeatureProfileSdwanPolicyObjectEntries3,
                SdwanPolicyObjectEntries4,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest21:
        """
        Ipv4 Network Object Group profile parcel schema
        """

        data: Data49
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries19_1:
        object_group: ParcelReferenceDef


    class SdwanPolicyObjectEntries21:
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


    class SdwanPolicyObjectEntries22:
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


    class Data50:
        # object-group Entries
        entries: List[
            Union[
                Entries19_1,
                Union[
                    SdwanPolicyObjectEntries21, SdwanPolicyObjectEntries22
                ],
            ]
        ]
        description: Optional[
            Union[
                SdwanPolicyObjectOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest22:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data50
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectEntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries31:
        ipv6_address: SdwanPolicyObjectEntriesIpv6AddressOptionsDef
        ipv6_prefix_length: (
            SdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef
        )
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data51:
        # IPv6 Prefix List
        entries: List[Entries31]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest23:
        """
        Ipv6 prefix profile parcel schema
        """

        data: Data51
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries32:
        remote_dest_ip: EntriesRemoteDestIpOptionsDef
        source_ip: EntriesSourceIpOptionsDef


    class Data52:
        # Mirror List
        entries: List[Entries32]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest24:
        """
        mirror profile parcel schema for POST request
        """

        data: Data52
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries33:
        burst: EntriesBurstOptionsDef
        exceed: EntriesExceedOptionsDef
        rate: EntriesRateOptionsDef


    class Data53:
        # Policer Entries
        entries: List[Entries33]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest25:
        """
        policer profile parcel schema for POST request
        """

        data: Data53
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectEntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries34:
        ipv4_address: SdwanPolicyObjectEntriesIpv4AddressOptionsDef
        ipv4_prefix_length: (
            SdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef
        )
        ge_range_prefix_length: Optional[
            SdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            SdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef
        ]


    class Data54:
        # IPv4 Prefix List
        entries: List[Entries34]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest26:
        """
        Ipv4 prefix profile parcel schema
        """

        data: Data54
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries35:
        standard_community: StandardCommunityOptionsDef


    class Data55:
        # Standard Community List
        entries: List[Entries35]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest27:
        """
        standard Community list profile parcel schema
        """

        data: Data55
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries36:
        vpn: EntriesVpnOptionsDef


    class Data56:
        # VPN List
        entries: List[Entries36]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest28:
        """
        vpn list profile parcel schema
        """

        data: Data56
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries37:
        # Forwarding Class Name
        forwarding_class: Union[ForwardingClass1, ForwardingClass2]
        # Map
        map: List[Map]


    class Data57:
        # App Probe List
        entries: List[Entries37]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest29:
        """
        app-probe profile parcel schema for POST request
        """

        data: Data57
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries38:
        color: OneOfEntriesColorOptionsDef
        encap: OneOfEntriesEncapOptionsDef
        tloc: OneOfEntriesTlocOptionsDef
        preference: Optional[OneOfEntriesPreferenceOptionsDef]


    class Data58:
        # TLOC List
        entries: Optional[List[Entries38]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest30:
        """
        tloc profile parcel schema for POST request
        """

        data: Data58
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesColorDef  # pytype: disable=annotation-type-mismatch


    class Entries39:
        color: SdwanPolicyObjectOneOfEntriesColorOptionsDef


    class Data59:
        # Color List
        entries: Optional[List[Entries39]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest31:
        """
        color profile parcel schema for POST request
        """

        data: Data59
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class Entries40:
        # Object with an color and path preference
        primary_preference: Union[PrimaryPreference1, PrimaryPreference2]
        # Object with an color and path preference
        secondary_preference: Optional[SecondaryPreference]
        # Object with an color and path preference
        tertiary_preference: Optional[TertiaryPreference]


    class Data60:
        # Preferred Color Group List
        entries: Optional[List[Entries40]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest32:
        """
        preferred-color-group profile parcel schema for POST request
        """

        data: Data60
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class Data61:
        entries: List[Entries]


    class Schema2HubGeneratedPolicyobjectlisttypePut1:
        """
        security-data-ip-prefix profile parcel schema for PUT request
        """

        data: Data61
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesPatternOptionsDef:
        option_type: GlobalOptionTypeDef
        # Must be valid FQDN
        value: str


    class Entries41:
        pattern: PolicyObjectOneOfEntriesPatternOptionsDef


    class Data62:
        entries: List[Entries41]


    class Schema2HubGeneratedPolicyobjectlisttypePut2:
        """
        security-data-fqdn-prefix profile parcel schema for PUT request
        """

        data: Data62
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries42:
        port: PolicyObjectOneOfEntriesPortOptionsDef


    class Data63:
        # Port List
        entries: List[Entries42]


    class Schema2HubGeneratedPolicyobjectlisttypePut3:
        """
        Port profile parcel schema for PUT request
        """

        data: Data63
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesAppOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries110:
        app: OneOfEntriesAppOptionsDef1
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef1]


    class OneOfEntriesAppOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries28_1:
        app_family: OneOfEntriesAppFamilyOptionsDef2
        app: Optional[OneOfEntriesAppOptionsDef2]


    class Data64:
        # Localapp list
        entries: List[Union[Entries110, Entries28_1]]


    class Schema2HubGeneratedPolicyobjectlisttypePut4:
        """
        security-localapp profile parcel schema for PUT request
        """

        data: Data64
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesNameServerOptionsDef:
        option_type: GlobalOptionTypeDef
        # String cannot start with a '.' or a '*', be empty, or be more than 240 characters
        value: str


    class Entries43:
        name_server: PolicyObjectOneOfEntriesNameServerOptionsDef


    class Data65:
        entries: List[Entries43]


    class Schema2HubGeneratedPolicyobjectlisttypePut5:
        """
        security-localdomain profile parcel schema for PUT request
        """

        data: Data65
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesGeneratorIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectOneOfEntriesSignatureIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries44:
        generator_id: PolicyObjectOneOfEntriesGeneratorIdOptionsDef
        signature_id: PolicyObjectOneOfEntriesSignatureIdOptionsDef


    class Data66:
        # Ips Signature
        entries: List[Entries44]


    class Schema2HubGeneratedPolicyobjectlisttypePut6:
        """
        security-ipssignature profile parcel schema for PUT request
        """

        data: Data66
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectEntriesUrlListOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries45:
        pattern: PolicyObjectEntriesUrlListOptionsDef


    class Data67:
        # URL List
        entries: List[Entries45]
        type_: Type


    class Schema2HubGeneratedPolicyobjectlisttypePut7:
        """
        URL List profile parcel schema for PUT request
        """

        data: Data67
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesProtocolNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesProtocolNameDef  # pytype: disable=annotation-type-mismatch


    class Entries46:
        protocol_name: PolicyObjectOneOfEntriesProtocolNameOptionsDef


    class Data68:
        entries: List[Entries46]


    class Schema2HubGeneratedPolicyobjectlisttypePut8:
        """
        security-protocolname profile parcel schema for PUT request
        """

        data: Data68
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesCountryOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesCountryDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectOneOfEntriesContinentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesContinentDef  # pytype: disable=annotation-type-mismatch


    class Entries111:
        country: PolicyObjectOneOfEntriesCountryOptionsDef
        continent: Optional[PolicyObjectOneOfEntriesContinentOptionsDef]


    class SdwanPolicyObjectOneOfEntriesCountryOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesCountryDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectOneOfEntriesContinentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesContinentDef  # pytype: disable=annotation-type-mismatch


    class Entries29_1:
        continent: SdwanPolicyObjectOneOfEntriesContinentOptionsDef
        country: Optional[SdwanPolicyObjectOneOfEntriesCountryOptionsDef]


    class Data69:
        # Geolocation  List
        entries: List[Union[Entries111, Entries29_1]]


    class Schema2HubGeneratedPolicyobjectlisttypePut9:
        """
        Geolocation profile parcel schema for PUT request
        """

        data: Data69
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class PolicyObjectOneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class Entries112:
        user: PolicyObjectOneOfEntriesUserOptionsDef
        user_group: Optional[PolicyObjectOneOfEntriesUserGroupOptionsDef]


    class SdwanPolicyObjectOneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class SdwanPolicyObjectOneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class Entries210:
        user_group: SdwanPolicyObjectOneOfEntriesUserGroupOptionsDef
        user: Optional[SdwanPolicyObjectOneOfEntriesUserOptionsDef]


    class Data70:
        # Array of Users and User Groups
        entries: List[Union[Entries112, Entries210]]


    class Schema2HubGeneratedPolicyobjectlisttypePut10:
        """
        security-identity profile parcel schema for PUT request
        """

        data: Data70
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesSgtNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectOneOfEntriesTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries47:
        sgt_name: PolicyObjectOneOfEntriesSgtNameOptionsDef
        tag: PolicyObjectOneOfEntriesTagOptionsDef


    class Data71:
        entries: List[Entries47]


    class Schema2HubGeneratedPolicyobjectlisttypePut11:
        """
        security-scalablegrouptag profile parcel schema for PUT request
        """

        data: Data71
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data72:
        entries: List[None]


    class Schema2HubGeneratedPolicyobjectlisttypePut12:
        """
        security-zone profile parcel schema for PUT request
        """

        data: Data72
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesAppOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries113:
        app: OneOfEntriesAppOptionsDef3
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef3]


    class OneOfEntriesAppOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries211:
        app_family: OneOfEntriesAppFamilyOptionsDef4
        app: Optional[OneOfEntriesAppOptionsDef4]


    class Data73:
        # centralized-applist list
        entries: List[Union[Entries113, Entries211]]


    class Schema2HubGeneratedPolicyobjectlisttypePut13:
        """
        security-localapp profile parcel schema for PUT request
        """

        data: Data73
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectOneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectOneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectOneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesCriteriaDef


    class SdwanPolicyObjectOneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectOneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectOneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectFallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[PolicyObjectOneOfEntriesCriteriaOptionsDef]
        jitter_variance: Optional[
            SdwanPolicyObjectOneOfEntriesJitterOptionsDef
        ]
        latency_variance: Optional[
            SdwanPolicyObjectOneOfEntriesLatencyOptionsDef
        ]
        loss_variance: Optional[
            SdwanPolicyObjectOneOfEntriesLossOptionsDef
        ]


    class Entries114:
        latency: PolicyObjectOneOfEntriesLatencyOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[PolicyObjectFallbackBestTunnel]
        jitter: Optional[PolicyObjectOneOfEntriesJitterOptionsDef]
        loss: Optional[PolicyObjectOneOfEntriesLossOptionsDef]


    class FeatureProfileSdwanPolicyObjectOneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectOneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectOneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectOneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesCriteriaDef


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesLossOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesJitterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectFallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[
            SdwanPolicyObjectOneOfEntriesCriteriaOptionsDef
        ]
        jitter_variance: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesJitterOptionsDef
        ]
        latency_variance: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesLatencyOptionsDef
        ]
        loss_variance: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesLossOptionsDef
        ]


    class Entries212:
        loss: FeatureProfileSdwanPolicyObjectOneOfEntriesLossOptionsDef
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[
            SdwanPolicyObjectFallbackBestTunnel
        ]
        jitter: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesJitterOptionsDef
        ]
        latency: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesLatencyOptionsDef
        ]


    class OneOfEntriesLatencyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectOneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectEntriesCriteriaDef


    class OneOfEntriesLossOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLatencyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectFallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesCriteriaOptionsDef
        ]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef2]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef2]
        loss_variance: Optional[OneOfEntriesLossOptionsDef2]


    class Entries31_1:
        jitter: OneOfEntriesJitterOptionsDef1
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[
            FeatureProfileSdwanPolicyObjectFallbackBestTunnel
        ]
        latency: Optional[OneOfEntriesLatencyOptionsDef1]
        loss: Optional[OneOfEntriesLossOptionsDef1]


    class Data74:
        # Sla class List
        entries: List[Union[Entries114, Entries212, Entries31_1]]


    class Schema2HubGeneratedPolicyobjectlisttypePut14:
        """
        Sla class profile parcel schema for PUT request
        """

        data: Data74
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries48:
        as_path: EntriesAsPathOptionsDef


    class Data75:
        # As path List Number
        as_path_list_num: AsPathListNum
        # AS Path List
        entries: List[Entries48]


    class Schema2HubGeneratedPolicyobjectlisttypePut15:
        """
        as path profile parcel schema
        """

        data: Data75
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectEntriesQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesQueueDef  # pytype: disable=annotation-type-mismatch


    class Entries49:
        queue: PolicyObjectEntriesQueueOptionsDef


    class Data76:
        # class map List
        entries: List[Entries49]


    class Schema2HubGeneratedPolicyobjectlisttypePut16:
        """
        class profile parcel schema for PUT request
        """

        data: Data76
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class FeatureProfileSdwanPolicyObjectEntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries50:
        ipv6_address: (
            FeatureProfileSdwanPolicyObjectEntriesIpv6AddressOptionsDef
        )
        ipv6_prefix_length: FeatureProfileSdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef


    class Data77:
        # IPv6 Prefix List
        entries: Optional[List[Entries50]]


    class Schema2HubGeneratedPolicyobjectlisttypePut17:
        """
        Ipv6 data prefix profile parcel schema for PUT request
        """

        data: Data77
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class FeatureProfileSdwanPolicyObjectEntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries51:
        ipv4_address: (
            FeatureProfileSdwanPolicyObjectEntriesIpv4AddressOptionsDef
        )
        ipv4_prefix_length: FeatureProfileSdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef


    class Data78:
        # IPv4 Data Prefix List
        entries: Optional[List[Entries51]]


    class Schema2HubGeneratedPolicyobjectlisttypePut18:
        """
        ipv4 data prefix profile parcel schema for PUT request
        """

        data: Data78
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class Data79:
        expanded_community_list: Union[
            OneOfExpandedCommunityOptionsDef1,
            OneOfExpandedCommunityOptionsDef2,
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePut19:
        """
        expanded Community list profile parcel schema
        """

        data: Data79
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries52:
        ext_community: EntriesExtCommunityOptionsDef


    class Data80:
        # Extended Community List
        entries: List[Entries52]


    class Schema2HubGeneratedPolicyobjectlisttypePut20:
        """
        extended community list profile parcel schema
        """

        data: Data80
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries115:
        address_type: OneOfEntriesAddressTypeHostOptionsDef
        host: Union[
            OneOfEntriesHostOptionsDef1, OneOfEntriesHostOptionsDef2
        ]


    class Entries213:
        address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef
        ip_prefix: Union[
            OneOfEntriesIpPrefixOptionsDef1,
            OneOfEntriesIpPrefixOptionsDef2,
        ]


    class Entries32_1:
        address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef
        object_group: ParcelReferenceDef


    class FeatureProfileSdwanPolicyObjectEntries4:
        address_type: OneOfEntriesAddressTypeHostRangeOptionsDef
        # Host Address Range
        host_range: HostRange


    class Data81:
        # object-group Entries
        entries: List[
            Union[
                Entries115,
                Entries213,
                Entries32_1,
                FeatureProfileSdwanPolicyObjectEntries4,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePut21:
        """
        Ipv4 Network Object Group profile parcel schema
        """

        data: Data81
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class FeatureProfileSdwanPolicyObjectOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries116:
        object_group: ParcelReferenceDef


    class FeatureProfileSdwanPolicyObjectEntries21:
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


    class FeatureProfileSdwanPolicyObjectEntries22:
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


    class Data82:
        # object-group Entries
        entries: List[
            Union[
                Entries116,
                Union[
                    FeatureProfileSdwanPolicyObjectEntries21,
                    FeatureProfileSdwanPolicyObjectEntries22,
                ],
            ]
        ]
        description: Optional[
            Union[
                FeatureProfileSdwanPolicyObjectOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class Schema2HubGeneratedPolicyobjectlisttypePut22:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data82
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class V1FeatureProfileSdwanPolicyObjectEntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries53:
        ipv6_address: (
            V1FeatureProfileSdwanPolicyObjectEntriesIpv6AddressOptionsDef
        )
        ipv6_prefix_length: V1FeatureProfileSdwanPolicyObjectEntriesIpv6PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data83:
        # IPv6 Prefix List
        entries: List[Entries53]


    class Schema2HubGeneratedPolicyobjectlisttypePut23:
        """
        Ipv6 prefix profile parcel schema
        """

        data: Data83
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectEntriesRemoteDestIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class PolicyObjectEntriesSourceIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class Entries54:
        remote_dest_ip: PolicyObjectEntriesRemoteDestIpOptionsDef
        source_ip: PolicyObjectEntriesSourceIpOptionsDef


    class Data84:
        # Mirror List
        entries: List[Entries54]


    class Schema2HubGeneratedPolicyobjectlisttypePut24:
        """
        mirror profile parcel schema for PUT request
        """

        data: Data84
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class PolicyObjectEntriesBurstOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectEntriesExceedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesExceedDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectEntriesRateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries55:
        burst: PolicyObjectEntriesBurstOptionsDef
        exceed: PolicyObjectEntriesExceedOptionsDef
        rate: PolicyObjectEntriesRateOptionsDef


    class Data85:
        # Policer Entries
        entries: List[Entries55]


    class Schema2HubGeneratedPolicyobjectlisttypePut25:
        """
        policer profile parcel schema for PUT request
        """

        data: Data85
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class V1FeatureProfileSdwanPolicyObjectEntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries56:
        ipv4_address: (
            V1FeatureProfileSdwanPolicyObjectEntriesIpv4AddressOptionsDef
        )
        ipv4_prefix_length: V1FeatureProfileSdwanPolicyObjectEntriesIpv4PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            FeatureProfileSdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            FeatureProfileSdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef
        ]


    class Data86:
        # IPv4 Prefix List
        entries: List[Entries56]


    class Schema2HubGeneratedPolicyobjectlisttypePut26:
        """
        Ipv4 prefix profile parcel schema
        """

        data: Data86
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries57:
        standard_community: StandardCommunityOptionsDef


    class Data87:
        # Standard Community List
        entries: List[Entries57]


    class Schema2HubGeneratedPolicyobjectlisttypePut27:
        """
        standard Community list profile parcel schema
        """

        data: Data87
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries58:
        vpn: EntriesVpnOptionsDef


    class Data88:
        # VPN List
        entries: List[Entries58]


    class Schema2HubGeneratedPolicyobjectlisttypePut28:
        """
        vpn list profile parcel schema
        """

        data: Data88
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesMapColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesMapColorDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectOneOfEntriesMapDscpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyObjectMap:
        color: PolicyObjectOneOfEntriesMapColorOptionsDef
        dscp: Optional[PolicyObjectOneOfEntriesMapDscpOptionsDef]


    class PolicyObjectForwardingClass1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries59:
        # Forwarding Class Name
        forwarding_class: Union[
            PolicyObjectForwardingClass1, ForwardingClass2
        ]
        # Map
        map: List[PolicyObjectMap]


    class Data89:
        # App Probe List
        entries: List[Entries59]


    class Schema2HubGeneratedPolicyobjectlisttypePut29:
        """
        app-probe profile parcel schema for PUT request
        """

        data: Data89
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectOneOfEntriesTlocOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectOneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectEntriesColorDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectOneOfEntriesEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesEncapDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectOneOfEntriesPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries60:
        color: FeatureProfileSdwanPolicyObjectOneOfEntriesColorOptionsDef
        encap: PolicyObjectOneOfEntriesEncapOptionsDef
        tloc: PolicyObjectOneOfEntriesTlocOptionsDef
        preference: Optional[PolicyObjectOneOfEntriesPreferenceOptionsDef]


    class Data90:
        # TLOC List
        entries: Optional[List[Entries60]]


    class Schema2HubGeneratedPolicyobjectlisttypePut30:
        """
        tloc profile parcel schema for PUT request
        """

        data: Data90
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectEntriesColorDef  # pytype: disable=annotation-type-mismatch


    class Entries61:
        color: (
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesColorOptionsDef
        )


    class Data91:
        # Color List
        entries: Optional[List[Entries61]]


    class Schema2HubGeneratedPolicyobjectlisttypePut31:
        """
        color profile parcel schema for PUT request
        """

        data: Data91
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class PolicyObjectOneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            PolicyObjectValue
        ]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectOneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectEntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectPrimaryPreference1:
        color_preference: (
            PolicyObjectOneOfEntriesColorPreferenceOptionsDef
        )
        path_preference: Optional[
            PolicyObjectOneOfEntriesPathPreferenceOptionsDef
        ]


    class SdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            SdwanPolicyObjectValue
        ]  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectPrimaryPreference2:
        path_preference: (
            SdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef
        )
        color_preference: Optional[
            SdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef
        ]


    class FeatureProfileSdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            FeatureProfileSdwanPolicyObjectValue
        ]  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectEntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectSecondaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef
        ]
        path_preference: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef
        ]


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            V1FeatureProfileSdwanPolicyObjectValue
        ]  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectEntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectTertiaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesColorPreferenceOptionsDef
        ]
        path_preference: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesPathPreferenceOptionsDef
        ]


    class Entries62:
        # Object with an color and path preference
        primary_preference: Union[
            PolicyObjectPrimaryPreference1, PolicyObjectPrimaryPreference2
        ]
        # Object with an color and path preference
        secondary_preference: Optional[PolicyObjectSecondaryPreference]
        # Object with an color and path preference
        tertiary_preference: Optional[PolicyObjectTertiaryPreference]


    class Data92:
        # Preferred Color Group List
        entries: Optional[List[Entries62]]


    class Schema2HubGeneratedPolicyobjectlisttypePut32:
        """
        preferred-color-group profile parcel schema for PUT request
        """

        data: Data92
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanPolicyObjectSecurityDataIpPrefixPayload:
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
        payload: Optional[
            Union[
                Schema2HubGeneratedPolicyobjectlisttypePut1,
                Schema2HubGeneratedPolicyobjectlisttypePut2,
                Schema2HubGeneratedPolicyobjectlisttypePut3,
                Schema2HubGeneratedPolicyobjectlisttypePut4,
                Schema2HubGeneratedPolicyobjectlisttypePut5,
                Schema2HubGeneratedPolicyobjectlisttypePut6,
                Schema2HubGeneratedPolicyobjectlisttypePut7,
                Schema2HubGeneratedPolicyobjectlisttypePut8,
                Schema2HubGeneratedPolicyobjectlisttypePut9,
                Schema2HubGeneratedPolicyobjectlisttypePut10,
                Schema2HubGeneratedPolicyobjectlisttypePut11,
                Schema2HubGeneratedPolicyobjectlisttypePut12,
                Schema2HubGeneratedPolicyobjectlisttypePut13,
                Schema2HubGeneratedPolicyobjectlisttypePut14,
                Schema2HubGeneratedPolicyobjectlisttypePut15,
                Schema2HubGeneratedPolicyobjectlisttypePut16,
                Schema2HubGeneratedPolicyobjectlisttypePut17,
                Schema2HubGeneratedPolicyobjectlisttypePut18,
                Schema2HubGeneratedPolicyobjectlisttypePut19,
                Schema2HubGeneratedPolicyobjectlisttypePut20,
                Schema2HubGeneratedPolicyobjectlisttypePut21,
                Schema2HubGeneratedPolicyobjectlisttypePut22,
                Schema2HubGeneratedPolicyobjectlisttypePut23,
                Schema2HubGeneratedPolicyobjectlisttypePut24,
                Schema2HubGeneratedPolicyobjectlisttypePut25,
                Schema2HubGeneratedPolicyobjectlisttypePut26,
                Schema2HubGeneratedPolicyobjectlisttypePut27,
                Schema2HubGeneratedPolicyobjectlisttypePut28,
                Schema2HubGeneratedPolicyobjectlisttypePut29,
                Schema2HubGeneratedPolicyobjectlisttypePut30,
                Schema2HubGeneratedPolicyobjectlisttypePut31,
                Schema2HubGeneratedPolicyobjectlisttypePut32,
            ]
        ]


    class EditDataPrefixProfileParcelForPolicyObjectPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class Data93:
        entries: List[Entries]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest1:
        """
        security-data-ip-prefix profile parcel schema for PUT request
        """

        data: Data93
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesPatternOptionsDef:
        option_type: GlobalOptionTypeDef
        # Must be valid FQDN
        value: str


    class Entries63:
        pattern: SdwanPolicyObjectOneOfEntriesPatternOptionsDef


    class Data94:
        entries: List[Entries63]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest2:
        """
        security-data-fqdn-prefix profile parcel schema for PUT request
        """

        data: Data94
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries64:
        port: SdwanPolicyObjectOneOfEntriesPortOptionsDef


    class Data95:
        # Port List
        entries: List[Entries64]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest3:
        """
        Port profile parcel schema for PUT request
        """

        data: Data95
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesAppOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries117:
        app: OneOfEntriesAppOptionsDef5
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef5]


    class OneOfEntriesAppOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries214:
        app_family: OneOfEntriesAppFamilyOptionsDef6
        app: Optional[OneOfEntriesAppOptionsDef6]


    class Data96:
        # Localapp list
        entries: List[Union[Entries117, Entries214]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest4:
        """
        security-localapp profile parcel schema for PUT request
        """

        data: Data96
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesNameServerOptionsDef:
        option_type: GlobalOptionTypeDef
        # String cannot start with a '.' or a '*', be empty, or be more than 240 characters
        value: str


    class Entries65:
        name_server: SdwanPolicyObjectOneOfEntriesNameServerOptionsDef


    class Data97:
        entries: List[Entries65]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest5:
        """
        security-localdomain profile parcel schema for PUT request
        """

        data: Data97
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesGeneratorIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectOneOfEntriesSignatureIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries66:
        generator_id: SdwanPolicyObjectOneOfEntriesGeneratorIdOptionsDef
        signature_id: SdwanPolicyObjectOneOfEntriesSignatureIdOptionsDef


    class Data98:
        # Ips Signature
        entries: List[Entries66]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest6:
        """
        security-ipssignature profile parcel schema for PUT request
        """

        data: Data98
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectEntriesUrlListOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries67:
        pattern: SdwanPolicyObjectEntriesUrlListOptionsDef


    class Data99:
        # URL List
        entries: List[Entries67]
        type_: Type


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest7:
        """
        URL List profile parcel schema for PUT request
        """

        data: Data99
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesProtocolNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesProtocolNameDef  # pytype: disable=annotation-type-mismatch


    class Entries68:
        protocol_name: SdwanPolicyObjectOneOfEntriesProtocolNameOptionsDef


    class Data100:
        entries: List[Entries68]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest8:
        """
        security-protocolname profile parcel schema for PUT request
        """

        data: Data100
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class FeatureProfileSdwanPolicyObjectOneOfEntriesCountryOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectEntriesCountryDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanPolicyObjectOneOfEntriesContinentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectEntriesContinentDef  # pytype: disable=annotation-type-mismatch


    class Entries118:
        country: (
            FeatureProfileSdwanPolicyObjectOneOfEntriesCountryOptionsDef
        )
        continent: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesContinentOptionsDef
        ]


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesCountryOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectEntriesCountryDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesContinentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectEntriesContinentDef  # pytype: disable=annotation-type-mismatch


    class Entries215:
        continent: V1FeatureProfileSdwanPolicyObjectOneOfEntriesContinentOptionsDef
        country: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesCountryOptionsDef
        ]


    class Data101:
        # Geolocation  List
        entries: List[Union[Entries118, Entries215]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest9:
        """
        Geolocation profile parcel schema for PUT request
        """

        data: Data101
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class FeatureProfileSdwanPolicyObjectOneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class FeatureProfileSdwanPolicyObjectOneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class Entries119:
        user: FeatureProfileSdwanPolicyObjectOneOfEntriesUserOptionsDef
        user_group: Optional[
            FeatureProfileSdwanPolicyObjectOneOfEntriesUserGroupOptionsDef
        ]


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class Entries216:
        user_group: V1FeatureProfileSdwanPolicyObjectOneOfEntriesUserGroupOptionsDef
        user: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesUserOptionsDef
        ]


    class Data102:
        # Array of Users and User Groups
        entries: List[Union[Entries119, Entries216]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest10:
        """
        security-identity profile parcel schema for PUT request
        """

        data: Data102
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesSgtNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectOneOfEntriesTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries69:
        sgt_name: SdwanPolicyObjectOneOfEntriesSgtNameOptionsDef
        tag: SdwanPolicyObjectOneOfEntriesTagOptionsDef


    class Data103:
        entries: List[Entries69]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest11:
        """
        security-scalablegrouptag profile parcel schema for PUT request
        """

        data: Data103
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data104:
        entries: List[None]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest12:
        """
        security-zone profile parcel schema for PUT request
        """

        data: Data104
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesAppOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries120:
        app: OneOfEntriesAppOptionsDef7
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef7]


    class OneOfEntriesAppOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries217:
        app_family: OneOfEntriesAppFamilyOptionsDef8
        app: Optional[OneOfEntriesAppOptionsDef8]


    class Data105:
        # centralized-applist list
        entries: List[Union[Entries120, Entries217]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest13:
        """
        security-localapp profile parcel schema for PUT request
        """

        data: Data105
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesLatencyOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectOneOfEntriesCriteriaOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectEntriesCriteriaDef


    class OneOfEntriesLossOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLatencyOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectFallbackBestTunnel:
        """
        Object with a criteria and variance
        """

        criteria: Optional[
            V1FeatureProfileSdwanPolicyObjectOneOfEntriesCriteriaOptionsDef
        ]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef4]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef4]
        loss_variance: Optional[OneOfEntriesLossOptionsDef4]


    class Entries121:
        latency: OneOfEntriesLatencyOptionsDef3
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[
            V1FeatureProfileSdwanPolicyObjectFallbackBestTunnel
        ]
        jitter: Optional[OneOfEntriesJitterOptionsDef3]
        loss: Optional[OneOfEntriesLossOptionsDef3]


    class OneOfEntriesLatencyOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesCriteriaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EntriesCriteriaDef1


    class OneOfEntriesLossOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLatencyOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: int


    class FallbackBestTunnel1:
        """
        Object with a criteria and variance
        """

        criteria: Optional[OneOfEntriesCriteriaOptionsDef1]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef6]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef6]
        loss_variance: Optional[OneOfEntriesLossOptionsDef6]


    class Entries218:
        loss: OneOfEntriesLossOptionsDef5
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel1]
        jitter: Optional[OneOfEntriesJitterOptionsDef5]
        latency: Optional[OneOfEntriesLatencyOptionsDef5]


    class OneOfEntriesLatencyOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLossOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesCriteriaOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: EntriesCriteriaDef2


    class OneOfEntriesLossOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesLatencyOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEntriesJitterOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: int


    class FallbackBestTunnel2:
        """
        Object with a criteria and variance
        """

        criteria: Optional[OneOfEntriesCriteriaOptionsDef2]
        jitter_variance: Optional[OneOfEntriesJitterOptionsDef8]
        latency_variance: Optional[OneOfEntriesLatencyOptionsDef8]
        loss_variance: Optional[OneOfEntriesLossOptionsDef8]


    class Entries33_1:
        jitter: OneOfEntriesJitterOptionsDef7
        app_probe_class: Optional[ParcelReferenceDef]
        # Object with a criteria and variance
        fallback_best_tunnel: Optional[FallbackBestTunnel2]
        latency: Optional[OneOfEntriesLatencyOptionsDef7]
        loss: Optional[OneOfEntriesLossOptionsDef7]


    class Data106:
        # Sla class List
        entries: List[Union[Entries121, Entries218, Entries33_1]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest14:
        """
        Sla class profile parcel schema for PUT request
        """

        data: Data106
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries70:
        as_path: EntriesAsPathOptionsDef


    class Data107:
        # As path List Number
        as_path_list_num: AsPathListNum
        # AS Path List
        entries: List[Entries70]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest15:
        """
        as path profile parcel schema
        """

        data: Data107
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectEntriesQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesQueueDef  # pytype: disable=annotation-type-mismatch


    class Entries71:
        queue: SdwanPolicyObjectEntriesQueueOptionsDef


    class Data108:
        # class map List
        entries: List[Entries71]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest16:
        """
        class profile parcel schema for PUT request
        """

        data: Data108
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class EntriesIpv6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv6PrefixLengthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries72:
        ipv6_address: EntriesIpv6AddressOptionsDef1
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef1


    class Data109:
        # IPv6 Prefix List
        entries: Optional[List[Entries72]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest17:
        """
        Ipv6 data prefix profile parcel schema for PUT request
        """

        data: Data109
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class EntriesIpv4AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv4PrefixLengthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries73:
        ipv4_address: EntriesIpv4AddressOptionsDef1
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef1


    class Data110:
        # IPv4 Data Prefix List
        entries: Optional[List[Entries73]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest18:
        """
        ipv4 data prefix profile parcel schema for PUT request
        """

        data: Data110
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class Data111:
        expanded_community_list: Union[
            OneOfExpandedCommunityOptionsDef1,
            OneOfExpandedCommunityOptionsDef2,
        ]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest19:
        """
        expanded Community list profile parcel schema
        """

        data: Data111
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries74:
        ext_community: EntriesExtCommunityOptionsDef


    class Data112:
        # Extended Community List
        entries: List[Entries74]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest20:
        """
        extended community list profile parcel schema
        """

        data: Data112
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries122:
        address_type: OneOfEntriesAddressTypeHostOptionsDef
        host: Union[
            OneOfEntriesHostOptionsDef1, OneOfEntriesHostOptionsDef2
        ]


    class Entries219:
        address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef
        ip_prefix: Union[
            OneOfEntriesIpPrefixOptionsDef1,
            OneOfEntriesIpPrefixOptionsDef2,
        ]


    class Entries34_1:
        address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef
        object_group: ParcelReferenceDef


    class V1FeatureProfileSdwanPolicyObjectEntries4:
        address_type: OneOfEntriesAddressTypeHostRangeOptionsDef
        # Host Address Range
        host_range: HostRange


    class Data113:
        # object-group Entries
        entries: List[
            Union[
                Entries122,
                Entries219,
                Entries34_1,
                V1FeatureProfileSdwanPolicyObjectEntries4,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest21:
        """
        Ipv4 Network Object Group profile parcel schema
        """

        data: Data113
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class V1FeatureProfileSdwanPolicyObjectOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries123:
        object_group: ParcelReferenceDef


    class V1FeatureProfileSdwanPolicyObjectEntries21:
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


    class V1FeatureProfileSdwanPolicyObjectEntries22:
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


    class Data114:
        # object-group Entries
        entries: List[
            Union[
                Entries123,
                Union[
                    V1FeatureProfileSdwanPolicyObjectEntries21,
                    V1FeatureProfileSdwanPolicyObjectEntries22,
                ],
            ]
        ]
        description: Optional[
            Union[
                V1FeatureProfileSdwanPolicyObjectOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest22:
        """
        Ipv4 Service Object Group profile parcel schema
        """

        data: Data114
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EntriesIpv6AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv6PrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries75:
        ipv6_address: EntriesIpv6AddressOptionsDef2
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef2
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data115:
        # IPv6 Prefix List
        entries: List[Entries75]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest23:
        """
        Ipv6 prefix profile parcel schema
        """

        data: Data115
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectEntriesRemoteDestIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class SdwanPolicyObjectEntriesSourceIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class Entries76:
        remote_dest_ip: SdwanPolicyObjectEntriesRemoteDestIpOptionsDef
        source_ip: SdwanPolicyObjectEntriesSourceIpOptionsDef


    class Data116:
        # Mirror List
        entries: List[Entries76]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest24:
        """
        mirror profile parcel schema for PUT request
        """

        data: Data116
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SdwanPolicyObjectEntriesBurstOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectEntriesExceedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesExceedDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectEntriesRateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries77:
        burst: SdwanPolicyObjectEntriesBurstOptionsDef
        exceed: SdwanPolicyObjectEntriesExceedOptionsDef
        rate: SdwanPolicyObjectEntriesRateOptionsDef


    class Data117:
        # Policer Entries
        entries: List[Entries77]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest25:
        """
        policer profile parcel schema for PUT request
        """

        data: Data117
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class EntriesIpv4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv4PrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries78:
        ipv4_address: EntriesIpv4AddressOptionsDef2
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef2
        ge_range_prefix_length: Optional[
            V1FeatureProfileSdwanPolicyObjectEntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            V1FeatureProfileSdwanPolicyObjectEntriesLeRangePrefixLengthOptionsDef
        ]


    class Data118:
        # IPv4 Prefix List
        entries: List[Entries78]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest26:
        """
        Ipv4 prefix profile parcel schema
        """

        data: Data118
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries79:
        standard_community: StandardCommunityOptionsDef


    class Data119:
        # Standard Community List
        entries: List[Entries79]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest27:
        """
        standard Community list profile parcel schema
        """

        data: Data119
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Entries80:
        vpn: EntriesVpnOptionsDef


    class Data120:
        # VPN List
        entries: List[Entries80]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest28:
        """
        vpn list profile parcel schema
        """

        data: Data120
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesMapColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesMapColorDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectOneOfEntriesMapDscpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanPolicyObjectMap:
        color: SdwanPolicyObjectOneOfEntriesMapColorOptionsDef
        dscp: Optional[SdwanPolicyObjectOneOfEntriesMapDscpOptionsDef]


    class SdwanPolicyObjectForwardingClass1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries81:
        # Forwarding Class Name
        forwarding_class: Union[
            SdwanPolicyObjectForwardingClass1, ForwardingClass2
        ]
        # Map
        map: List[SdwanPolicyObjectMap]


    class Data121:
        # App Probe List
        entries: List[Entries81]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest29:
        """
        app-probe profile parcel schema for PUT request
        """

        data: Data121
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanPolicyObjectOneOfEntriesTlocOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesColorDef1  # pytype: disable=annotation-type-mismatch
        )


    class SdwanPolicyObjectOneOfEntriesEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectEntriesEncapDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectOneOfEntriesPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries82:
        color: OneOfEntriesColorOptionsDef1
        encap: SdwanPolicyObjectOneOfEntriesEncapOptionsDef
        tloc: SdwanPolicyObjectOneOfEntriesTlocOptionsDef
        preference: Optional[
            SdwanPolicyObjectOneOfEntriesPreferenceOptionsDef
        ]


    class Data122:
        # TLOC List
        entries: Optional[List[Entries82]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest30:
        """
        tloc profile parcel schema for PUT request
        """

        data: Data122
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfEntriesColorOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesColorDef2  # pytype: disable=annotation-type-mismatch
        )


    class Entries83:
        color: OneOfEntriesColorOptionsDef2


    class Data123:
        # Color List
        entries: Optional[List[Entries83]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest31:
        """
        color profile parcel schema for PUT request
        """

        data: Data123
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class OneOfEntriesColorPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[Value1]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef1  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectPrimaryPreference1:
        color_preference: OneOfEntriesColorPreferenceOptionsDef1
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef1]


    class OneOfEntriesColorPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[Value2]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef2  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectPrimaryPreference2:
        path_preference: OneOfEntriesPathPreferenceOptionsDef2
        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef2]


    class OneOfEntriesColorPreferenceOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: List[Value3]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef3  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectSecondaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef3]
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef3]


    class OneOfEntriesColorPreferenceOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: List[Value4]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef4  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectTertiaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef4]
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef4]


    class Entries84:
        # Object with an color and path preference
        primary_preference: Union[
            SdwanPolicyObjectPrimaryPreference1,
            SdwanPolicyObjectPrimaryPreference2,
        ]
        # Object with an color and path preference
        secondary_preference: Optional[
            SdwanPolicyObjectSecondaryPreference
        ]
        # Object with an color and path preference
        tertiary_preference: Optional[SdwanPolicyObjectTertiaryPreference]


    class Data124:
        # Preferred Color Group List
        entries: Optional[List[Entries84]]


    class EditDataPrefixProfileParcelForPolicyObjectPutRequest32:
        """
        preferred-color-group profile parcel schema for PUT request
        """

        data: Data124
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


