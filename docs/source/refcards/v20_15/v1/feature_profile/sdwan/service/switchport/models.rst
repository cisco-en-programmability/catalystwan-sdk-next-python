======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    InterfaceModeDef = Literal["access", "trunk"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

    InterfaceSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    InterfaceDuplexDef = Literal["full", "half"]

    InterfacePortControlDef = Literal[
        "auto", "force-authorized", "force-unauthorized"
    ]

    InterfaceHostModeDef = Literal[
        "multi-auth", "multi-domain", "multi-host", "single-host"
    ]

    InterfaceControlDirectionDef = Literal["both", "in"]

    SwitchportInterfaceModeDef = Literal["access", "trunk"]

    SwitchportInterfaceSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    SwitchportInterfaceDuplexDef = Literal["full", "half"]

    SwitchportInterfacePortControlDef = Literal[
        "auto", "force-authorized", "force-unauthorized"
    ]

    SwitchportInterfaceHostModeDef = Literal[
        "multi-auth", "multi-domain", "multi-host", "single-host"
    ]

    SwitchportInterfaceControlDirectionDef = Literal["both", "in"]

    ServiceSwitchportInterfaceModeDef = Literal["access", "trunk"]

    ServiceSwitchportInterfaceSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    ServiceSwitchportInterfaceDuplexDef = Literal["full", "half"]

    ServiceSwitchportInterfacePortControlDef = Literal[
        "auto", "force-authorized", "force-unauthorized"
    ]

    ServiceSwitchportInterfaceHostModeDef = Literal[
        "multi-auth", "multi-domain", "multi-host", "single-host"
    ]

    ServiceSwitchportInterfaceControlDirectionDef = Literal["both", "in"]


    class OneOfInterfaceIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            InterfaceModeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfInterfaceShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            InterfaceSpeedDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfInterfaceSpeedOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceSpeedOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            InterfaceDuplexDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfInterfaceDuplexOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDuplexOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceSwitchportAccessVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceSwitchportAccessVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceSwitchportAccessVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceVlansOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceVlansOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceVlansOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfacePortControlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfacePortControlDef


    class OneOfInterfacePortControlOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacePortControlOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceVoiceVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceVoiceVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceVoiceVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfacePaeEnableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfacePaeEnableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacePaeEnableOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceMacAuthenticationBypassOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceMacAuthenticationBypassOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceMacAuthenticationBypassOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceHostModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceHostModeDef


    class OneOfInterfaceHostModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceHostModeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceEnablePeriodicReauthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceEnablePeriodicReauthOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceEnablePeriodicReauthOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceInactivityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceInactivityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceInactivityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceReauthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceReauthenticationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceReauthenticationOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInterfaceControlDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceControlDirectionDef


    class OneOfInterfaceControlDirectionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceControlDirectionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceRestrictedVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceRestrictedVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceRestrictedVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceGuestVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceGuestVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceGuestVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceCriticalVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceCriticalVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceCriticalVlanOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceEnableVoiceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceEnableVoiceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceEnableVoiceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Interface:
        if_name: Union[
            OneOfInterfaceIfNameOptionsDef1,
            OneOfInterfaceIfNameOptionsDef2,
        ]
        control_direction: Optional[
            Union[
                OneOfInterfaceControlDirectionOptionsDef1,
                OneOfInterfaceControlDirectionOptionsDef2,
                OneOfInterfaceControlDirectionOptionsDef3,
            ]
        ]
        critical_vlan: Optional[
            Union[
                OneOfInterfaceCriticalVlanOptionsDef1,
                OneOfInterfaceCriticalVlanOptionsDef2,
                OneOfInterfaceCriticalVlanOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                OneOfInterfaceDuplexOptionsDef1,
                OneOfInterfaceDuplexOptionsDef2,
                OneOfInterfaceDuplexOptionsDef3,
            ]
        ]
        enable_dot1x: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        enable_periodic_reauth: Optional[
            Union[
                OneOfInterfaceEnablePeriodicReauthOptionsDef1,
                OneOfInterfaceEnablePeriodicReauthOptionsDef2,
                OneOfInterfaceEnablePeriodicReauthOptionsDef3,
            ]
        ]
        enable_voice: Optional[
            Union[
                OneOfInterfaceEnableVoiceOptionsDef1,
                OneOfInterfaceEnableVoiceOptionsDef2,
                OneOfInterfaceEnableVoiceOptionsDef3,
            ]
        ]
        guest_vlan: Optional[
            Union[
                OneOfInterfaceGuestVlanOptionsDef1,
                OneOfInterfaceGuestVlanOptionsDef2,
                OneOfInterfaceGuestVlanOptionsDef3,
            ]
        ]
        host_mode: Optional[
            Union[
                OneOfInterfaceHostModeOptionsDef1,
                OneOfInterfaceHostModeOptionsDef2,
                OneOfInterfaceHostModeOptionsDef3,
            ]
        ]
        inactivity: Optional[
            Union[
                OneOfInterfaceInactivityOptionsDef1,
                OneOfInterfaceInactivityOptionsDef2,
                OneOfInterfaceInactivityOptionsDef3,
            ]
        ]
        mac_authentication_bypass: Optional[
            Union[
                OneOfInterfaceMacAuthenticationBypassOptionsDef1,
                OneOfInterfaceMacAuthenticationBypassOptionsDef2,
                OneOfInterfaceMacAuthenticationBypassOptionsDef3,
            ]
        ]
        mode: Optional[OneOfInterfaceModeOptionsDef]
        pae_enable: Optional[
            Union[
                OneOfInterfacePaeEnableOptionsDef1,
                OneOfInterfacePaeEnableOptionsDef2,
                OneOfInterfacePaeEnableOptionsDef3,
            ]
        ]
        port_control: Optional[
            Union[
                OneOfInterfacePortControlOptionsDef1,
                OneOfInterfacePortControlOptionsDef2,
                OneOfInterfacePortControlOptionsDef3,
            ]
        ]
        reauthentication: Optional[
            Union[
                OneOfInterfaceReauthenticationOptionsDef1,
                OneOfInterfaceReauthenticationOptionsDef2,
                OneOfInterfaceReauthenticationOptionsDef3,
            ]
        ]
        restricted_vlan: Optional[
            Union[
                OneOfInterfaceRestrictedVlanOptionsDef1,
                OneOfInterfaceRestrictedVlanOptionsDef2,
                OneOfInterfaceRestrictedVlanOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
                OneOfInterfaceShutdownOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                OneOfInterfaceSpeedOptionsDef1,
                OneOfInterfaceSpeedOptionsDef2,
                OneOfInterfaceSpeedOptionsDef3,
            ]
        ]
        switchport_access_vlan: Optional[
            Union[
                OneOfInterfaceSwitchportAccessVlanOptionsDef1,
                OneOfInterfaceSwitchportAccessVlanOptionsDef2,
                OneOfInterfaceSwitchportAccessVlanOptionsDef3,
            ]
        ]
        switchport_trunk_allowed_vlans: Optional[
            Union[
                OneOfInterfaceVlansOptionsDef1,
                OneOfInterfaceVlansOptionsDef2,
                OneOfInterfaceVlansOptionsDef3,
            ]
        ]
        switchport_trunk_native_vlan: Optional[
            Union[
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef2,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef3,
            ]
        ]
        voice_vlan: Optional[
            Union[
                OneOfInterfaceVoiceVlanOptionsDef1,
                OneOfInterfaceVoiceVlanOptionsDef2,
                OneOfInterfaceVoiceVlanOptionsDef3,
            ]
        ]


    class OneOfAgeTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAgeTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAgeTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfStaticMacAddressMacaddrOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticMacAddressMacaddrOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticMacAddressVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfStaticMacAddressVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticMacAddressIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticMacAddressIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class StaticMacAddress:
        macaddr: Union[
            OneOfStaticMacAddressMacaddrOptionsDef1,
            OneOfStaticMacAddressMacaddrOptionsDef2,
        ]
        vlan: Union[
            OneOfStaticMacAddressVlanOptionsDef1,
            OneOfStaticMacAddressVlanOptionsDef2,
        ]
        if_name: Optional[
            Union[
                OneOfStaticMacAddressIfNameOptionsDef1,
                OneOfStaticMacAddressIfNameOptionsDef2,
            ]
        ]


    class SwitchportData:
        age_time: Optional[
            Union[
                OneOfAgeTimeOptionsDef1,
                OneOfAgeTimeOptionsDef2,
                OneOfAgeTimeOptionsDef3,
            ]
        ]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[Interface]]
        # Add static MAC address entries for interface
        static_mac_address: Optional[List[StaticMacAddress]]


    class Payload:
        """
        SwitchPort profile parcel schema for POST request
        """

        data: SwitchportData
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
        # SwitchPort profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceSwitchportPayload:
        data: Optional[List[Data]]


    class CedgeServiceProfileSwitchportParcelRestfulResourcePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ServiceSwitchportData:
        age_time: Optional[
            Union[
                OneOfAgeTimeOptionsDef1,
                OneOfAgeTimeOptionsDef2,
                OneOfAgeTimeOptionsDef3,
            ]
        ]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[Interface]]
        # Add static MAC address entries for interface
        static_mac_address: Optional[List[StaticMacAddress]]


    class CedgeServiceProfileSwitchportParcelRestfulResourcePostRequest:
        """
        SwitchPort profile parcel schema for POST request
        """

        data: ServiceSwitchportData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SwitchportOneOfInterfaceIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SwitchportOneOfInterfaceModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfaceModeDef  # pytype: disable=annotation-type-mismatch


    class SwitchportOneOfInterfaceSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfaceSpeedDef  # pytype: disable=annotation-type-mismatch


    class SwitchportOneOfInterfaceDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfaceDuplexDef  # pytype: disable=annotation-type-mismatch


    class SwitchportOneOfInterfaceSwitchportAccessVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceVlansOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SwitchportOneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfacePortControlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfacePortControlDef


    class SwitchportOneOfInterfaceVoiceVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceHostModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfaceHostModeDef


    class SwitchportOneOfInterfaceInactivityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceReauthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceReauthenticationOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceControlDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SwitchportInterfaceControlDirectionDef


    class SwitchportOneOfInterfaceRestrictedVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceGuestVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfInterfaceCriticalVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportInterface:
        if_name: Union[
            SwitchportOneOfInterfaceIfNameOptionsDef1,
            OneOfInterfaceIfNameOptionsDef2,
        ]
        control_direction: Optional[
            Union[
                SwitchportOneOfInterfaceControlDirectionOptionsDef1,
                OneOfInterfaceControlDirectionOptionsDef2,
                OneOfInterfaceControlDirectionOptionsDef3,
            ]
        ]
        critical_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceCriticalVlanOptionsDef1,
                OneOfInterfaceCriticalVlanOptionsDef2,
                OneOfInterfaceCriticalVlanOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                SwitchportOneOfInterfaceDuplexOptionsDef1,
                OneOfInterfaceDuplexOptionsDef2,
                OneOfInterfaceDuplexOptionsDef3,
            ]
        ]
        enable_dot1x: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        enable_periodic_reauth: Optional[
            Union[
                OneOfInterfaceEnablePeriodicReauthOptionsDef1,
                OneOfInterfaceEnablePeriodicReauthOptionsDef2,
                OneOfInterfaceEnablePeriodicReauthOptionsDef3,
            ]
        ]
        enable_voice: Optional[
            Union[
                OneOfInterfaceEnableVoiceOptionsDef1,
                OneOfInterfaceEnableVoiceOptionsDef2,
                OneOfInterfaceEnableVoiceOptionsDef3,
            ]
        ]
        guest_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceGuestVlanOptionsDef1,
                OneOfInterfaceGuestVlanOptionsDef2,
                OneOfInterfaceGuestVlanOptionsDef3,
            ]
        ]
        host_mode: Optional[
            Union[
                SwitchportOneOfInterfaceHostModeOptionsDef1,
                OneOfInterfaceHostModeOptionsDef2,
                OneOfInterfaceHostModeOptionsDef3,
            ]
        ]
        inactivity: Optional[
            Union[
                SwitchportOneOfInterfaceInactivityOptionsDef1,
                OneOfInterfaceInactivityOptionsDef2,
                OneOfInterfaceInactivityOptionsDef3,
            ]
        ]
        mac_authentication_bypass: Optional[
            Union[
                OneOfInterfaceMacAuthenticationBypassOptionsDef1,
                OneOfInterfaceMacAuthenticationBypassOptionsDef2,
                OneOfInterfaceMacAuthenticationBypassOptionsDef3,
            ]
        ]
        mode: Optional[SwitchportOneOfInterfaceModeOptionsDef]
        pae_enable: Optional[
            Union[
                OneOfInterfacePaeEnableOptionsDef1,
                OneOfInterfacePaeEnableOptionsDef2,
                OneOfInterfacePaeEnableOptionsDef3,
            ]
        ]
        port_control: Optional[
            Union[
                SwitchportOneOfInterfacePortControlOptionsDef1,
                OneOfInterfacePortControlOptionsDef2,
                OneOfInterfacePortControlOptionsDef3,
            ]
        ]
        reauthentication: Optional[
            Union[
                SwitchportOneOfInterfaceReauthenticationOptionsDef1,
                OneOfInterfaceReauthenticationOptionsDef2,
                SwitchportOneOfInterfaceReauthenticationOptionsDef3,
            ]
        ]
        restricted_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceRestrictedVlanOptionsDef1,
                OneOfInterfaceRestrictedVlanOptionsDef2,
                OneOfInterfaceRestrictedVlanOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
                OneOfInterfaceShutdownOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                SwitchportOneOfInterfaceSpeedOptionsDef1,
                OneOfInterfaceSpeedOptionsDef2,
                OneOfInterfaceSpeedOptionsDef3,
            ]
        ]
        switchport_access_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceSwitchportAccessVlanOptionsDef1,
                OneOfInterfaceSwitchportAccessVlanOptionsDef2,
                OneOfInterfaceSwitchportAccessVlanOptionsDef3,
            ]
        ]
        switchport_trunk_allowed_vlans: Optional[
            Union[
                SwitchportOneOfInterfaceVlansOptionsDef1,
                OneOfInterfaceVlansOptionsDef2,
                OneOfInterfaceVlansOptionsDef3,
            ]
        ]
        switchport_trunk_native_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef2,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef3,
            ]
        ]
        voice_vlan: Optional[
            Union[
                SwitchportOneOfInterfaceVoiceVlanOptionsDef1,
                OneOfInterfaceVoiceVlanOptionsDef2,
                OneOfInterfaceVoiceVlanOptionsDef3,
            ]
        ]


    class SwitchportOneOfAgeTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfAgeTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SwitchportOneOfStaticMacAddressMacaddrOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SwitchportOneOfStaticMacAddressVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SwitchportOneOfStaticMacAddressIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SwitchportStaticMacAddress:
        macaddr: Union[
            SwitchportOneOfStaticMacAddressMacaddrOptionsDef1,
            OneOfStaticMacAddressMacaddrOptionsDef2,
        ]
        vlan: Union[
            SwitchportOneOfStaticMacAddressVlanOptionsDef1,
            OneOfStaticMacAddressVlanOptionsDef2,
        ]
        if_name: Optional[
            Union[
                SwitchportOneOfStaticMacAddressIfNameOptionsDef1,
                OneOfStaticMacAddressIfNameOptionsDef2,
            ]
        ]


    class SdwanServiceSwitchportData:
        age_time: Optional[
            Union[
                SwitchportOneOfAgeTimeOptionsDef1,
                OneOfAgeTimeOptionsDef2,
                SwitchportOneOfAgeTimeOptionsDef3,
            ]
        ]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[SwitchportInterface]]
        # Add static MAC address entries for interface
        static_mac_address: Optional[List[SwitchportStaticMacAddress]]


    class SwitchportPayload:
        """
        SwitchPort profile parcel schema for PUT request
        """

        data: SdwanServiceSwitchportData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceSwitchportPayload:
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
        # SwitchPort profile parcel schema for PUT request
        payload: Optional[SwitchportPayload]


    class EditSwitchportParcelAssociationForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ServiceSwitchportOneOfInterfaceIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceSwitchportOneOfInterfaceModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfaceModeDef  # pytype: disable=annotation-type-mismatch


    class ServiceSwitchportOneOfInterfaceSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfaceSpeedDef  # pytype: disable=annotation-type-mismatch


    class ServiceSwitchportOneOfInterfaceDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfaceDuplexDef  # pytype: disable=annotation-type-mismatch


    class ServiceSwitchportOneOfInterfaceSwitchportAccessVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceVlansOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceSwitchportOneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfacePortControlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfacePortControlDef


    class ServiceSwitchportOneOfInterfaceVoiceVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceHostModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfaceHostModeDef


    class ServiceSwitchportOneOfInterfaceInactivityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceReauthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceReauthenticationOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceControlDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceSwitchportInterfaceControlDirectionDef


    class ServiceSwitchportOneOfInterfaceRestrictedVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceGuestVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfInterfaceCriticalVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportInterface:
        if_name: Union[
            ServiceSwitchportOneOfInterfaceIfNameOptionsDef1,
            OneOfInterfaceIfNameOptionsDef2,
        ]
        control_direction: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceControlDirectionOptionsDef1,
                OneOfInterfaceControlDirectionOptionsDef2,
                OneOfInterfaceControlDirectionOptionsDef3,
            ]
        ]
        critical_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceCriticalVlanOptionsDef1,
                OneOfInterfaceCriticalVlanOptionsDef2,
                OneOfInterfaceCriticalVlanOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceDuplexOptionsDef1,
                OneOfInterfaceDuplexOptionsDef2,
                OneOfInterfaceDuplexOptionsDef3,
            ]
        ]
        enable_dot1x: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        enable_periodic_reauth: Optional[
            Union[
                OneOfInterfaceEnablePeriodicReauthOptionsDef1,
                OneOfInterfaceEnablePeriodicReauthOptionsDef2,
                OneOfInterfaceEnablePeriodicReauthOptionsDef3,
            ]
        ]
        enable_voice: Optional[
            Union[
                OneOfInterfaceEnableVoiceOptionsDef1,
                OneOfInterfaceEnableVoiceOptionsDef2,
                OneOfInterfaceEnableVoiceOptionsDef3,
            ]
        ]
        guest_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceGuestVlanOptionsDef1,
                OneOfInterfaceGuestVlanOptionsDef2,
                OneOfInterfaceGuestVlanOptionsDef3,
            ]
        ]
        host_mode: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceHostModeOptionsDef1,
                OneOfInterfaceHostModeOptionsDef2,
                OneOfInterfaceHostModeOptionsDef3,
            ]
        ]
        inactivity: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceInactivityOptionsDef1,
                OneOfInterfaceInactivityOptionsDef2,
                OneOfInterfaceInactivityOptionsDef3,
            ]
        ]
        mac_authentication_bypass: Optional[
            Union[
                OneOfInterfaceMacAuthenticationBypassOptionsDef1,
                OneOfInterfaceMacAuthenticationBypassOptionsDef2,
                OneOfInterfaceMacAuthenticationBypassOptionsDef3,
            ]
        ]
        mode: Optional[ServiceSwitchportOneOfInterfaceModeOptionsDef]
        pae_enable: Optional[
            Union[
                OneOfInterfacePaeEnableOptionsDef1,
                OneOfInterfacePaeEnableOptionsDef2,
                OneOfInterfacePaeEnableOptionsDef3,
            ]
        ]
        port_control: Optional[
            Union[
                ServiceSwitchportOneOfInterfacePortControlOptionsDef1,
                OneOfInterfacePortControlOptionsDef2,
                OneOfInterfacePortControlOptionsDef3,
            ]
        ]
        reauthentication: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceReauthenticationOptionsDef1,
                OneOfInterfaceReauthenticationOptionsDef2,
                ServiceSwitchportOneOfInterfaceReauthenticationOptionsDef3,
            ]
        ]
        restricted_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceRestrictedVlanOptionsDef1,
                OneOfInterfaceRestrictedVlanOptionsDef2,
                OneOfInterfaceRestrictedVlanOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
                OneOfInterfaceShutdownOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceSpeedOptionsDef1,
                OneOfInterfaceSpeedOptionsDef2,
                OneOfInterfaceSpeedOptionsDef3,
            ]
        ]
        switchport_access_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceSwitchportAccessVlanOptionsDef1,
                OneOfInterfaceSwitchportAccessVlanOptionsDef2,
                OneOfInterfaceSwitchportAccessVlanOptionsDef3,
            ]
        ]
        switchport_trunk_allowed_vlans: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceVlansOptionsDef1,
                OneOfInterfaceVlansOptionsDef2,
                OneOfInterfaceVlansOptionsDef3,
            ]
        ]
        switchport_trunk_native_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceSwitchportTrunkNativeVlanOptionsDef1,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef2,
                OneOfInterfaceSwitchportTrunkNativeVlanOptionsDef3,
            ]
        ]
        voice_vlan: Optional[
            Union[
                ServiceSwitchportOneOfInterfaceVoiceVlanOptionsDef1,
                OneOfInterfaceVoiceVlanOptionsDef2,
                OneOfInterfaceVoiceVlanOptionsDef3,
            ]
        ]


    class ServiceSwitchportOneOfAgeTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfAgeTimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ServiceSwitchportOneOfStaticMacAddressMacaddrOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceSwitchportOneOfStaticMacAddressVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceSwitchportOneOfStaticMacAddressIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceSwitchportStaticMacAddress:
        macaddr: Union[
            ServiceSwitchportOneOfStaticMacAddressMacaddrOptionsDef1,
            OneOfStaticMacAddressMacaddrOptionsDef2,
        ]
        vlan: Union[
            ServiceSwitchportOneOfStaticMacAddressVlanOptionsDef1,
            OneOfStaticMacAddressVlanOptionsDef2,
        ]
        if_name: Optional[
            Union[
                ServiceSwitchportOneOfStaticMacAddressIfNameOptionsDef1,
                OneOfStaticMacAddressIfNameOptionsDef2,
            ]
        ]


    class FeatureProfileSdwanServiceSwitchportData:
        age_time: Optional[
            Union[
                ServiceSwitchportOneOfAgeTimeOptionsDef1,
                OneOfAgeTimeOptionsDef2,
                ServiceSwitchportOneOfAgeTimeOptionsDef3,
            ]
        ]
        # Interface name: GigabitEthernet0/<>/<> when present
        interface: Optional[List[ServiceSwitchportInterface]]
        # Add static MAC address entries for interface
        static_mac_address: Optional[
            List[ServiceSwitchportStaticMacAddress]
        ]


    class EditSwitchportParcelAssociationForServicePutRequest:
        """
        SwitchPort profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanServiceSwitchportData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


