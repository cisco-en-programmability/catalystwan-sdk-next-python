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

    GlobalHttpAuthenticationDef = Literal["aaa", "local"]

    GlobalVersionDef = Literal["2"]

    SystemGlobalHttpAuthenticationDef = Literal["aaa", "local"]

    SystemGlobalVersionDef = Literal["2"]


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


    class OneOfNatUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatUdpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNatTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatTcpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatTcpTimeoutOptionsDef3:
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
        global_settings_nat_tcp_timeout: Optional[
            Union[
                OneOfNatTcpTimeoutOptionsDef1,
                OneOfNatTcpTimeoutOptionsDef2,
                OneOfNatTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat_udp_timeout: Optional[
            Union[
                OneOfNatUdpTimeoutOptionsDef1,
                OneOfNatUdpTimeoutOptionsDef2,
                OneOfNatUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                OneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
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
        Global settings feature schema for POST request
        """

        data: GlobalData
        name: str
        # Set the feature description
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
        # Global settings feature schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingSystemGlobalPayload:
        data: Optional[List[Data]]


    class CreateSdroutingGlobalSettingFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemGlobalData:
        services_global: ServicesGlobal


    class CreateSdroutingGlobalSettingFeaturePostRequest:
        """
        Global settings feature schema for POST request
        """

        data: SystemGlobalData
        name: str
        # Set the feature description
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


    class GlobalOneOfNatUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalOneOfNatUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalOneOfNatTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalOneOfNatTcpTimeoutOptionsDef3:
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
        global_settings_nat_tcp_timeout: Optional[
            Union[
                GlobalOneOfNatTcpTimeoutOptionsDef1,
                OneOfNatTcpTimeoutOptionsDef2,
                GlobalOneOfNatTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat_udp_timeout: Optional[
            Union[
                GlobalOneOfNatUdpTimeoutOptionsDef1,
                OneOfNatUdpTimeoutOptionsDef2,
                GlobalOneOfNatUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                GlobalOneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
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


    class SdRoutingSystemGlobalData:
        services_global: GlobalServicesGlobal


    class GlobalPayload:
        """
        Global settings feature schema for PUT request
        """

        data: SdRoutingSystemGlobalData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemGlobalPayload:
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
        # Global settings feature schema for PUT request
        payload: Optional[GlobalPayload]


    class EditSdroutingGlobalSettingFeaturePutResponse:
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


    class SystemGlobalOneOfNatUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemGlobalOneOfNatUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemGlobalOneOfNatTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemGlobalOneOfNatTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemGlobalOneOfHttpAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemGlobalHttpAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class SystemGlobalOneOfVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemGlobalVersionDef  # pytype: disable=annotation-type-mismatch


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
        global_settings_nat_tcp_timeout: Optional[
            Union[
                SystemGlobalOneOfNatTcpTimeoutOptionsDef1,
                OneOfNatTcpTimeoutOptionsDef2,
                SystemGlobalOneOfNatTcpTimeoutOptionsDef3,
            ]
        ]
        global_settings_nat_udp_timeout: Optional[
            Union[
                SystemGlobalOneOfNatUdpTimeoutOptionsDef1,
                OneOfNatUdpTimeoutOptionsDef2,
                SystemGlobalOneOfNatUdpTimeoutOptionsDef3,
            ]
        ]
        global_settings_ssh_version: Optional[
            Union[
                SystemGlobalOneOfVersionOptionsDef1,
                OneOfVersionOptionsDef2,
                OneOfVersionOptionsDef3,
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


    class FeatureProfileSdRoutingSystemGlobalData:
        services_global: SystemGlobalServicesGlobal


    class EditSdroutingGlobalSettingFeaturePutRequest:
        """
        Global settings feature schema for PUT request
        """

        data: FeatureProfileSdRoutingSystemGlobalData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


