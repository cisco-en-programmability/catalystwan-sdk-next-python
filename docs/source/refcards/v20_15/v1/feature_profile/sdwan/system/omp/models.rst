======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

    BooleanFalseDef = Literal[False]

    Value = Literal[60, 300]

    DefaultAdvertiseConnectedDef = Literal[False, True]

    DefaultAdvertiseStaticDef = Literal[False, True]

    TransportGatewayEnumDef = Literal["ecmp-with-direct-path", "prefer"]

    SiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    OmpDefaultAdvertiseConnectedDef = Literal[False, True]

    OmpDefaultAdvertiseStaticDef = Literal[False, True]

    SystemOmpDefaultAdvertiseConnectedDef = Literal[False, True]

    SystemOmpDefaultAdvertiseStaticDef = Literal[False, True]

    OmpTransportGatewayEnumDef = Literal[
        "ecmp-with-direct-path", "prefer"
    ]

    OmpSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    SystemOmpSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    SdwanSystemOmpDefaultAdvertiseConnectedDef = Literal[False, True]

    SdwanSystemOmpDefaultAdvertiseStaticDef = Literal[False, True]

    FeatureProfileSdwanSystemOmpDefaultAdvertiseConnectedDef = Literal[
        False, True
    ]

    FeatureProfileSdwanSystemOmpDefaultAdvertiseStaticDef = Literal[
        False, True
    ]

    SystemOmpTransportGatewayEnumDef = Literal[
        "ecmp-with-direct-path", "prefer"
    ]

    SdwanSystemOmpSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    FeatureProfileSdwanSystemOmpSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]


    class OneOfGracefulRestartOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGracefulRestartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfGracefulRestartOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfOverlayAsOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOverlayAsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOverlayAsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSendPathLimitOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSendPathLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSendPathLimitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfEcmpLimitOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEcmpLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEcmpLimitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfShutdownOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfOmpAdminDistanceIpv4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOmpAdminDistanceIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOmpAdminDistanceIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class OneOfOmpAdminDistanceIpv6OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOmpAdminDistanceIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOmpAdminDistanceIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class OneOfAdvertisementIntervalOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertisementIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAdvertisementIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfGracefulRestartTimerOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGracefulRestartTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfGracefulRestartTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfEorTimerOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEorTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEorTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHoldtimeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value


    class OneOfAdvertiseProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAdvertiseProtocolOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAdvertiseConnectedOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseConnectedOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAdvertiseConnectedOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[DefaultAdvertiseConnectedDef]


    class OneOfAdvertiseStaticOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseStaticOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAdvertiseStaticOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[DefaultAdvertiseStaticDef]


    class AdvertiseIpv4:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            OneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospfv3: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            OneOfAdvertiseStaticOptionsDef3,
        ]


    class AdvertiseIpv6:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            OneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            OneOfAdvertiseStaticOptionsDef3,
        ]


    class OneOfIgnoreRegionPathLengthOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIgnoreRegionPathLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIgnoreRegionPathLengthOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTransportGatewayOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTransportGatewayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TransportGatewayEnumDef  # pytype: disable=annotation-type-mismatch


    class OneOfTransportGatewayOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSiteTypesOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSiteTypesOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            SiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSiteTypesOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOnBooleanDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OmpData:
        advertise_ipv4: AdvertiseIpv4
        advertise_ipv6: AdvertiseIpv6
        advertisement_interval: Union[
            OneOfAdvertisementIntervalOptionsDef1,
            OneOfAdvertisementIntervalOptionsDef2,
            OneOfAdvertisementIntervalOptionsDef3,
        ]
        ecmp_limit: Union[
            OneOfEcmpLimitOptionsDef1,
            OneOfEcmpLimitOptionsDef2,
            OneOfEcmpLimitOptionsDef3,
        ]
        eor_timer: Union[
            OneOfEorTimerOptionsDef1,
            OneOfEorTimerOptionsDef2,
            OneOfEorTimerOptionsDef3,
        ]
        graceful_restart: Union[
            OneOfGracefulRestartOptionsDef1,
            OneOfGracefulRestartOptionsDef2,
            OneOfGracefulRestartOptionsDef3,
        ]
        graceful_restart_timer: Union[
            OneOfGracefulRestartTimerOptionsDef1,
            OneOfGracefulRestartTimerOptionsDef2,
            OneOfGracefulRestartTimerOptionsDef3,
        ]
        holdtime: Union[
            OneOfHoldtimeOptionsDef1,
            OneOfHoldtimeOptionsDef2,
            OneOfHoldtimeOptionsDef3,
        ]
        omp_admin_distance_ipv4: Union[
            OneOfOmpAdminDistanceIpv4OptionsDef1,
            OneOfOmpAdminDistanceIpv4OptionsDef2,
            OneOfOmpAdminDistanceIpv4OptionsDef3,
        ]
        omp_admin_distance_ipv6: Union[
            OneOfOmpAdminDistanceIpv6OptionsDef1,
            OneOfOmpAdminDistanceIpv6OptionsDef2,
            OneOfOmpAdminDistanceIpv6OptionsDef3,
        ]
        overlay_as: Union[
            OneOfOverlayAsOptionsDef1,
            OneOfOverlayAsOptionsDef2,
            OneOfOverlayAsOptionsDef3,
        ]
        send_path_limit: Union[
            OneOfSendPathLimitOptionsDef1,
            OneOfSendPathLimitOptionsDef2,
            OneOfSendPathLimitOptionsDef3,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        aspath_auto_translation: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        ignore_region_path_length: Optional[
            Union[
                OneOfIgnoreRegionPathLengthOptionsDef1,
                OneOfIgnoreRegionPathLengthOptionsDef2,
                OneOfIgnoreRegionPathLengthOptionsDef3,
            ]
        ]
        site_types: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                OneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        site_types_for_transport_gateway: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                OneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class Payload:
        """
        OMP profile parcel schema for POST request
        """

        data: OmpData
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
        # OMP profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemOmpPayload:
        data: Optional[List[Data]]


    class CreateOmpProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemOmpData:
        advertise_ipv4: AdvertiseIpv4
        advertise_ipv6: AdvertiseIpv6
        advertisement_interval: Union[
            OneOfAdvertisementIntervalOptionsDef1,
            OneOfAdvertisementIntervalOptionsDef2,
            OneOfAdvertisementIntervalOptionsDef3,
        ]
        ecmp_limit: Union[
            OneOfEcmpLimitOptionsDef1,
            OneOfEcmpLimitOptionsDef2,
            OneOfEcmpLimitOptionsDef3,
        ]
        eor_timer: Union[
            OneOfEorTimerOptionsDef1,
            OneOfEorTimerOptionsDef2,
            OneOfEorTimerOptionsDef3,
        ]
        graceful_restart: Union[
            OneOfGracefulRestartOptionsDef1,
            OneOfGracefulRestartOptionsDef2,
            OneOfGracefulRestartOptionsDef3,
        ]
        graceful_restart_timer: Union[
            OneOfGracefulRestartTimerOptionsDef1,
            OneOfGracefulRestartTimerOptionsDef2,
            OneOfGracefulRestartTimerOptionsDef3,
        ]
        holdtime: Union[
            OneOfHoldtimeOptionsDef1,
            OneOfHoldtimeOptionsDef2,
            OneOfHoldtimeOptionsDef3,
        ]
        omp_admin_distance_ipv4: Union[
            OneOfOmpAdminDistanceIpv4OptionsDef1,
            OneOfOmpAdminDistanceIpv4OptionsDef2,
            OneOfOmpAdminDistanceIpv4OptionsDef3,
        ]
        omp_admin_distance_ipv6: Union[
            OneOfOmpAdminDistanceIpv6OptionsDef1,
            OneOfOmpAdminDistanceIpv6OptionsDef2,
            OneOfOmpAdminDistanceIpv6OptionsDef3,
        ]
        overlay_as: Union[
            OneOfOverlayAsOptionsDef1,
            OneOfOverlayAsOptionsDef2,
            OneOfOverlayAsOptionsDef3,
        ]
        send_path_limit: Union[
            OneOfSendPathLimitOptionsDef1,
            OneOfSendPathLimitOptionsDef2,
            OneOfSendPathLimitOptionsDef3,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        aspath_auto_translation: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        ignore_region_path_length: Optional[
            Union[
                OneOfIgnoreRegionPathLengthOptionsDef1,
                OneOfIgnoreRegionPathLengthOptionsDef2,
                OneOfIgnoreRegionPathLengthOptionsDef3,
            ]
        ]
        site_types: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                OneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        site_types_for_transport_gateway: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                OneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class CreateOmpProfileParcelForSystemPostRequest:
        """
        OMP profile parcel schema for POST request
        """

        data: SystemOmpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class OmpOneOfOverlayAsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfSendPathLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfEcmpLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfOmpAdminDistanceIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfOmpAdminDistanceIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class OmpOneOfOmpAdminDistanceIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfOmpAdminDistanceIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class OmpOneOfAdvertisementIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfGracefulRestartTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfEorTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfHoldtimeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OmpOneOfAdvertiseConnectedOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[OmpDefaultAdvertiseConnectedDef]


    class OmpOneOfAdvertiseStaticOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[OmpDefaultAdvertiseStaticDef]


    class OmpAdvertiseIpv4:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            OmpOneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospfv3: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            OmpOneOfAdvertiseStaticOptionsDef3,
        ]


    class SystemOmpOneOfAdvertiseConnectedOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[SystemOmpDefaultAdvertiseConnectedDef]


    class SystemOmpOneOfAdvertiseStaticOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[SystemOmpDefaultAdvertiseStaticDef]


    class OmpAdvertiseIpv6:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            SystemOmpOneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            SystemOmpOneOfAdvertiseStaticOptionsDef3,
        ]


    class OmpOneOfTransportGatewayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: OmpTransportGatewayEnumDef  # pytype: disable=annotation-type-mismatch


    class OmpOneOfSiteTypesOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            OmpSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class SystemOmpOneOfSiteTypesOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            SystemOmpSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class SdwanSystemOmpData:
        advertise_ipv4: OmpAdvertiseIpv4
        advertise_ipv6: OmpAdvertiseIpv6
        advertisement_interval: Union[
            OneOfAdvertisementIntervalOptionsDef1,
            OmpOneOfAdvertisementIntervalOptionsDef2,
            OneOfAdvertisementIntervalOptionsDef3,
        ]
        ecmp_limit: Union[
            OneOfEcmpLimitOptionsDef1,
            OmpOneOfEcmpLimitOptionsDef2,
            OneOfEcmpLimitOptionsDef3,
        ]
        eor_timer: Union[
            OneOfEorTimerOptionsDef1,
            OmpOneOfEorTimerOptionsDef2,
            OneOfEorTimerOptionsDef3,
        ]
        graceful_restart: Union[
            OneOfGracefulRestartOptionsDef1,
            OneOfGracefulRestartOptionsDef2,
            OneOfGracefulRestartOptionsDef3,
        ]
        graceful_restart_timer: Union[
            OneOfGracefulRestartTimerOptionsDef1,
            OmpOneOfGracefulRestartTimerOptionsDef2,
            OneOfGracefulRestartTimerOptionsDef3,
        ]
        holdtime: Union[
            OneOfHoldtimeOptionsDef1,
            OmpOneOfHoldtimeOptionsDef2,
            OneOfHoldtimeOptionsDef3,
        ]
        omp_admin_distance_ipv4: Union[
            OneOfOmpAdminDistanceIpv4OptionsDef1,
            OmpOneOfOmpAdminDistanceIpv4OptionsDef2,
            OmpOneOfOmpAdminDistanceIpv4OptionsDef3,
        ]
        omp_admin_distance_ipv6: Union[
            OneOfOmpAdminDistanceIpv6OptionsDef1,
            OmpOneOfOmpAdminDistanceIpv6OptionsDef2,
            OmpOneOfOmpAdminDistanceIpv6OptionsDef3,
        ]
        overlay_as: Union[
            OneOfOverlayAsOptionsDef1,
            OmpOneOfOverlayAsOptionsDef2,
            OneOfOverlayAsOptionsDef3,
        ]
        send_path_limit: Union[
            OneOfSendPathLimitOptionsDef1,
            OmpOneOfSendPathLimitOptionsDef2,
            OneOfSendPathLimitOptionsDef3,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        aspath_auto_translation: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        ignore_region_path_length: Optional[
            Union[
                OneOfIgnoreRegionPathLengthOptionsDef1,
                OneOfIgnoreRegionPathLengthOptionsDef2,
                OneOfIgnoreRegionPathLengthOptionsDef3,
            ]
        ]
        site_types: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                SystemOmpOneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        site_types_for_transport_gateway: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                OmpOneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OmpOneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class OmpPayload:
        """
        OMP profile parcel schema for PUT request
        """

        data: SdwanSystemOmpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemOmpPayload:
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
        # OMP profile parcel schema for PUT request
        payload: Optional[OmpPayload]


    class EditOmpProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemOmpOneOfOverlayAsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfSendPathLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfEcmpLimitOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfOmpAdminDistanceIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfOmpAdminDistanceIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class SystemOmpOneOfOmpAdminDistanceIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfOmpAdminDistanceIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[int]


    class SystemOmpOneOfAdvertisementIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfGracefulRestartTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfEorTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemOmpOneOfHoldtimeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanSystemOmpOneOfAdvertiseConnectedOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[SdwanSystemOmpDefaultAdvertiseConnectedDef]


    class SdwanSystemOmpOneOfAdvertiseStaticOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[SdwanSystemOmpDefaultAdvertiseStaticDef]


    class SystemOmpAdvertiseIpv4:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            SdwanSystemOmpOneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospfv3: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            SdwanSystemOmpOneOfAdvertiseStaticOptionsDef3,
        ]


    class FeatureProfileSdwanSystemOmpOneOfAdvertiseConnectedOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[
            FeatureProfileSdwanSystemOmpDefaultAdvertiseConnectedDef
        ]


    class FeatureProfileSdwanSystemOmpOneOfAdvertiseStaticOptionsDef3:
        option_type: DefaultOptionTypeDef
        # use enum for backward compatibility, use default for UI to display default value
        value: Optional[
            FeatureProfileSdwanSystemOmpDefaultAdvertiseStaticDef
        ]


    class SystemOmpAdvertiseIpv6:
        bgp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        connected: Union[
            OneOfAdvertiseConnectedOptionsDef1,
            OneOfAdvertiseConnectedOptionsDef2,
            FeatureProfileSdwanSystemOmpOneOfAdvertiseConnectedOptionsDef3,
        ]
        eigrp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        isis: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        lisp: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        ospf: Union[
            OneOfAdvertiseProtocolOptionsDef1,
            OneOfAdvertiseProtocolOptionsDef2,
            OneOfAdvertiseProtocolOptionsDef3,
        ]
        static: Union[
            OneOfAdvertiseStaticOptionsDef1,
            OneOfAdvertiseStaticOptionsDef2,
            FeatureProfileSdwanSystemOmpOneOfAdvertiseStaticOptionsDef3,
        ]


    class SystemOmpOneOfTransportGatewayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SystemOmpTransportGatewayEnumDef  # pytype: disable=annotation-type-mismatch


    class SdwanSystemOmpOneOfSiteTypesOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            SdwanSystemOmpSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanSystemOmpOneOfSiteTypesOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            FeatureProfileSdwanSystemOmpSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanSystemOmpData:
        advertise_ipv4: SystemOmpAdvertiseIpv4
        advertise_ipv6: SystemOmpAdvertiseIpv6
        advertisement_interval: Union[
            OneOfAdvertisementIntervalOptionsDef1,
            SystemOmpOneOfAdvertisementIntervalOptionsDef2,
            OneOfAdvertisementIntervalOptionsDef3,
        ]
        ecmp_limit: Union[
            OneOfEcmpLimitOptionsDef1,
            SystemOmpOneOfEcmpLimitOptionsDef2,
            OneOfEcmpLimitOptionsDef3,
        ]
        eor_timer: Union[
            OneOfEorTimerOptionsDef1,
            SystemOmpOneOfEorTimerOptionsDef2,
            OneOfEorTimerOptionsDef3,
        ]
        graceful_restart: Union[
            OneOfGracefulRestartOptionsDef1,
            OneOfGracefulRestartOptionsDef2,
            OneOfGracefulRestartOptionsDef3,
        ]
        graceful_restart_timer: Union[
            OneOfGracefulRestartTimerOptionsDef1,
            SystemOmpOneOfGracefulRestartTimerOptionsDef2,
            OneOfGracefulRestartTimerOptionsDef3,
        ]
        holdtime: Union[
            OneOfHoldtimeOptionsDef1,
            SystemOmpOneOfHoldtimeOptionsDef2,
            OneOfHoldtimeOptionsDef3,
        ]
        omp_admin_distance_ipv4: Union[
            OneOfOmpAdminDistanceIpv4OptionsDef1,
            SystemOmpOneOfOmpAdminDistanceIpv4OptionsDef2,
            SystemOmpOneOfOmpAdminDistanceIpv4OptionsDef3,
        ]
        omp_admin_distance_ipv6: Union[
            OneOfOmpAdminDistanceIpv6OptionsDef1,
            SystemOmpOneOfOmpAdminDistanceIpv6OptionsDef2,
            SystemOmpOneOfOmpAdminDistanceIpv6OptionsDef3,
        ]
        overlay_as: Union[
            OneOfOverlayAsOptionsDef1,
            SystemOmpOneOfOverlayAsOptionsDef2,
            OneOfOverlayAsOptionsDef3,
        ]
        send_path_limit: Union[
            OneOfSendPathLimitOptionsDef1,
            SystemOmpOneOfSendPathLimitOptionsDef2,
            OneOfSendPathLimitOptionsDef3,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        aspath_auto_translation: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        ignore_region_path_length: Optional[
            Union[
                OneOfIgnoreRegionPathLengthOptionsDef1,
                OneOfIgnoreRegionPathLengthOptionsDef2,
                OneOfIgnoreRegionPathLengthOptionsDef3,
            ]
        ]
        site_types: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                FeatureProfileSdwanSystemOmpOneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        site_types_for_transport_gateway: Optional[
            Union[
                OneOfSiteTypesOptionsDef1,
                SdwanSystemOmpOneOfSiteTypesOptionsDef2,
                OneOfSiteTypesOptionsDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                SystemOmpOneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class EditOmpProfileParcelForSystemPutRequest:
        """
        OMP profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemOmpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


