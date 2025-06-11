======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    IpsecReplayWindowDef = Literal["1024", "128", "256", "512", "64"]

    DefaultIpsecReplayWindowDef = Literal["64"]

    BooleanFalseDef = Literal[False]

    PfsGroupDef = Literal["14", "15", "16", "19", "20", "21"]

    DefaultPfsGroupDef = Literal["16"]

    SignatureTypeDef = Literal["ECDSA", "RSA"]

    DefaultSignatureTypeDef = Literal["RSA"]


    class OneOfDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDpdIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDpdRetryIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdRetryIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDpdRetryIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIkeSaLifeTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIkeSaLifeTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeSaLifeTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIkeV2LocalIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIpv6NextHopAddressOptionsWithOutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6NextHopAddressOptionsWithOutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIkeV2LocalIdentityOptionsDef2:
        ipv6_addr: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]


    class OneOfIdentityValueFqdnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueFqdnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV2LocalIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIdentityValueEmailOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueEmailOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV2LocalIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIdentityValueKeyIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueKeyIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV2LocalIdentityOptionsDef5:
        key_id: Union[
            OneOfIdentityValueKeyIdOptionsDef1,
            OneOfIdentityValueKeyIdOptionsDef2,
        ]


    class RemoteIdentities1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class RemoteIdentities2:
        ipv6_prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class RemoteIdentities3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class RemoteIdentities4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class RemoteIdentities5:
        key_id: Union[
            OneOfIdentityValueKeyIdOptionsDef1,
            OneOfIdentityValueKeyIdOptionsDef2,
        ]


    class OneOfIpsecSaLifeTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpsecSaLifeTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecSaLifeTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IpsecReplayWindowDef


    class OneOfIpsecReplayWindowOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecReplayWindowOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpsecReplayWindowDef  # pytype: disable=annotation-type-mismatch


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfPfsGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PfsGroupDef


    class OneOfPfsGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPfsGroupOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultPfsGroupDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfPreSharedKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPreSharedKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV2AuthConfigOptionsDef1:
        group_psk: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]


    class OneOfKeyringPeerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PeerIPv4AddressOrSubnetMaskOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class PeerIPv4AddressOrSubnetMaskOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkev2KeyringPeerAddressOptionsDef1:
        ipv4_address_or_subnet: Union[
            PeerIPv4AddressOrSubnetMaskOptionsDef1,
            PeerIPv4AddressOrSubnetMaskOptionsDef2,
        ]


    class OneOfIkev2KeyringPeerAddressOptionsDef2:
        ipv6_prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class OneOfIkev2KeyringPeerAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfKeyringPeerHostNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeyringPeerHostNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyringPeerHostNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIPeerIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIPeerIdentityOptionsDef2:
        ipv6_addr: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]


    class OneOfIPeerIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIPeerIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIPeerIdentityOptionsDef5:
        key_id: Union[
            OneOfIdentityValueKeyIdOptionsDef1,
            OneOfIdentityValueKeyIdOptionsDef2,
        ]


    class OneOfIPeerIdentityOptionsDef6:
        option_type: DefaultOptionTypeDef


    class Peers1:
        address_config: Union[
            OneOfIkev2KeyringPeerAddressOptionsDef1,
            OneOfIkev2KeyringPeerAddressOptionsDef2,
            OneOfIkev2KeyringPeerAddressOptionsDef3,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        host_name: Optional[
            Union[
                OneOfKeyringPeerHostNameOptionsDef1,
                OneOfKeyringPeerHostNameOptionsDef2,
                OneOfKeyringPeerHostNameOptionsDef3,
            ]
        ]
        identity: Optional[
            Union[
                OneOfIPeerIdentityOptionsDef1,
                OneOfIPeerIdentityOptionsDef2,
                OneOfIPeerIdentityOptionsDef3,
                OneOfIPeerIdentityOptionsDef4,
                OneOfIPeerIdentityOptionsDef5,
                OneOfIPeerIdentityOptionsDef6,
            ]
        ]


    class Peers2:
        host_name: Union[
            OneOfKeyringPeerHostNameOptionsDef1,
            OneOfKeyringPeerHostNameOptionsDef2,
            OneOfKeyringPeerHostNameOptionsDef3,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        address_config: Optional[
            Union[
                OneOfIkev2KeyringPeerAddressOptionsDef1,
                OneOfIkev2KeyringPeerAddressOptionsDef2,
                OneOfIkev2KeyringPeerAddressOptionsDef3,
            ]
        ]
        identity: Optional[
            Union[
                OneOfIPeerIdentityOptionsDef1,
                OneOfIPeerIdentityOptionsDef2,
                OneOfIPeerIdentityOptionsDef3,
                OneOfIPeerIdentityOptionsDef4,
                OneOfIPeerIdentityOptionsDef5,
                OneOfIPeerIdentityOptionsDef6,
            ]
        ]


    class Peers3:
        identity: Union[
            OneOfIPeerIdentityOptionsDef1,
            OneOfIPeerIdentityOptionsDef2,
            OneOfIPeerIdentityOptionsDef3,
            OneOfIPeerIdentityOptionsDef4,
            OneOfIPeerIdentityOptionsDef5,
            OneOfIPeerIdentityOptionsDef6,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        address_config: Optional[
            Union[
                OneOfIkev2KeyringPeerAddressOptionsDef1,
                OneOfIkev2KeyringPeerAddressOptionsDef2,
                OneOfIkev2KeyringPeerAddressOptionsDef3,
            ]
        ]
        host_name: Optional[
            Union[
                OneOfKeyringPeerHostNameOptionsDef1,
                OneOfKeyringPeerHostNameOptionsDef2,
                OneOfKeyringPeerHostNameOptionsDef3,
            ]
        ]


    class Peers4:
        address_config: Union[
            OneOfIkev2KeyringPeerAddressOptionsDef1,
            OneOfIkev2KeyringPeerAddressOptionsDef2,
            OneOfIkev2KeyringPeerAddressOptionsDef3,
        ]
        host_name: Union[
            OneOfKeyringPeerHostNameOptionsDef1,
            OneOfKeyringPeerHostNameOptionsDef2,
            OneOfKeyringPeerHostNameOptionsDef3,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        identity: Optional[
            Union[
                OneOfIPeerIdentityOptionsDef1,
                OneOfIPeerIdentityOptionsDef2,
                OneOfIPeerIdentityOptionsDef3,
                OneOfIPeerIdentityOptionsDef4,
                OneOfIPeerIdentityOptionsDef5,
                OneOfIPeerIdentityOptionsDef6,
            ]
        ]


    class Peers5:
        address_config: Union[
            OneOfIkev2KeyringPeerAddressOptionsDef1,
            OneOfIkev2KeyringPeerAddressOptionsDef2,
            OneOfIkev2KeyringPeerAddressOptionsDef3,
        ]
        identity: Union[
            OneOfIPeerIdentityOptionsDef1,
            OneOfIPeerIdentityOptionsDef2,
            OneOfIPeerIdentityOptionsDef3,
            OneOfIPeerIdentityOptionsDef4,
            OneOfIPeerIdentityOptionsDef5,
            OneOfIPeerIdentityOptionsDef6,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        host_name: Optional[
            Union[
                OneOfKeyringPeerHostNameOptionsDef1,
                OneOfKeyringPeerHostNameOptionsDef2,
                OneOfKeyringPeerHostNameOptionsDef3,
            ]
        ]


    class Peers6:
        host_name: Union[
            OneOfKeyringPeerHostNameOptionsDef1,
            OneOfKeyringPeerHostNameOptionsDef2,
            OneOfKeyringPeerHostNameOptionsDef3,
        ]
        identity: Union[
            OneOfIPeerIdentityOptionsDef1,
            OneOfIPeerIdentityOptionsDef2,
            OneOfIPeerIdentityOptionsDef3,
            OneOfIPeerIdentityOptionsDef4,
            OneOfIPeerIdentityOptionsDef5,
            OneOfIPeerIdentityOptionsDef6,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]
        address_config: Optional[
            Union[
                OneOfIkev2KeyringPeerAddressOptionsDef1,
                OneOfIkev2KeyringPeerAddressOptionsDef2,
                OneOfIkev2KeyringPeerAddressOptionsDef3,
            ]
        ]


    class Peers7:
        address_config: Union[
            OneOfIkev2KeyringPeerAddressOptionsDef1,
            OneOfIkev2KeyringPeerAddressOptionsDef2,
            OneOfIkev2KeyringPeerAddressOptionsDef3,
        ]
        host_name: Union[
            OneOfKeyringPeerHostNameOptionsDef1,
            OneOfKeyringPeerHostNameOptionsDef2,
            OneOfKeyringPeerHostNameOptionsDef3,
        ]
        identity: Union[
            OneOfIPeerIdentityOptionsDef1,
            OneOfIPeerIdentityOptionsDef2,
            OneOfIPeerIdentityOptionsDef3,
            OneOfIPeerIdentityOptionsDef4,
            OneOfIPeerIdentityOptionsDef5,
            OneOfIPeerIdentityOptionsDef6,
        ]
        peer_name: OneOfKeyringPeerNameOptionsDef
        pre_shared_key: Union[
            OneOfPreSharedKeyOptionsDef1, OneOfPreSharedKeyOptionsDef2
        ]


    class PerPeerPskAuth:
        """
        Per-peer pre-shared key authentication, different peer use different key
        """

        # PSK authentication for different peers, peerName and preSharedKey are mandatory,addressConfig, hostName and identity at least configure one.
        peers: List[
            Union[Peers1, Peers2, Peers3, Peers4, Peers5, Peers6, Peers7]
        ]


    class OneOfIkeV2AuthConfigOptionsDef2:
        # Per-peer pre-shared key authentication, different peer use different key
        per_peer_psk_auth: PerPeerPskAuth


    class OneOfTrustPointNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTrustPointNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSignatureTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            SignatureTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSignatureTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSignatureTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultSignatureTypeDef  # pytype: disable=annotation-type-mismatch


    class EnterpriseCaAuth:
        """
        Enterprise CA authentication
        """

        trust_point: Union[
            OneOfTrustPointNameOptionsDef1, OneOfTrustPointNameOptionsDef2
        ]
        signature_type: Optional[
            Union[
                OneOfSignatureTypeOptionsDef1,
                OneOfSignatureTypeOptionsDef2,
                OneOfSignatureTypeOptionsDef3,
            ]
        ]


    class OneOfIkeV2AuthConfigOptionsDef3:
        # Enterprise CA authentication
        enterprise_ca_auth: EnterpriseCaAuth


    class IpsecProfileData:
        """
        IKEv2 and IPSec profile config parameters
        """

        auth_config: Union[
            OneOfIkeV2AuthConfigOptionsDef1,
            OneOfIkeV2AuthConfigOptionsDef2,
            OneOfIkeV2AuthConfigOptionsDef3,
        ]
        dpd_keep_alive_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retry_interval: Union[
            OneOfDpdRetryIntervalOptionsDef1,
            OneOfDpdRetryIntervalOptionsDef2,
            OneOfDpdRetryIntervalOptionsDef3,
        ]
        ike_sa_life_time: Union[
            OneOfIkeSaLifeTimeOptionsDef1,
            OneOfIkeSaLifeTimeOptionsDef2,
            OneOfIkeSaLifeTimeOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipsec_sa_life_time: Union[
            OneOfIpsecSaLifeTimeOptionsDef1,
            OneOfIpsecSaLifeTimeOptionsDef2,
            OneOfIpsecSaLifeTimeOptionsDef3,
        ]
        local_identity: Union[
            OneOfIkeV2LocalIdentityOptionsDef1,
            OneOfIkeV2LocalIdentityOptionsDef2,
            OneOfIkeV2LocalIdentityOptionsDef3,
            OneOfIkeV2LocalIdentityOptionsDef4,
            OneOfIkeV2LocalIdentityOptionsDef5,
        ]
        pfs_enabled: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        # IKE matched remote identity list, at least one configured
        remote_identities: List[
            Union[
                RemoteIdentities1,
                RemoteIdentities2,
                RemoteIdentities3,
                RemoteIdentities4,
                RemoteIdentities5,
            ]
        ]
        pfs_group: Optional[
            Union[
                OneOfPfsGroupOptionsDef1,
                OneOfPfsGroupOptionsDef2,
                OneOfPfsGroupOptionsDef3,
            ]
        ]


    class Payload:
        """
        SD-Routing IPsec profile feature schema
        """

        # IKEv2 and IPSec profile config parameters
        data: IpsecProfileData
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
        # SD-Routing IPsec profile feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceIpsecProfilePayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceIpsecProfileFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ServiceIpsecProfileData:
        """
        IKEv2 and IPSec profile config parameters
        """

        auth_config: Union[
            OneOfIkeV2AuthConfigOptionsDef1,
            OneOfIkeV2AuthConfigOptionsDef2,
            OneOfIkeV2AuthConfigOptionsDef3,
        ]
        dpd_keep_alive_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retry_interval: Union[
            OneOfDpdRetryIntervalOptionsDef1,
            OneOfDpdRetryIntervalOptionsDef2,
            OneOfDpdRetryIntervalOptionsDef3,
        ]
        ike_sa_life_time: Union[
            OneOfIkeSaLifeTimeOptionsDef1,
            OneOfIkeSaLifeTimeOptionsDef2,
            OneOfIkeSaLifeTimeOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipsec_sa_life_time: Union[
            OneOfIpsecSaLifeTimeOptionsDef1,
            OneOfIpsecSaLifeTimeOptionsDef2,
            OneOfIpsecSaLifeTimeOptionsDef3,
        ]
        local_identity: Union[
            OneOfIkeV2LocalIdentityOptionsDef1,
            OneOfIkeV2LocalIdentityOptionsDef2,
            OneOfIkeV2LocalIdentityOptionsDef3,
            OneOfIkeV2LocalIdentityOptionsDef4,
            OneOfIkeV2LocalIdentityOptionsDef5,
        ]
        pfs_enabled: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        # IKE matched remote identity list, at least one configured
        remote_identities: List[
            Union[
                RemoteIdentities1,
                RemoteIdentities2,
                RemoteIdentities3,
                RemoteIdentities4,
                RemoteIdentities5,
            ]
        ]
        pfs_group: Optional[
            Union[
                OneOfPfsGroupOptionsDef1,
                OneOfPfsGroupOptionsDef2,
                OneOfPfsGroupOptionsDef3,
            ]
        ]


    class CreateSdroutingServiceIpsecProfileFeaturePostRequest:
        """
        SD-Routing IPsec profile feature schema
        """

        # IKEv2 and IPSec profile config parameters
        data: ServiceIpsecProfileData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingServiceIpsecProfilePayload:
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
        # SD-Routing IPsec profile feature schema
        payload: Optional[Payload]


    class EditSdroutingServiceIpsecProfileFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingServiceIpsecProfileData:
        """
        IKEv2 and IPSec profile config parameters
        """

        auth_config: Union[
            OneOfIkeV2AuthConfigOptionsDef1,
            OneOfIkeV2AuthConfigOptionsDef2,
            OneOfIkeV2AuthConfigOptionsDef3,
        ]
        dpd_keep_alive_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retry_interval: Union[
            OneOfDpdRetryIntervalOptionsDef1,
            OneOfDpdRetryIntervalOptionsDef2,
            OneOfDpdRetryIntervalOptionsDef3,
        ]
        ike_sa_life_time: Union[
            OneOfIkeSaLifeTimeOptionsDef1,
            OneOfIkeSaLifeTimeOptionsDef2,
            OneOfIkeSaLifeTimeOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipsec_sa_life_time: Union[
            OneOfIpsecSaLifeTimeOptionsDef1,
            OneOfIpsecSaLifeTimeOptionsDef2,
            OneOfIpsecSaLifeTimeOptionsDef3,
        ]
        local_identity: Union[
            OneOfIkeV2LocalIdentityOptionsDef1,
            OneOfIkeV2LocalIdentityOptionsDef2,
            OneOfIkeV2LocalIdentityOptionsDef3,
            OneOfIkeV2LocalIdentityOptionsDef4,
            OneOfIkeV2LocalIdentityOptionsDef5,
        ]
        pfs_enabled: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        # IKE matched remote identity list, at least one configured
        remote_identities: List[
            Union[
                RemoteIdentities1,
                RemoteIdentities2,
                RemoteIdentities3,
                RemoteIdentities4,
                RemoteIdentities5,
            ]
        ]
        pfs_group: Optional[
            Union[
                OneOfPfsGroupOptionsDef1,
                OneOfPfsGroupOptionsDef2,
                OneOfPfsGroupOptionsDef3,
            ]
        ]


    class EditSdroutingServiceIpsecProfileFeaturePutRequest:
        """
        SD-Routing IPsec profile feature schema
        """

        # IKEv2 and IPSec profile config parameters
        data: SdRoutingServiceIpsecProfileData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


