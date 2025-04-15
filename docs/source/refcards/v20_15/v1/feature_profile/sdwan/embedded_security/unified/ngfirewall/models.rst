======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

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

    NgfirewallDefaultActionTypeDef = Literal["drop", "pass"]

    NgfirewallSequencesBaseActionDef = Literal["drop", "inspect", "pass"]

    UnifiedNgfirewallValue = Literal[
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

    EmbeddedSecurityUnifiedNgfirewallValue = Literal[
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

    SdwanEmbeddedSecurityUnifiedNgfirewallValue = Literal[
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

    NgfirewallSequencesActionsTypeDef = Literal["connectionEvents", "log"]

    UnifiedNgfirewallDefaultActionTypeDef = Literal["drop", "pass"]

    UnifiedNgfirewallSequencesBaseActionDef = Literal[
        "drop", "inspect", "pass"
    ]

    FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallValue = Literal[
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

    V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallValue = Literal[
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

    Value1 = Literal[
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

    UnifiedNgfirewallSequencesActionsTypeDef = Literal[
        "connectionEvents", "log"
    ]


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


    class FqdnInputDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class FqdnMatchDef:
        fqdn_value: Union[FqdnInputDef1, FqdnInputDef2]


    class SourcePortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class SourcePortInputDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourcePortMatchDef:
        port_value: Union[SourcePortInputDef1, SourcePortInputDef2]


    class AppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class DestinationPortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]
        app: Optional[AppMatchDef]


    class DestinationPortInputDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class DestinationPortMatchDef:
        port_value: Union[
            DestinationPortInputDef1, DestinationPortInputDef2
        ]


    class GeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[Value]  # pytype: disable=annotation-type-mismatch


    class GeoLocationMatchDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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
            Union[GeoLocationMatchDef1, GeoLocationMatchDef2]
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
            Union[GeoLocationMatchDef1, GeoLocationMatchDef2]
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


    class NgfirewallData:
        default_action_type: OneOfDefaultActionTypeOptionsDef
        sequences: List[Sequences]


    class Payload:
        """
        ngfirewall profile feature schema for POST request
        """

        data: NgfirewallData
        description: str
        name: str
        contains_tls: Optional[bool]
        contains_utd: Optional[bool]
        metadata: Optional[Any]
        optimized: Optional[bool]


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
        # ngfirewall profile feature schema for POST request
        payload: Optional[Payload]


    class GetListSdwanEmbeddedSecurityUnifiedNgfirewallPayload:
        data: Optional[List[Data]]


    class CreateNgfirewallProfileParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class UnifiedNgfirewallData:
        default_action_type: OneOfDefaultActionTypeOptionsDef
        sequences: List[Sequences]


    class CreateNgfirewallProfileParcelPostRequest:
        """
        ngfirewall profile feature schema for POST request
        """

        data: UnifiedNgfirewallData
        description: str
        name: str
        contains_tls: Optional[bool]
        contains_utd: Optional[bool]
        metadata: Optional[Any]
        optimized: Optional[bool]


    class NgfirewallOneOfDefaultActionTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NgfirewallDefaultActionTypeDef


    class NgfirewallOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NgfirewallOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NgfirewallOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NgfirewallSequencesBaseActionDef


    class NgfirewallOneOfSequencesSequenceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class NgfirewallListDef:
        ref_id: NgfirewallRefIdArrayValue


    class UnifiedNgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallListDef:
        ref_id: UnifiedNgfirewallRefIdArrayValue


    class EmbeddedSecurityUnifiedNgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class EmbeddedSecurityUnifiedNgfirewallListDef:
        ref_id: EmbeddedSecurityUnifiedNgfirewallRefIdArrayValue


    class SdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SdwanEmbeddedSecurityUnifiedNgfirewallListDef:
        ref_id: SdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue


    class FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallListDef:
        ref_id: FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue


    class V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallListDef:
        ref_id: V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallRefIdArrayValue


    class RefIdArrayValue1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef1:
        ref_id: RefIdArrayValue1


    class RefIdArrayValue2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef2:
        ref_id: RefIdArrayValue2


    class RefIdArrayValue3:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef3:
        ref_id: RefIdArrayValue3


    class RefIdArrayValue4:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef4:
        ref_id: RefIdArrayValue4


    class RefIdArrayValue5:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef5:
        ref_id: RefIdArrayValue5


    class RefIdArrayValue6:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef6:
        ref_id: RefIdArrayValue6


    class RefIdArrayValue7:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef7:
        ref_id: RefIdArrayValue7


    class RefIdArrayValue8:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef8:
        ref_id: RefIdArrayValue8


    class RefIdArrayValue9:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef9:
        ref_id: RefIdArrayValue9


    class RefIdArrayValue10:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef10:
        ref_id: RefIdArrayValue10


    class NgfirewallIpv4MatchDef:
        ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2]


    class UnifiedNgfirewallIpv4MatchDef:
        ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2]


    class NgfirewallFqdnInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class NgfirewallFqdnMatchDef:
        fqdn_value: Union[NgfirewallFqdnInputDef1, FqdnInputDef2]


    class NgfirewallSourcePortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class NgfirewallSourcePortMatchDef:
        port_value: Union[
            NgfirewallSourcePortInputDef1, SourcePortInputDef2
        ]


    class NgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class NgfirewallDestinationPortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]
        app: Optional[NgfirewallAppMatchDef]


    class NgfirewallDestinationPortMatchDef:
        port_value: Union[
            NgfirewallDestinationPortInputDef1, DestinationPortInputDef2
        ]


    class NgfirewallGeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            UnifiedNgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedNgfirewallGeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            EmbeddedSecurityUnifiedNgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class NgfirewallIdentityUserMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class NgfirewallIdentityUsergroupMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class EmbeddedSecurityUnifiedNgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class NgfirewallProtocolMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]
        app: Optional[SdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef]


    class NgfirewallProtocolNameMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[
            SdwanEmbeddedSecurityUnifiedNgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class NgfirewallEntries:
        app: Optional[UnifiedNgfirewallAppMatchDef]
        app_family: Optional[EmbeddedSecurityUnifiedNgfirewallAppMatchDef]
        app_list: Optional[ListDef6]
        app_list_flat: Optional[ListDef7]
        destination_data_prefix_list: Optional[UnifiedNgfirewallListDef]
        destination_fqdn: Optional[NgfirewallFqdnMatchDef]
        destination_fqdn_list: Optional[
            EmbeddedSecurityUnifiedNgfirewallListDef
        ]
        destination_geo_location: Optional[
            Union[
                UnifiedNgfirewallGeoLocationMatchDef1,
                GeoLocationMatchDef2,
            ]
        ]
        destination_geo_location_list: Optional[
            FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallListDef
        ]
        destination_ip: Optional[UnifiedNgfirewallIpv4MatchDef]
        destination_port: Optional[NgfirewallDestinationPortMatchDef]
        destination_port_list: Optional[ListDef1]
        destination_scalable_group_tag_list: Optional[ListDef3]
        destination_security_group: Optional[ListDef10]
        protocol: Optional[NgfirewallProtocolMatchDef]
        protocol_name: Optional[NgfirewallProtocolNameMatchDef]
        protocol_name_list: Optional[ListDef5]
        rule_set_list: Optional[ListDef8]
        source_data_prefix_list: Optional[NgfirewallListDef]
        source_geo_location: Optional[
            Union[NgfirewallGeoLocationMatchDef1, GeoLocationMatchDef2]
        ]
        source_geo_location_list: Optional[
            SdwanEmbeddedSecurityUnifiedNgfirewallListDef
        ]
        source_identity_list: Optional[ListDef4]
        source_identity_user: Optional[NgfirewallIdentityUserMatchDef]
        source_identity_usergroup: Optional[
            NgfirewallIdentityUsergroupMatchDef
        ]
        source_ip: Optional[NgfirewallIpv4MatchDef]
        source_port: Optional[NgfirewallSourcePortMatchDef]
        source_port_list: Optional[
            V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallListDef
        ]
        source_scalable_group_tag_list: Optional[ListDef2]
        source_security_group: Optional[ListDef9]


    class NgfirewallMatch:
        entries: List[NgfirewallEntries]


    class NgfirewallOneOfSequencesActionsTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NgfirewallSequencesActionsTypeDef  # pytype: disable=annotation-type-mismatch


    class NgfirewallOneOfSequencesActionsParameterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NgfirewallActions1:
        parameter: NgfirewallOneOfSequencesActionsParameterOptionsDef
        type_: NgfirewallOneOfSequencesActionsTypeOptionsDef


    class NgfirewallSequences:
        # can be empty array or with type or parameter
        actions: List[Union[NgfirewallActions1, Actions2]]
        base_action: NgfirewallOneOfSequencesBaseActionOptionsDef
        match_: NgfirewallMatch
        sequence_id: NgfirewallOneOfSequencesSequenceIdOptionsDef
        sequence_name: NgfirewallOneOfSequencesSequenceNameOptionsDef
        sequence_type: NgfirewallOneOfSequencesSequenceTypeOptionsDef
        disable_sequence: Optional[OneOfdisableSequenceDef]


    class EmbeddedSecurityUnifiedNgfirewallData:
        default_action_type: NgfirewallOneOfDefaultActionTypeOptionsDef
        sequences: List[NgfirewallSequences]


    class NgfirewallPayload:
        """
        ngfirewall profile feature schema for PUT request
        """

        data: EmbeddedSecurityUnifiedNgfirewallData
        description: str
        name: str
        contains_tls: Optional[bool]
        contains_utd: Optional[bool]
        metadata: Optional[Any]
        optimized: Optional[bool]


    class GetSingleSdwanEmbeddedSecurityUnifiedNgfirewallPayload:
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
        # ngfirewall profile feature schema for PUT request
        payload: Optional[NgfirewallPayload]


    class EditNgfirewallProfileParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class UnifiedNgfirewallOneOfDefaultActionTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedNgfirewallDefaultActionTypeDef


    class UnifiedNgfirewallOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedNgfirewallOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedNgfirewallOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedNgfirewallSequencesBaseActionDef


    class UnifiedNgfirewallOneOfSequencesSequenceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdArrayValue11:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef11:
        ref_id: RefIdArrayValue11


    class RefIdArrayValue12:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef12:
        ref_id: RefIdArrayValue12


    class RefIdArrayValue13:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef13:
        ref_id: RefIdArrayValue13


    class RefIdArrayValue14:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef14:
        ref_id: RefIdArrayValue14


    class RefIdArrayValue15:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef15:
        ref_id: RefIdArrayValue15


    class RefIdArrayValue16:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef16:
        ref_id: RefIdArrayValue16


    class RefIdArrayValue17:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef17:
        ref_id: RefIdArrayValue17


    class RefIdArrayValue18:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef18:
        ref_id: RefIdArrayValue18


    class RefIdArrayValue19:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef19:
        ref_id: RefIdArrayValue19


    class RefIdArrayValue20:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef20:
        ref_id: RefIdArrayValue20


    class RefIdArrayValue21:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef21:
        ref_id: RefIdArrayValue21


    class RefIdArrayValue22:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef22:
        ref_id: RefIdArrayValue22


    class RefIdArrayValue23:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef23:
        ref_id: RefIdArrayValue23


    class RefIdArrayValue24:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef24:
        ref_id: RefIdArrayValue24


    class RefIdArrayValue25:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef25:
        ref_id: RefIdArrayValue25


    class RefIdArrayValue26:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class ListDef26:
        ref_id: RefIdArrayValue26


    class EmbeddedSecurityUnifiedNgfirewallIpv4MatchDef:
        ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2]


    class SdwanEmbeddedSecurityUnifiedNgfirewallIpv4MatchDef:
        ipv4_value: Union[Ipv4InputDef1, Ipv4InputDef2]


    class UnifiedNgfirewallFqdnInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallFqdnMatchDef:
        fqdn_value: Union[UnifiedNgfirewallFqdnInputDef1, FqdnInputDef2]


    class UnifiedNgfirewallSourcePortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class UnifiedNgfirewallSourcePortMatchDef:
        port_value: Union[
            UnifiedNgfirewallSourcePortInputDef1, SourcePortInputDef2
        ]


    class FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallDestinationPortInputDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]
        app: Optional[
            FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef
        ]


    class UnifiedNgfirewallDestinationPortMatchDef:
        port_value: Union[
            UnifiedNgfirewallDestinationPortInputDef1,
            DestinationPortInputDef2,
        ]


    class EmbeddedSecurityUnifiedNgfirewallGeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class SdwanEmbeddedSecurityUnifiedNgfirewallGeoLocationMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallValue
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedNgfirewallIdentityUserMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallIdentityUsergroupMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AppMatchDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AppMatchDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedNgfirewallProtocolMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[str]
        app: Optional[AppMatchDef2]


    class UnifiedNgfirewallProtocolNameMatchDef:
        option_type: GlobalOptionTypeDef
        value: List[Value1]  # pytype: disable=annotation-type-mismatch


    class UnifiedNgfirewallEntries:
        app: Optional[
            V1FeatureProfileSdwanEmbeddedSecurityUnifiedNgfirewallAppMatchDef
        ]
        app_family: Optional[AppMatchDef1]
        app_list: Optional[ListDef22]
        app_list_flat: Optional[ListDef23]
        destination_data_prefix_list: Optional[ListDef12]
        destination_fqdn: Optional[UnifiedNgfirewallFqdnMatchDef]
        destination_fqdn_list: Optional[ListDef13]
        destination_geo_location: Optional[
            Union[
                SdwanEmbeddedSecurityUnifiedNgfirewallGeoLocationMatchDef1,
                GeoLocationMatchDef2,
            ]
        ]
        destination_geo_location_list: Optional[ListDef15]
        destination_ip: Optional[
            SdwanEmbeddedSecurityUnifiedNgfirewallIpv4MatchDef
        ]
        destination_port: Optional[
            UnifiedNgfirewallDestinationPortMatchDef
        ]
        destination_port_list: Optional[ListDef17]
        destination_scalable_group_tag_list: Optional[ListDef19]
        destination_security_group: Optional[ListDef26]
        protocol: Optional[UnifiedNgfirewallProtocolMatchDef]
        protocol_name: Optional[UnifiedNgfirewallProtocolNameMatchDef]
        protocol_name_list: Optional[ListDef21]
        rule_set_list: Optional[ListDef24]
        source_data_prefix_list: Optional[ListDef11]
        source_geo_location: Optional[
            Union[
                EmbeddedSecurityUnifiedNgfirewallGeoLocationMatchDef1,
                GeoLocationMatchDef2,
            ]
        ]
        source_geo_location_list: Optional[ListDef14]
        source_identity_list: Optional[ListDef20]
        source_identity_user: Optional[
            UnifiedNgfirewallIdentityUserMatchDef
        ]
        source_identity_usergroup: Optional[
            UnifiedNgfirewallIdentityUsergroupMatchDef
        ]
        source_ip: Optional[EmbeddedSecurityUnifiedNgfirewallIpv4MatchDef]
        source_port: Optional[UnifiedNgfirewallSourcePortMatchDef]
        source_port_list: Optional[ListDef16]
        source_scalable_group_tag_list: Optional[ListDef18]
        source_security_group: Optional[ListDef25]


    class UnifiedNgfirewallMatch:
        entries: List[UnifiedNgfirewallEntries]


    class UnifiedNgfirewallOneOfSequencesActionsTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedNgfirewallSequencesActionsTypeDef  # pytype: disable=annotation-type-mismatch


    class UnifiedNgfirewallOneOfSequencesActionsParameterOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedNgfirewallActions1:
        parameter: (
            UnifiedNgfirewallOneOfSequencesActionsParameterOptionsDef
        )
        type_: UnifiedNgfirewallOneOfSequencesActionsTypeOptionsDef


    class UnifiedNgfirewallSequences:
        # can be empty array or with type or parameter
        actions: List[Union[UnifiedNgfirewallActions1, Actions2]]
        base_action: UnifiedNgfirewallOneOfSequencesBaseActionOptionsDef
        match_: UnifiedNgfirewallMatch
        sequence_id: UnifiedNgfirewallOneOfSequencesSequenceIdOptionsDef
        sequence_name: (
            UnifiedNgfirewallOneOfSequencesSequenceNameOptionsDef
        )
        sequence_type: (
            UnifiedNgfirewallOneOfSequencesSequenceTypeOptionsDef
        )
        disable_sequence: Optional[OneOfdisableSequenceDef]


    class SdwanEmbeddedSecurityUnifiedNgfirewallData:
        default_action_type: (
            UnifiedNgfirewallOneOfDefaultActionTypeOptionsDef
        )
        sequences: List[UnifiedNgfirewallSequences]


    class EditNgfirewallProfileParcelPutRequest:
        """
        ngfirewall profile feature schema for PUT request
        """

        data: SdwanEmbeddedSecurityUnifiedNgfirewallData
        description: str
        name: str
        contains_tls: Optional[bool]
        contains_utd: Optional[bool]
        metadata: Optional[Any]
        optimized: Optional[bool]


