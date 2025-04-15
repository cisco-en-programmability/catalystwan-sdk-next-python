======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    ColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    BfdColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    SystemBfdColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]


    class OneOfMultiplierOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMultiplierOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPollIntervalOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPollIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPollIntervalOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDefaultDscpOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDefaultDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDefaultDscpOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfColorOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfColorOptions2:
        option_type: GlobalOptionTypeDef
        value: ColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfHelloIntervalOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloIntervalOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfColorMultiplierOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfColorMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfColorMultiplierOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPmtuDiscoveryOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPmtuDiscoveryOptions2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPmtuDiscoveryOptions3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfColorDscpOptions1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfColorDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfColorDscpOptions3:
        option_type: DefaultOptionTypeDef
        value: int


    class Colors:
        color: Union[OneOfColorOptions1, OneOfColorOptions2]
        dscp: Union[
            OneOfColorDscpOptions1,
            OneOfColorDscpOptions2,
            OneOfColorDscpOptions3,
        ]
        hello_interval: Union[
            OneOfHelloIntervalOptions1,
            OneOfHelloIntervalOptions2,
            OneOfHelloIntervalOptions3,
        ]
        multiplier: Union[
            OneOfColorMultiplierOptions1,
            OneOfColorMultiplierOptions2,
            OneOfColorMultiplierOptions3,
        ]
        pmtu_discovery: Union[
            OneOfPmtuDiscoveryOptions1,
            OneOfPmtuDiscoveryOptions2,
            OneOfPmtuDiscoveryOptions3,
        ]


    class BfdData:
        default_dscp: Union[
            OneOfDefaultDscpOptions1,
            OneOfDefaultDscpOptions2,
            OneOfDefaultDscpOptions3,
        ]
        multiplier: Union[
            OneOfMultiplierOptions1,
            OneOfMultiplierOptions2,
            OneOfMultiplierOptions3,
        ]
        poll_interval: Union[
            OneOfPollIntervalOptions1,
            OneOfPollIntervalOptions2,
            OneOfPollIntervalOptions3,
        ]
        # Set color that identifies the WAN transport tunnel
        colors: Optional[List[Colors]]


    class Payload:
        """
        BFD profile parcel schema for POST request
        """

        data: BfdData
        name: str
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
        # BFD profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemBfdPayload:
        data: Optional[List[Data]]


    class CreateBfdProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemBfdData:
        default_dscp: Union[
            OneOfDefaultDscpOptions1,
            OneOfDefaultDscpOptions2,
            OneOfDefaultDscpOptions3,
        ]
        multiplier: Union[
            OneOfMultiplierOptions1,
            OneOfMultiplierOptions2,
            OneOfMultiplierOptions3,
        ]
        poll_interval: Union[
            OneOfPollIntervalOptions1,
            OneOfPollIntervalOptions2,
            OneOfPollIntervalOptions3,
        ]
        # Set color that identifies the WAN transport tunnel
        colors: Optional[List[Colors]]


    class CreateBfdProfileParcelForSystemPostRequest:
        """
        BFD profile parcel schema for POST request
        """

        data: SystemBfdData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class BfdOneOfMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdOneOfPollIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdOneOfDefaultDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdOneOfColorOptions2:
        option_type: GlobalOptionTypeDef
        value: BfdColorDef  # pytype: disable=annotation-type-mismatch


    class BfdOneOfHelloIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdOneOfColorMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdOneOfColorDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class BfdColors:
        color: Union[OneOfColorOptions1, BfdOneOfColorOptions2]
        dscp: Union[
            OneOfColorDscpOptions1,
            BfdOneOfColorDscpOptions2,
            OneOfColorDscpOptions3,
        ]
        hello_interval: Union[
            OneOfHelloIntervalOptions1,
            BfdOneOfHelloIntervalOptions2,
            OneOfHelloIntervalOptions3,
        ]
        multiplier: Union[
            OneOfColorMultiplierOptions1,
            BfdOneOfColorMultiplierOptions2,
            OneOfColorMultiplierOptions3,
        ]
        pmtu_discovery: Union[
            OneOfPmtuDiscoveryOptions1,
            OneOfPmtuDiscoveryOptions2,
            OneOfPmtuDiscoveryOptions3,
        ]


    class SdwanSystemBfdData:
        default_dscp: Union[
            OneOfDefaultDscpOptions1,
            BfdOneOfDefaultDscpOptions2,
            OneOfDefaultDscpOptions3,
        ]
        multiplier: Union[
            OneOfMultiplierOptions1,
            BfdOneOfMultiplierOptions2,
            OneOfMultiplierOptions3,
        ]
        poll_interval: Union[
            OneOfPollIntervalOptions1,
            BfdOneOfPollIntervalOptions2,
            OneOfPollIntervalOptions3,
        ]
        # Set color that identifies the WAN transport tunnel
        colors: Optional[List[BfdColors]]


    class BfdPayload:
        """
        BFD profile parcel schema for PUT request
        """

        data: SdwanSystemBfdData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemBfdPayload:
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
        # BFD profile parcel schema for PUT request
        payload: Optional[BfdPayload]


    class EditBfdProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemBfdOneOfMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdOneOfPollIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdOneOfDefaultDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdOneOfColorOptions2:
        option_type: GlobalOptionTypeDef
        value: (
            SystemBfdColorDef  # pytype: disable=annotation-type-mismatch
        )


    class SystemBfdOneOfHelloIntervalOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdOneOfColorMultiplierOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdOneOfColorDscpOptions2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBfdColors:
        color: Union[OneOfColorOptions1, SystemBfdOneOfColorOptions2]
        dscp: Union[
            OneOfColorDscpOptions1,
            SystemBfdOneOfColorDscpOptions2,
            OneOfColorDscpOptions3,
        ]
        hello_interval: Union[
            OneOfHelloIntervalOptions1,
            SystemBfdOneOfHelloIntervalOptions2,
            OneOfHelloIntervalOptions3,
        ]
        multiplier: Union[
            OneOfColorMultiplierOptions1,
            SystemBfdOneOfColorMultiplierOptions2,
            OneOfColorMultiplierOptions3,
        ]
        pmtu_discovery: Union[
            OneOfPmtuDiscoveryOptions1,
            OneOfPmtuDiscoveryOptions2,
            OneOfPmtuDiscoveryOptions3,
        ]


    class FeatureProfileSdwanSystemBfdData:
        default_dscp: Union[
            OneOfDefaultDscpOptions1,
            SystemBfdOneOfDefaultDscpOptions2,
            OneOfDefaultDscpOptions3,
        ]
        multiplier: Union[
            OneOfMultiplierOptions1,
            SystemBfdOneOfMultiplierOptions2,
            OneOfMultiplierOptions3,
        ]
        poll_interval: Union[
            OneOfPollIntervalOptions1,
            SystemBfdOneOfPollIntervalOptions2,
            OneOfPollIntervalOptions3,
        ]
        # Set color that identifies the WAN transport tunnel
        colors: Optional[List[SystemBfdColors]]


    class EditBfdProfileParcelForSystemPutRequest:
        """
        BFD profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemBfdData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


