======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    HttpAuthenticationDef = Literal["aaa", "local"]

    VersionDef = Literal["2"]

    EtherchannelFlowLbDef = Literal[
        "dst-ip",
        "dst-mac",
        "sdwan",
        "src-dst-ip",
        "src-dst-mac",
        "src-dst-mixed-ip-port",
        "src-ip",
        "src-mac",
    ]

    GlobalHttpAuthenticationDef = Literal["aaa", "local"]

    GlobalVersionDef = Literal["2"]

    GlobalEtherchannelFlowLbDef = Literal[
        "dst-ip",
        "dst-mac",
        "sdwan",
        "src-dst-ip",
        "src-dst-mac",
        "src-dst-mixed-ip-port",
        "src-ip",
        "src-mac",
    ]

    SystemGlobalHttpAuthenticationDef = Literal["aaa", "local"]

    SystemGlobalVersionDef = Literal["2"]

    SystemGlobalEtherchannelFlowLbDef = Literal[
        "dst-ip",
        "dst-mac",
        "sdwan",
        "src-dst-ip",
        "src-dst-mac",
        "src-dst-mixed-ip-port",
        "src-ip",
        "src-mac",
    ]


    class OneOfServerDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServerDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServerDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfServerDefaultTrueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServerDefaultTrueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServerDefaultTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfSourceInterfaceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSourceInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSourceInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfUdpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHttpAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: HttpAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class OneOfHttpAuthenticationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHttpAuthenticationOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VersionDef  # pytype: disable=annotation-type-mismatch


    class OneOfVersionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVersionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLacpSystemPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLacpSystemPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpSystemPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEtherchannelFlowLbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EtherchannelFlowLbDef


    class OneOfEtherchannelFlowLbOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEtherchannelFlowLbOptionsDef3:
        option_type: DefaultOptionTypeDef


    class ServicesIp:
        services_global_services_ip_arp_proxy: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_cdp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_domain_lookup: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_ftp_passive: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_http_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_https_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_line_vty: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_lldp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_rcmd: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        bgp_community_new_format: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        etherchannel_flow_load_balance: Optional[
            Union[
                OneOfEtherchannelFlowLbOptionsDef1,
                OneOfEtherchannelFlowLbOptionsDef2,
                OneOfEtherchannelFlowLbOptionsDef3,
            ]
        ]
        etherchannel_vlan_load_balance: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_console_logging: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ignore_bootp: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ip_source_route: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_snmp_ifindex_persist: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_in: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_out: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_udp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_vty_line_logging: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_settings_http_authentication: Optional[
            Union[
                OneOfHttpAuthenticationOptionsDef1,
                OneOfHttpAuthenticationOptionsDef2,
                OneOfHttpAuthenticationOptionsDef3,
            ]
        ]
        global_settings_nat64_tcp_timeout: Optional[
            Union[
                OneOfTcpTimeoutOptionsDef1,
                OneOfTcpTimeoutOptionsDef2,
                OneOfTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat64_udp_timeout: Optional[
            Union[
                OneOfUdpTimeoutOptionsDef1,
                OneOfUdpTimeoutOptionsDef2,
                OneOfUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                OneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
            ]
        ]
        lacp_system_priority: Optional[
            Union[
                OneOfLacpSystemPriorityOptionsDef1,
                OneOfLacpSystemPriorityOptionsDef2,
                OneOfLacpSystemPriorityOptionsDef3,
            ]
        ]
        services_global_services_ip_source_intrf: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]


    class ServicesGlobal:
        services_ip: ServicesIp


    class GlobalData:
        services_global: ServicesGlobal


    class Payload:
        """
        Global Services profile parcel schema for POST request
        """

        data: GlobalData
        name: str
        # Set the parcel description
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
        # Global Services profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemGlobalPayload:
        data: Optional[List[Data]]


    class CreateGlobalProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemGlobalData:
        services_global: ServicesGlobal


    class CreateGlobalProfileParcelForSystemPostRequest:
        """
        Global Services profile parcel schema for POST request
        """

        data: SystemGlobalData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GlobalOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalOneOfHttpAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalHttpAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class GlobalOneOfVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            GlobalVersionDef  # pytype: disable=annotation-type-mismatch
        )


    class GlobalOneOfLacpSystemPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalOneOfEtherchannelFlowLbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalEtherchannelFlowLbDef


    class GlobalServicesIp:
        services_global_services_ip_arp_proxy: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_cdp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_domain_lookup: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_ftp_passive: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_http_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_https_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_line_vty: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_lldp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_rcmd: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        bgp_community_new_format: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        etherchannel_flow_load_balance: Optional[
            Union[
                GlobalOneOfEtherchannelFlowLbOptionsDef1,
                OneOfEtherchannelFlowLbOptionsDef2,
                OneOfEtherchannelFlowLbOptionsDef3,
            ]
        ]
        etherchannel_vlan_load_balance: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_console_logging: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ignore_bootp: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ip_source_route: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_snmp_ifindex_persist: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_in: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_out: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_udp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_vty_line_logging: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_settings_http_authentication: Optional[
            Union[
                GlobalOneOfHttpAuthenticationOptionsDef1,
                OneOfHttpAuthenticationOptionsDef2,
                OneOfHttpAuthenticationOptionsDef3,
            ]
        ]
        global_settings_nat64_tcp_timeout: Optional[
            Union[
                GlobalOneOfTcpTimeoutOptionsDef1,
                OneOfTcpTimeoutOptionsDef2,
                GlobalOneOfTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat64_udp_timeout: Optional[
            Union[
                GlobalOneOfUdpTimeoutOptionsDef1,
                OneOfUdpTimeoutOptionsDef2,
                GlobalOneOfUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                GlobalOneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
            ]
        ]
        lacp_system_priority: Optional[
            Union[
                GlobalOneOfLacpSystemPriorityOptionsDef1,
                OneOfLacpSystemPriorityOptionsDef2,
                OneOfLacpSystemPriorityOptionsDef3,
            ]
        ]
        services_global_services_ip_source_intrf: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]


    class GlobalServicesGlobal:
        services_ip: GlobalServicesIp


    class SdwanSystemGlobalData:
        services_global: GlobalServicesGlobal


    class GlobalPayload:
        """
        Global Services profile parcel schema for PUT request
        """

        data: SdwanSystemGlobalData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemGlobalPayload:
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
        # Global Services profile parcel schema for PUT request
        payload: Optional[GlobalPayload]


    class EditGlobalProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemGlobalOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemGlobalOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemGlobalOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemGlobalOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemGlobalOneOfHttpAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemGlobalHttpAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class SystemGlobalOneOfVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemGlobalVersionDef  # pytype: disable=annotation-type-mismatch


    class SystemGlobalOneOfLacpSystemPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemGlobalOneOfEtherchannelFlowLbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemGlobalEtherchannelFlowLbDef


    class SystemGlobalServicesIp:
        services_global_services_ip_arp_proxy: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_cdp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_domain_lookup: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_ftp_passive: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_http_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_https_server: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_line_vty: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        services_global_services_ip_lldp: Union[
            OneOfServerDefaultTrueOptionsDef1,
            OneOfServerDefaultTrueOptionsDef2,
            OneOfServerDefaultTrueOptionsDef3,
        ]
        services_global_services_ip_rcmd: Union[
            OneOfServerDefaultFalseOptionsDef1,
            OneOfServerDefaultFalseOptionsDef2,
            OneOfServerDefaultFalseOptionsDef3,
        ]
        bgp_community_new_format: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        etherchannel_flow_load_balance: Optional[
            Union[
                SystemGlobalOneOfEtherchannelFlowLbOptionsDef1,
                OneOfEtherchannelFlowLbOptionsDef2,
                OneOfEtherchannelFlowLbOptionsDef3,
            ]
        ]
        etherchannel_vlan_load_balance: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_console_logging: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ignore_bootp: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_ip_source_route: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_snmp_ifindex_persist: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_in: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_keepalives_out: Optional[
            Union[
                OneOfServerDefaultTrueOptionsDef1,
                OneOfServerDefaultTrueOptionsDef2,
                OneOfServerDefaultTrueOptionsDef3,
            ]
        ]
        global_other_settings_tcp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_udp_small_servers: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_other_settings_vty_line_logging: Optional[
            Union[
                OneOfServerDefaultFalseOptionsDef1,
                OneOfServerDefaultFalseOptionsDef2,
                OneOfServerDefaultFalseOptionsDef3,
            ]
        ]
        global_settings_http_authentication: Optional[
            Union[
                SystemGlobalOneOfHttpAuthenticationOptionsDef1,
                OneOfHttpAuthenticationOptionsDef2,
                OneOfHttpAuthenticationOptionsDef3,
            ]
        ]
        global_settings_nat64_tcp_timeout: Optional[
            Union[
                SystemGlobalOneOfTcpTimeoutOptionsDef1,
                OneOfTcpTimeoutOptionsDef2,
                SystemGlobalOneOfTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat64_udp_timeout: Optional[
            Union[
                SystemGlobalOneOfUdpTimeoutOptionsDef1,
                OneOfUdpTimeoutOptionsDef2,
                SystemGlobalOneOfUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                SystemGlobalOneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
            ]
        ]
        lacp_system_priority: Optional[
            Union[
                SystemGlobalOneOfLacpSystemPriorityOptionsDef1,
                OneOfLacpSystemPriorityOptionsDef2,
                OneOfLacpSystemPriorityOptionsDef3,
            ]
        ]
        services_global_services_ip_source_intrf: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]


    class SystemGlobalServicesGlobal:
        services_ip: SystemGlobalServicesIp


    class FeatureProfileSdwanSystemGlobalData:
        services_global: SystemGlobalServicesGlobal


    class EditGlobalProfileParcelForSystemPutRequest:
        """
        Global Services profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemGlobalData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


