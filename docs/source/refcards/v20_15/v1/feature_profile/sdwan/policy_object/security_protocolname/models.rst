======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]

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


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesProtocolNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesProtocolNameDef  # pytype: disable=annotation-type-mismatch


    class Entries:
        protocol_name: OneOfEntriesProtocolNameOptionsDef


    class Data:
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-protocolname profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for security-protocolname profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # security-protocolname profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


