======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    LocalInterfaceDef = Literal["Cellular1/0", "GigabitEthernet0/0"]

    DefaultOptionTypeDef = Literal["default"]

    IkePhase1CipherSuiteDefaultDef = Literal["aes128-cbc-sha1"]

    IkePhase1CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]

    DiffeHellmanGroupDef = Literal["14", "15", "16", "19", "20", "21"]

    DiffeHellmanGroupDefaultDef = Literal["14"]

    IkePhase2CipherSuiteDefaultDef = Literal["aes128-sha1"]

    IkePhase2CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes128-sha1",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]

    VpnLocalInterfaceDef = Literal["Cellular1/0", "GigabitEthernet0/0"]

    VpnIkePhase1CipherSuiteDefaultDef = Literal["aes128-cbc-sha1"]

    VpnIkePhase1CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]

    VpnDiffeHellmanGroupDef = Literal["14", "15", "16", "19", "20", "21"]

    VpnDiffeHellmanGroupDefaultDef = Literal["14"]

    VpnIkePhase2CipherSuiteDefaultDef = Literal["aes128-sha1"]

    VpnIkePhase2CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes128-sha1",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]

    GlobalVpnLocalInterfaceDef = Literal[
        "Cellular1/0", "GigabitEthernet0/0"
    ]

    GlobalVpnIkePhase1CipherSuiteDefaultDef = Literal["aes128-cbc-sha1"]

    GlobalVpnIkePhase1CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]

    GlobalVpnDiffeHellmanGroupDef = Literal[
        "14", "15", "16", "19", "20", "21"
    ]

    GlobalVpnDiffeHellmanGroupDefaultDef = Literal["14"]

    GlobalVpnIkePhase2CipherSuiteDefaultDef = Literal["aes128-sha1"]

    GlobalVpnIkePhase2CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha256",
        "aes128-gcm",
        "aes128-sha1",
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-gcm",
    ]


    class OneOfTunnelNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelDescriptionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfListOfIpv4RemotePrivateSubnetsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfLocalPrivateSubnetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLocalPrivateSubnetOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class StaticLocalRemotePrivateSubnetDef:
        local_private_subnet: Union[
            OneOfLocalPrivateSubnetOptionsDef1,
            OneOfLocalPrivateSubnetOptionsDef2,
        ]
        remote_private_subnets: (
            OneOfListOfIpv4RemotePrivateSubnetsOptionsDef
        )


    class OneOfPresharedSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class OneOfTunnelDnsAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfLocalInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            LocalInterfaceDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSecondaryRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdIntervalOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdRetriesOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class TunnelRedundancyConfigDef:
        secondary_remote_public_ip: OneOfSecondaryRemotePublicIpOptionsDef
        dpd_interval: Optional[
            Union[
                OneOfDpdIntervalOptionsDef1, OneOfDpdIntervalOptionsDef2
            ]
        ]
        dpd_retries: Optional[
            Union[OneOfDpdRetriesOptionsDef1, OneOfDpdRetriesOptionsDef2]
        ]


    class VpnTunnelInfo:
        """
        Provide specific tunnel information
        """

        local_interface: OneOfLocalInterfaceOptionsDef
        name: OneOfTunnelNameOptionsDef
        pre_shared_secret: OneOfPresharedSecretOptionsDef
        remote_public_ip: OneOfRemotePublicIpOptionsDef
        description: Optional[OneOfTunnelDescriptionOptionsDef]
        private_subnets: Optional[StaticLocalRemotePrivateSubnetDef]
        tunnel_dns_address: Optional[OneOfTunnelDnsAddressOptionsDef]
        tunnel_redundancy_configuration: Optional[
            TunnelRedundancyConfigDef
        ]


    class OneOfIkePhase1CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: IkePhase1CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class OneOfIkePhase1CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: IkePhase1CipherSuiteDef


    class OneOfIkeVersionOptionsDef:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDiffeHellmanGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: DiffeHellmanGroupDef


    class OneOfDiffeHellmanGroupOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DiffeHellmanGroupDefaultDef  # pytype: disable=annotation-type-mismatch


    class OneOfRekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class IkePhase1:
        """
        IKE Phase 1
        """

        cipher_suite: Union[
            OneOfIkePhase1CipherSuiteOptionsDef1,
            OneOfIkePhase1CipherSuiteOptionsDef2,
        ]
        diffe_hellman_group: Union[
            OneOfDiffeHellmanGroupOptionsDef1,
            OneOfDiffeHellmanGroupOptionsDef2,
        ]
        ike_version: Optional[OneOfIkeVersionOptionsDef]
        rekey_timer: Optional[
            Union[OneOfRekeyTimerOptionsDef1, OneOfRekeyTimerOptionsDef2]
        ]


    class OneOfIkePhase2CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: IkePhase2CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class OneOfIkePhase2CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: IkePhase2CipherSuiteDef


    class OneOfIkePhase2RekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIkePhase2RekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class IpSecPolicy:
        """
        Provide IPSEC policy information
        """

        # IKE Phase 1
        ike_phase1: IkePhase1
        ike_phase2_cipher_suite: Union[
            OneOfIkePhase2CipherSuiteOptionsDef1,
            OneOfIkePhase2CipherSuiteOptionsDef2,
        ]
        ike_phase2_rekey_timer: Optional[
            Union[
                OneOfIkePhase2RekeyTimerOptionsDef1,
                OneOfIkePhase2RekeyTimerOptionsDef2,
            ]
        ]


    class VpnTunnels:
        # Provide IPSEC policy information
        ip_sec_policy: IpSecPolicy
        # Provide specific tunnel information
        vpn_tunnel_info: VpnTunnelInfo


    class VpnData:
        # Container to provide multiple VPN tunnels configurations
        vpn_tunnels: List[VpnTunnels]


    class Payload:
        """
        AON VPN profile parcel schema for POST request
        """

        data: VpnData
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
        # AON VPN profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListMobilityGlobalVpnPayload:
        data: Optional[List[Data]]


    class CreateVpnProfileParcelForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalVpnData:
        # Container to provide multiple VPN tunnels configurations
        vpn_tunnels: List[VpnTunnels]


    class CreateVpnProfileParcelForMobilityPostRequest:
        """
        AON VPN profile parcel schema for POST request
        """

        data: GlobalVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class VpnOneOfTunnelNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfTunnelDescriptionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfListOfIpv4RemotePrivateSubnetsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class VpnOneOfLocalPrivateSubnetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnStaticLocalRemotePrivateSubnetDef:
        local_private_subnet: Union[
            VpnOneOfLocalPrivateSubnetOptionsDef1,
            OneOfLocalPrivateSubnetOptionsDef2,
        ]
        remote_private_subnets: (
            VpnOneOfListOfIpv4RemotePrivateSubnetsOptionsDef
        )


    class VpnOneOfPresharedSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class VpnOneOfTunnelDnsAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class VpnOneOfLocalInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: VpnLocalInterfaceDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfSecondaryRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfDpdIntervalOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnOneOfDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfDpdRetriesOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnTunnelRedundancyConfigDef:
        secondary_remote_public_ip: (
            VpnOneOfSecondaryRemotePublicIpOptionsDef
        )
        dpd_interval: Optional[
            Union[
                VpnOneOfDpdIntervalOptionsDef1,
                VpnOneOfDpdIntervalOptionsDef2,
            ]
        ]
        dpd_retries: Optional[
            Union[
                VpnOneOfDpdRetriesOptionsDef1,
                VpnOneOfDpdRetriesOptionsDef2,
            ]
        ]


    class VpnVpnTunnelInfo:
        """
        Provide specific tunnel information
        """

        local_interface: VpnOneOfLocalInterfaceOptionsDef
        name: VpnOneOfTunnelNameOptionsDef
        pre_shared_secret: VpnOneOfPresharedSecretOptionsDef
        remote_public_ip: VpnOneOfRemotePublicIpOptionsDef
        description: Optional[VpnOneOfTunnelDescriptionOptionsDef]
        private_subnets: Optional[VpnStaticLocalRemotePrivateSubnetDef]
        tunnel_dns_address: Optional[VpnOneOfTunnelDnsAddressOptionsDef]
        tunnel_redundancy_configuration: Optional[
            VpnTunnelRedundancyConfigDef
        ]


    class VpnOneOfIkePhase1CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: VpnIkePhase1CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfIkePhase1CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnIkePhase1CipherSuiteDef


    class VpnOneOfIkeVersionOptionsDef:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnOneOfDiffeHellmanGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VpnDiffeHellmanGroupDef


    class VpnOneOfDiffeHellmanGroupOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: VpnDiffeHellmanGroupDefaultDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfRekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnIkePhase1:
        """
        IKE Phase 1
        """

        cipher_suite: Union[
            VpnOneOfIkePhase1CipherSuiteOptionsDef1,
            VpnOneOfIkePhase1CipherSuiteOptionsDef2,
        ]
        diffe_hellman_group: Union[
            VpnOneOfDiffeHellmanGroupOptionsDef1,
            VpnOneOfDiffeHellmanGroupOptionsDef2,
        ]
        ike_version: Optional[VpnOneOfIkeVersionOptionsDef]
        rekey_timer: Optional[
            Union[
                VpnOneOfRekeyTimerOptionsDef1,
                VpnOneOfRekeyTimerOptionsDef2,
            ]
        ]


    class VpnOneOfIkePhase2CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: VpnIkePhase2CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfIkePhase2CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnIkePhase2CipherSuiteDef


    class VpnOneOfIkePhase2RekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfIkePhase2RekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnIpSecPolicy:
        """
        Provide IPSEC policy information
        """

        # IKE Phase 1
        ike_phase1: VpnIkePhase1
        ike_phase2_cipher_suite: Union[
            VpnOneOfIkePhase2CipherSuiteOptionsDef1,
            VpnOneOfIkePhase2CipherSuiteOptionsDef2,
        ]
        ike_phase2_rekey_timer: Optional[
            Union[
                VpnOneOfIkePhase2RekeyTimerOptionsDef1,
                VpnOneOfIkePhase2RekeyTimerOptionsDef2,
            ]
        ]


    class VpnVpnTunnels:
        # Provide IPSEC policy information
        ip_sec_policy: VpnIpSecPolicy
        # Provide specific tunnel information
        vpn_tunnel_info: VpnVpnTunnelInfo


    class MobilityGlobalVpnData:
        # Container to provide multiple VPN tunnels configurations
        vpn_tunnels: List[VpnVpnTunnels]


    class VpnPayload:
        """
        AON VPN profile parcel schema for PUT request
        """

        data: MobilityGlobalVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalVpnPayload:
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
        # AON VPN profile parcel schema for PUT request
        payload: Optional[VpnPayload]


    class EditVpnProfileParcelForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class GlobalVpnOneOfTunnelNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVpnOneOfTunnelDescriptionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVpnOneOfListOfIpv4RemotePrivateSubnetsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class GlobalVpnOneOfLocalPrivateSubnetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVpnStaticLocalRemotePrivateSubnetDef:
        local_private_subnet: Union[
            GlobalVpnOneOfLocalPrivateSubnetOptionsDef1,
            OneOfLocalPrivateSubnetOptionsDef2,
        ]
        remote_private_subnets: (
            GlobalVpnOneOfListOfIpv4RemotePrivateSubnetsOptionsDef
        )


    class GlobalVpnOneOfPresharedSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVpnOneOfRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class GlobalVpnOneOfTunnelDnsAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class GlobalVpnOneOfLocalInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: GlobalVpnLocalInterfaceDef  # pytype: disable=annotation-type-mismatch


    class GlobalVpnOneOfSecondaryRemotePublicIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVpnOneOfDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVpnOneOfDpdIntervalOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVpnOneOfDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVpnOneOfDpdRetriesOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVpnTunnelRedundancyConfigDef:
        secondary_remote_public_ip: (
            GlobalVpnOneOfSecondaryRemotePublicIpOptionsDef
        )
        dpd_interval: Optional[
            Union[
                GlobalVpnOneOfDpdIntervalOptionsDef1,
                GlobalVpnOneOfDpdIntervalOptionsDef2,
            ]
        ]
        dpd_retries: Optional[
            Union[
                GlobalVpnOneOfDpdRetriesOptionsDef1,
                GlobalVpnOneOfDpdRetriesOptionsDef2,
            ]
        ]


    class GlobalVpnVpnTunnelInfo:
        """
        Provide specific tunnel information
        """

        local_interface: GlobalVpnOneOfLocalInterfaceOptionsDef
        name: GlobalVpnOneOfTunnelNameOptionsDef
        pre_shared_secret: GlobalVpnOneOfPresharedSecretOptionsDef
        remote_public_ip: GlobalVpnOneOfRemotePublicIpOptionsDef
        description: Optional[GlobalVpnOneOfTunnelDescriptionOptionsDef]
        private_subnets: Optional[
            GlobalVpnStaticLocalRemotePrivateSubnetDef
        ]
        tunnel_dns_address: Optional[
            GlobalVpnOneOfTunnelDnsAddressOptionsDef
        ]
        tunnel_redundancy_configuration: Optional[
            GlobalVpnTunnelRedundancyConfigDef
        ]


    class GlobalVpnOneOfIkePhase1CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: GlobalVpnIkePhase1CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class GlobalVpnOneOfIkePhase1CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: GlobalVpnIkePhase1CipherSuiteDef


    class GlobalVpnOneOfIkeVersionOptionsDef:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVpnOneOfDiffeHellmanGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalVpnDiffeHellmanGroupDef


    class GlobalVpnOneOfDiffeHellmanGroupOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: GlobalVpnDiffeHellmanGroupDefaultDef  # pytype: disable=annotation-type-mismatch


    class GlobalVpnOneOfRekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVpnOneOfRekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVpnIkePhase1:
        """
        IKE Phase 1
        """

        cipher_suite: Union[
            GlobalVpnOneOfIkePhase1CipherSuiteOptionsDef1,
            GlobalVpnOneOfIkePhase1CipherSuiteOptionsDef2,
        ]
        diffe_hellman_group: Union[
            GlobalVpnOneOfDiffeHellmanGroupOptionsDef1,
            GlobalVpnOneOfDiffeHellmanGroupOptionsDef2,
        ]
        ike_version: Optional[GlobalVpnOneOfIkeVersionOptionsDef]
        rekey_timer: Optional[
            Union[
                GlobalVpnOneOfRekeyTimerOptionsDef1,
                GlobalVpnOneOfRekeyTimerOptionsDef2,
            ]
        ]


    class GlobalVpnOneOfIkePhase2CipherSuiteOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: GlobalVpnIkePhase2CipherSuiteDefaultDef  # pytype: disable=annotation-type-mismatch


    class GlobalVpnOneOfIkePhase2CipherSuiteOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: GlobalVpnIkePhase2CipherSuiteDef


    class GlobalVpnOneOfIkePhase2RekeyTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVpnOneOfIkePhase2RekeyTimerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVpnIpSecPolicy:
        """
        Provide IPSEC policy information
        """

        # IKE Phase 1
        ike_phase1: GlobalVpnIkePhase1
        ike_phase2_cipher_suite: Union[
            GlobalVpnOneOfIkePhase2CipherSuiteOptionsDef1,
            GlobalVpnOneOfIkePhase2CipherSuiteOptionsDef2,
        ]
        ike_phase2_rekey_timer: Optional[
            Union[
                GlobalVpnOneOfIkePhase2RekeyTimerOptionsDef1,
                GlobalVpnOneOfIkePhase2RekeyTimerOptionsDef2,
            ]
        ]


    class GlobalVpnVpnTunnels:
        # Provide IPSEC policy information
        ip_sec_policy: GlobalVpnIpSecPolicy
        # Provide specific tunnel information
        vpn_tunnel_info: GlobalVpnVpnTunnelInfo


    class FeatureProfileMobilityGlobalVpnData:
        # Container to provide multiple VPN tunnels configurations
        vpn_tunnels: List[GlobalVpnVpnTunnels]


    class EditVpnProfileParcelForMobilityPutRequest:
        """
        AON VPN profile parcel schema for PUT request
        """

        data: FeatureProfileMobilityGlobalVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


