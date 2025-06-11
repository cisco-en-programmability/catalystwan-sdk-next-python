======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

    SsidRadioTypeDef = Literal["24ghz", "5ghz", "all"]

    DefaultSsidRadioTypeDef = Literal["all"]

    SsidQosProfileDef = Literal["bronze", "gold", "platinum", "silver"]

    DefaultSsidQosProfileDef = Literal["silver"]

    CountryDef = Literal[
        "AE",
        "AR",
        "AT",
        "AU",
        "BA",
        "BB",
        "BE",
        "BG",
        "BH",
        "BN",
        "BO",
        "BR",
        "BY",
        "CA",
        "CA2",
        "CH",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CY",
        "CZ",
        "DE",
        "DK",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "ES",
        "FI",
        "FJ",
        "FR",
        "GB",
        "GH",
        "GI",
        "GR",
        "HK",
        "HR",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IO",
        "IQ",
        "IS",
        "IT",
        "J2",
        "J4",
        "JM",
        "JO",
        "KE",
        "KN",
        "KW",
        "KZ",
        "LB",
        "LI",
        "LK",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "ME",
        "MK",
        "MN",
        "MO",
        "MT",
        "MX",
        "MY",
        "NL",
        "NO",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PH",
        "PH2",
        "PK",
        "PL",
        "PR",
        "PT",
        "PY",
        "QA",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "TH",
        "TN",
        "TR",
        "TW",
        "UA",
        "US",
        "UY",
        "VE",
        "VN",
        "ZA",
    ]

    OptionType = Literal["default", "global"]

    BooleanFalseDef = Literal[False]

    Ipv4SubnetMaskDef = Literal[
        "0.0.0.0",
        "128.0.0.0",
        "192.0.0.0",
        "224.0.0.0",
        "240.0.0.0",
        "248.0.0.0",
        "252.0.0.0",
        "254.0.0.0",
        "255.0.0.0",
        "255.128.0.0",
        "255.192.0.0",
        "255.224.0.0",
        "255.240.0.0",
        "255.252.0.0",
        "255.254.0.0",
        "255.255.0.0",
        "255.255.128.0",
        "255.255.192.0",
        "255.255.224.0",
        "255.255.240.0",
        "255.255.248.0",
        "255.255.252.0",
        "255.255.254.0",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
        "255.255.255.254",
        "255.255.255.255",
    ]

    WirelesslanSsidRadioTypeDef = Literal["24ghz", "5ghz", "all"]

    WirelesslanDefaultSsidRadioTypeDef = Literal["all"]

    WirelesslanSsidQosProfileDef = Literal[
        "bronze", "gold", "platinum", "silver"
    ]

    WirelesslanDefaultSsidQosProfileDef = Literal["silver"]

    WirelesslanCountryDef = Literal[
        "AE",
        "AR",
        "AT",
        "AU",
        "BA",
        "BB",
        "BE",
        "BG",
        "BH",
        "BN",
        "BO",
        "BR",
        "BY",
        "CA",
        "CA2",
        "CH",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CY",
        "CZ",
        "DE",
        "DK",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "ES",
        "FI",
        "FJ",
        "FR",
        "GB",
        "GH",
        "GI",
        "GR",
        "HK",
        "HR",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IO",
        "IQ",
        "IS",
        "IT",
        "J2",
        "J4",
        "JM",
        "JO",
        "KE",
        "KN",
        "KW",
        "KZ",
        "LB",
        "LI",
        "LK",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "ME",
        "MK",
        "MN",
        "MO",
        "MT",
        "MX",
        "MY",
        "NL",
        "NO",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PH",
        "PH2",
        "PK",
        "PL",
        "PR",
        "PT",
        "PY",
        "QA",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "TH",
        "TN",
        "TR",
        "TW",
        "UA",
        "US",
        "UY",
        "VE",
        "VN",
        "ZA",
    ]

    ServiceWirelesslanSsidRadioTypeDef = Literal["24ghz", "5ghz", "all"]

    ServiceWirelesslanDefaultSsidRadioTypeDef = Literal["all"]

    ServiceWirelesslanSsidQosProfileDef = Literal[
        "bronze", "gold", "platinum", "silver"
    ]

    ServiceWirelesslanDefaultSsidQosProfileDef = Literal["silver"]

    ServiceWirelesslanCountryDef = Literal[
        "AE",
        "AR",
        "AT",
        "AU",
        "BA",
        "BB",
        "BE",
        "BG",
        "BH",
        "BN",
        "BO",
        "BR",
        "BY",
        "CA",
        "CA2",
        "CH",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CY",
        "CZ",
        "DE",
        "DK",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "ES",
        "FI",
        "FJ",
        "FR",
        "GB",
        "GH",
        "GI",
        "GR",
        "HK",
        "HR",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IO",
        "IQ",
        "IS",
        "IT",
        "J2",
        "J4",
        "JM",
        "JO",
        "KE",
        "KN",
        "KW",
        "KZ",
        "LB",
        "LI",
        "LK",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "ME",
        "MK",
        "MN",
        "MO",
        "MT",
        "MX",
        "MY",
        "NL",
        "NO",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PH",
        "PH2",
        "PK",
        "PL",
        "PR",
        "PT",
        "PY",
        "QA",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "TH",
        "TN",
        "TR",
        "TW",
        "UA",
        "US",
        "UY",
        "VE",
        "VN",
        "ZA",
    ]


    class OneOfOnBooleanDefaultTrueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultTrueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfSsidNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSsidVlanIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSsidVlanIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSsidRadioTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SsidRadioTypeDef


    class OneOfSsidRadioTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSsidRadioTypeOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultSsidRadioTypeDef]


    class SecurityType:
        """
        Select security type
        """

        option_type: Any
        value: Any


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSsidRadiusServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSsidRadiusServerPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSsidRadiusServerPortOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfSsidRadiusServerSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSsidRadiusServerSecretOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSsidPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSsidPassphraseOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SecurityConfig1:
        # Select security type
        security_type: SecurityType
        passphrase: Optional[
            Union[
                OneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                OneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                OneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                OneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class WirelesslanSecurityType:
        """
        Select security type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class SecurityConfig2:
        # Select security type
        security_type: WirelesslanSecurityType
        passphrase: Optional[
            Union[
                OneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                OneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                OneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                OneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class OneOfSsidQosProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SsidQosProfileDef


    class OneOfSsidQosProfileOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSsidQosProfileOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultSsidQosProfileDef]


    class Ssid:
        admin_state: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        broadcast_ssid: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        name: OneOfSsidNameOptionsDef
        qos_profile: Union[
            OneOfSsidQosProfileOptionsDef1,
            OneOfSsidQosProfileOptionsDef2,
            OneOfSsidQosProfileOptionsDef3,
        ]
        radio_type: Union[
            OneOfSsidRadioTypeOptionsDef1,
            OneOfSsidRadioTypeOptionsDef2,
            OneOfSsidRadioTypeOptionsDef3,
        ]
        # Select security type
        security_config: Union[SecurityConfig1, SecurityConfig2]
        vlan_id: Union[
            OneOfSsidVlanIdOptionsDef1, OneOfSsidVlanIdOptionsDef2
        ]


    class OneOfCountryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CountryDef  # pytype: disable=annotation-type-mismatch


    class OneOfCountryOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUsernameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MeDynamicIpEnabled:
        """
        ME management IP dynamic allocated by DHCP
        """

        option_type: OptionType
        value: Any


    class MeIpConfig1:
        # ME management IP dynamic allocated by DHCP
        me_dynamic_ip_enabled: MeDynamicIpEnabled


    class BooleanGlobalFalseOptionsDef:
        option_type: GlobalOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpV4SubnetMaskOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class MeStaticIpCfg:
        """
        Mobility Express management IP static configuration
        """

        default_gateway: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        me_ipv4_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        netmask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class MeIpConfig2:
        me_dynamic_ip_enabled: BooleanGlobalFalseOptionsDef
        # Mobility Express management IP static configuration
        me_static_ip_cfg: MeStaticIpCfg


    class WirelesslanData:
        country: Union[OneOfCountryOptionsDef1, OneOfCountryOptionsDef2]
        enable24_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        enable5_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        # ME management IP configuration, if ME IP address is assigned by DHCP, a DHCP server parcel, a Wlan-GigabitEthernet switchport parcel, and a management SVI interface parcel must be created and associate with configuration group.
        me_ip_config: Union[MeIpConfig1, MeIpConfig2]
        password: Union[
            OneOfPasswordOptionsDef1, OneOfPasswordOptionsDef2
        ]
        # Configure Wi-Fi SSID profile
        ssid: List[Ssid]
        username: Union[
            OneOfUsernameOptionsDef1, OneOfUsernameOptionsDef2
        ]


    class Payload:
        """
        wirelesslan profile parcel schema for POST request
        """

        data: WirelesslanData
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
        # wirelesslan profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceWirelesslanPayload:
        data: Optional[List[Data]]


    class CreateWirelesslanProfileParcelForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ServiceWirelesslanData:
        country: Union[OneOfCountryOptionsDef1, OneOfCountryOptionsDef2]
        enable24_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        enable5_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        # ME management IP configuration, if ME IP address is assigned by DHCP, a DHCP server parcel, a Wlan-GigabitEthernet switchport parcel, and a management SVI interface parcel must be created and associate with configuration group.
        me_ip_config: Union[MeIpConfig1, MeIpConfig2]
        password: Union[
            OneOfPasswordOptionsDef1, OneOfPasswordOptionsDef2
        ]
        # Configure Wi-Fi SSID profile
        ssid: List[Ssid]
        username: Union[
            OneOfUsernameOptionsDef1, OneOfUsernameOptionsDef2
        ]


    class CreateWirelesslanProfileParcelForServicePostRequest:
        """
        wirelesslan profile parcel schema for POST request
        """

        data: ServiceWirelesslanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class WirelesslanOneOfSsidNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class WirelesslanOneOfSsidVlanIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WirelesslanOneOfSsidRadioTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WirelesslanSsidRadioTypeDef


    class WirelesslanOneOfSsidRadioTypeOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[WirelesslanDefaultSsidRadioTypeDef]


    class WirelesslanOneOfSsidRadiusServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WirelesslanOneOfSsidRadiusServerPortOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class WirelesslanOneOfSsidRadiusServerSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WirelesslanOneOfSsidPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WirelesslanSecurityConfig1:
        # Select security type
        security_type: SecurityType
        passphrase: Optional[
            Union[
                WirelesslanOneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                WirelesslanOneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                WirelesslanOneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                WirelesslanOneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class ServiceWirelesslanSecurityType:
        """
        Select security type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class ServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class ServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceWirelesslanOneOfSsidPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WirelesslanSecurityConfig2:
        # Select security type
        security_type: ServiceWirelesslanSecurityType
        passphrase: Optional[
            Union[
                ServiceWirelesslanOneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                ServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                ServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                ServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class WirelesslanOneOfSsidQosProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WirelesslanSsidQosProfileDef


    class WirelesslanOneOfSsidQosProfileOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[WirelesslanDefaultSsidQosProfileDef]


    class WirelesslanSsid:
        admin_state: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        broadcast_ssid: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        name: WirelesslanOneOfSsidNameOptionsDef
        qos_profile: Union[
            WirelesslanOneOfSsidQosProfileOptionsDef1,
            OneOfSsidQosProfileOptionsDef2,
            WirelesslanOneOfSsidQosProfileOptionsDef3,
        ]
        radio_type: Union[
            WirelesslanOneOfSsidRadioTypeOptionsDef1,
            OneOfSsidRadioTypeOptionsDef2,
            WirelesslanOneOfSsidRadioTypeOptionsDef3,
        ]
        # Select security type
        security_config: Union[
            WirelesslanSecurityConfig1, WirelesslanSecurityConfig2
        ]
        vlan_id: Union[
            WirelesslanOneOfSsidVlanIdOptionsDef1,
            OneOfSsidVlanIdOptionsDef2,
        ]


    class WirelesslanOneOfCountryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WirelesslanCountryDef  # pytype: disable=annotation-type-mismatch


    class WirelesslanOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class WirelesslanOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SdwanServiceWirelesslanData:
        country: Union[
            WirelesslanOneOfCountryOptionsDef1, OneOfCountryOptionsDef2
        ]
        enable24_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        enable5_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        # ME management IP configuration, if ME IP address is assigned by DHCP, a DHCP server parcel, a Wlan-GigabitEthernet switchport parcel, and a management SVI interface parcel must be created and associate with configuration group.
        me_ip_config: Union[MeIpConfig1, MeIpConfig2]
        password: Union[
            WirelesslanOneOfPasswordOptionsDef1, OneOfPasswordOptionsDef2
        ]
        # Configure Wi-Fi SSID profile
        ssid: List[WirelesslanSsid]
        username: Union[
            WirelesslanOneOfUsernameOptionsDef1, OneOfUsernameOptionsDef2
        ]


    class WirelesslanPayload:
        """
        wirelesslan profile parcel schema for PUT request
        """

        data: SdwanServiceWirelesslanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceWirelesslanPayload:
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
        # wirelesslan profile parcel schema for PUT request
        payload: Optional[WirelesslanPayload]


    class EditWirelesslanProfileParcelForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ServiceWirelesslanOneOfSsidNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceWirelesslanOneOfSsidVlanIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceWirelesslanOneOfSsidRadioTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceWirelesslanSsidRadioTypeDef


    class ServiceWirelesslanOneOfSsidRadioTypeOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[ServiceWirelesslanDefaultSsidRadioTypeDef]


    class SdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SdwanServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanServiceWirelesslanOneOfSsidPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceWirelesslanSecurityConfig1:
        # Select security type
        security_type: SecurityType
        passphrase: Optional[
            Union[
                SdwanServiceWirelesslanOneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                SdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                SdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                SdwanServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class SdwanServiceWirelesslanSecurityType:
        """
        Select security type
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanServiceWirelesslanOneOfSsidPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceWirelesslanSecurityConfig2:
        # Select security type
        security_type: SdwanServiceWirelesslanSecurityType
        passphrase: Optional[
            Union[
                FeatureProfileSdwanServiceWirelesslanOneOfSsidPassphraseOptionsDef1,
                OneOfSsidPassphraseOptionsDef2,
            ]
        ]
        radius_server_ip: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        radius_server_port: Optional[
            Union[
                FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef1,
                OneOfSsidRadiusServerPortOptionsDef2,
                FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerPortOptionsDef3,
            ]
        ]
        radius_server_secret: Optional[
            Union[
                FeatureProfileSdwanServiceWirelesslanOneOfSsidRadiusServerSecretOptionsDef1,
                OneOfSsidRadiusServerSecretOptionsDef2,
            ]
        ]


    class ServiceWirelesslanOneOfSsidQosProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceWirelesslanSsidQosProfileDef


    class ServiceWirelesslanOneOfSsidQosProfileOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[ServiceWirelesslanDefaultSsidQosProfileDef]


    class ServiceWirelesslanSsid:
        admin_state: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        broadcast_ssid: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        name: ServiceWirelesslanOneOfSsidNameOptionsDef
        qos_profile: Union[
            ServiceWirelesslanOneOfSsidQosProfileOptionsDef1,
            OneOfSsidQosProfileOptionsDef2,
            ServiceWirelesslanOneOfSsidQosProfileOptionsDef3,
        ]
        radio_type: Union[
            ServiceWirelesslanOneOfSsidRadioTypeOptionsDef1,
            OneOfSsidRadioTypeOptionsDef2,
            ServiceWirelesslanOneOfSsidRadioTypeOptionsDef3,
        ]
        # Select security type
        security_config: Union[
            ServiceWirelesslanSecurityConfig1,
            ServiceWirelesslanSecurityConfig2,
        ]
        vlan_id: Union[
            ServiceWirelesslanOneOfSsidVlanIdOptionsDef1,
            OneOfSsidVlanIdOptionsDef2,
        ]


    class ServiceWirelesslanOneOfCountryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceWirelesslanCountryDef  # pytype: disable=annotation-type-mismatch


    class ServiceWirelesslanOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceWirelesslanOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class FeatureProfileSdwanServiceWirelesslanData:
        country: Union[
            ServiceWirelesslanOneOfCountryOptionsDef1,
            OneOfCountryOptionsDef2,
        ]
        enable24_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        enable5_g: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]
        # ME management IP configuration, if ME IP address is assigned by DHCP, a DHCP server parcel, a Wlan-GigabitEthernet switchport parcel, and a management SVI interface parcel must be created and associate with configuration group.
        me_ip_config: Union[MeIpConfig1, MeIpConfig2]
        password: Union[
            ServiceWirelesslanOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        # Configure Wi-Fi SSID profile
        ssid: List[ServiceWirelesslanSsid]
        username: Union[
            ServiceWirelesslanOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class EditWirelesslanProfileParcelForServicePutRequest:
        """
        wirelesslan profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanServiceWirelesslanData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


