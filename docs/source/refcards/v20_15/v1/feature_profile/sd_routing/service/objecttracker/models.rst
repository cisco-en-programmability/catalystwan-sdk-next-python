======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    InterfaceTrackTypeDef = Literal[
        "ip-routing", "ipv6-routing", "line-protocol"
    ]

    DefaultOptionTypeDef = Literal["default"]

    DefaultInterfaceTrackTypeDef = Literal["line-protocol"]

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


    class OneOfTrackerObjectIdDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerObjectIdDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceNameV2OptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameV2OptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTrackTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceTrackTypeDef


    class OneOfInterfaceTrackTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultInterfaceTrackTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceTrackTypeOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceObjectTrackerConfigDef:
        if_name: Union[
            OneOfInterfaceNameV2OptionsNoDefaultDef1,
            OneOfInterfaceNameV2OptionsNoDefaultDef2,
        ]
        interface_track_type: Union[
            OneOfInterfaceTrackTypeOptionsDef1,
            OneOfInterfaceTrackTypeOptionsDef2,
            OneOfInterfaceTrackTypeOptionsDef3,
        ]


    class OneOfObjectTrackerConfigOptionsDef1:
        interface: OneOfInterfaceObjectTrackerConfigDef


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


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


    class OneOfVrfOptionsWithDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsWithDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVrfOptionsWithDefault3:
        option_type: DefaultOptionTypeDef


    class OneOfRouteObjectTrackerConfigDef:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]
        vrf_name: Union[
            OneOfVrfOptionsWithDefault1,
            OneOfVrfOptionsWithDefault2,
            OneOfVrfOptionsWithDefault3,
        ]


    class OneOfObjectTrackerConfigOptionsDef2:
        route: OneOfRouteObjectTrackerConfigDef


    class OneOfDelayUpTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDelayUpTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDelayUpTimeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDelayDownTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDelayDownTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDelayDownTimeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class ObjecttrackerData:
        delay_down_time: Union[
            OneOfDelayDownTimeOptionsDef1,
            OneOfDelayDownTimeOptionsDef2,
            OneOfDelayDownTimeOptionsDef3,
        ]
        delay_up_time: Union[
            OneOfDelayUpTimeOptionsDef1,
            OneOfDelayUpTimeOptionsDef2,
            OneOfDelayUpTimeOptionsDef3,
        ]
        tracker_config: Union[
            OneOfObjectTrackerConfigOptionsDef1,
            OneOfObjectTrackerConfigOptionsDef2,
        ]
        tracker_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]


    class Payload:
        """
        SD-Routing Object tracker feature schema
        """

        data: ObjecttrackerData
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
        # SD-Routing Object tracker feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceObjecttrackerPayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceObjectTrackerFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ServiceObjecttrackerData:
        delay_down_time: Union[
            OneOfDelayDownTimeOptionsDef1,
            OneOfDelayDownTimeOptionsDef2,
            OneOfDelayDownTimeOptionsDef3,
        ]
        delay_up_time: Union[
            OneOfDelayUpTimeOptionsDef1,
            OneOfDelayUpTimeOptionsDef2,
            OneOfDelayUpTimeOptionsDef3,
        ]
        tracker_config: Union[
            OneOfObjectTrackerConfigOptionsDef1,
            OneOfObjectTrackerConfigOptionsDef2,
        ]
        tracker_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]


    class CreateSdroutingServiceObjectTrackerFeaturePostRequest:
        """
        SD-Routing Object tracker feature schema
        """

        data: ServiceObjecttrackerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingServiceObjecttrackerPayload:
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
        # SD-Routing Object tracker feature schema
        payload: Optional[Payload]


    class EditSdroutingServiceObjectTrackerFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingServiceObjecttrackerData:
        delay_down_time: Union[
            OneOfDelayDownTimeOptionsDef1,
            OneOfDelayDownTimeOptionsDef2,
            OneOfDelayDownTimeOptionsDef3,
        ]
        delay_up_time: Union[
            OneOfDelayUpTimeOptionsDef1,
            OneOfDelayUpTimeOptionsDef2,
            OneOfDelayUpTimeOptionsDef3,
        ]
        tracker_config: Union[
            OneOfObjectTrackerConfigOptionsDef1,
            OneOfObjectTrackerConfigOptionsDef2,
        ]
        tracker_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]


    class EditSdroutingServiceObjectTrackerFeaturePutRequest:
        """
        SD-Routing Object tracker feature schema
        """

        data: SdRoutingServiceObjecttrackerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


