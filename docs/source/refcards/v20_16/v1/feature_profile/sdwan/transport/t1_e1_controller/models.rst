======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    TypeDef = Literal["e1", "t1"]

    VariableOptionTypeDef = Literal["variable"]

    Value = Literal["T1"]

    ControllerTxExListFramingT1 = Literal["esf", "sf"]

    DefaultOptionTypeDef = Literal["default"]

    ControllerTxExListLinecodeT1 = Literal["ami", "b8zs"]

    T1E1ControllerValue = Literal["E1"]

    ControllerTxExListFramingE1 = Literal["crc4", "no-crc4"]

    ControllerTxExListLinecodeE1 = Literal["ami", "hdb3"]

    ControllerTxExListClockSource = Literal[
        "internal", "line", "loop-timed", "network"
    ]

    ControllerTxExListLineModeDef = Literal["primary", "secondary"]

    TransportT1E1ControllerValue = Literal["short"]

    ControllerTxExListShortDef = Literal[
        "110ft", "220ft", "330ft", "440ft", "550ft", "660ft"
    ]

    SdwanTransportT1E1ControllerValue = Literal["long"]

    ControllerTxExListLongDef = Literal[
        "-15db", "-22.5db", "-7.5db", "0db"
    ]


    class OneOfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfSlotOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSlotOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Name:
        """
        Card Type
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListFramingOptionsT11:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListFramingT1  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListFramingOptionsT12:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListFramingOptionsT13:
        option_type: DefaultOptionTypeDef


    class OneOfControllerTxExListLinecodeOptionsT11:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListLinecodeT1  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListLinecodeOptionsT12:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListLinecodeOptionsT13:
        option_type: DefaultOptionTypeDef


    class T1:
        # Card Type
        name: Name
        framing: Optional[
            Union[
                OneOfControllerTxExListFramingOptionsT11,
                OneOfControllerTxExListFramingOptionsT12,
                OneOfControllerTxExListFramingOptionsT13,
            ]
        ]
        linecode: Optional[
            Union[
                OneOfControllerTxExListLinecodeOptionsT11,
                OneOfControllerTxExListLinecodeOptionsT12,
                OneOfControllerTxExListLinecodeOptionsT13,
            ]
        ]


    class Basic1:
        t1: T1


    class T1E1ControllerName:
        """
        Card Type
        """

        option_type: GlobalOptionTypeDef
        value: T1E1ControllerValue  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListFramingOptionsE11:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListFramingE1  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListFramingOptionsE12:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListFramingOptionsE13:
        option_type: DefaultOptionTypeDef


    class OneOfControllerTxExListLinecodeOptionsE11:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListLinecodeE1  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListLinecodeOptionsE12:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListLinecodeOptionsE13:
        option_type: DefaultOptionTypeDef


    class E1:
        # Card Type
        name: T1E1ControllerName
        framing: Optional[
            Union[
                OneOfControllerTxExListFramingOptionsE11,
                OneOfControllerTxExListFramingOptionsE12,
                OneOfControllerTxExListFramingOptionsE13,
            ]
        ]
        linecode: Optional[
            Union[
                OneOfControllerTxExListLinecodeOptionsE11,
                OneOfControllerTxExListLinecodeOptionsE12,
                OneOfControllerTxExListLinecodeOptionsE13,
            ]
        ]


    class Basic2:
        e1: E1


    class Cable:
        length_long: Optional[Any]


    class OneOfControllerTxExListClockSourceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListClockSource  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListClockSourceOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfControllerTxExListLineModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListLineModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListLineModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListLineModeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfControllerTxExListDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfControllerTxExListDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfControllerTxExListChannelGroupNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfControllerTxExListChannelGroupNumberOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerTxExListChannelGroupTimeslotsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfControllerTxExListChannelGroupTimeslotsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ChannelGroup:
        number: Union[
            OneOfControllerTxExListChannelGroupNumberOptionsDef1,
            OneOfControllerTxExListChannelGroupNumberOptionsDef2,
        ]
        timeslots: Union[
            OneOfControllerTxExListChannelGroupTimeslotsOptionsDef1,
            OneOfControllerTxExListChannelGroupTimeslotsOptionsDef2,
        ]


    class ControllerTxExList1:
        # Basic Config
        basic: Union[Basic1, Basic2]
        cable: Optional[Cable]
        # Channel Group List
        channel_group: Optional[List[ChannelGroup]]
        clock_source: Optional[
            Union[
                OneOfControllerTxExListClockSourceOptionsDef1,
                OneOfControllerTxExListClockSourceOptionsDef2,
            ]
        ]
        description: Optional[
            Union[
                OneOfControllerTxExListDescriptionOptionsDef1,
                OneOfControllerTxExListDescriptionOptionsDef2,
                OneOfControllerTxExListDescriptionOptionsDef3,
            ]
        ]
        line_mode: Optional[
            Union[
                OneOfControllerTxExListLineModeOptionsDef1,
                OneOfControllerTxExListLineModeOptionsDef2,
                OneOfControllerTxExListLineModeOptionsDef3,
            ]
        ]


    class DefaultOptionNoDefaultDef:
        option_type: DefaultOptionTypeDef


    class Cable1:
        cable_length: Optional[DefaultOptionNoDefaultDef]


    class CableLength:
        """
        Cable Config
        """

        option_type: GlobalOptionTypeDef
        value: TransportT1E1ControllerValue  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListShortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListShortDef  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListShortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Cable2:
        # Cable Config
        cable_length: Optional[CableLength]
        length_short: Optional[
            Union[
                OneOfControllerTxExListShortOptionsDef1,
                OneOfControllerTxExListShortOptionsDef2,
            ]
        ]


    class T1E1ControllerCableLength:
        """
        Cable Config
        """

        option_type: GlobalOptionTypeDef
        value: SdwanTransportT1E1ControllerValue  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListLongOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ControllerTxExListLongDef  # pytype: disable=annotation-type-mismatch


    class OneOfControllerTxExListLongOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Cable3:
        # Cable Config
        cable_length: Optional[T1E1ControllerCableLength]
        length_long: Optional[
            Union[
                OneOfControllerTxExListLongOptionsDef1,
                OneOfControllerTxExListLongOptionsDef2,
            ]
        ]


    class ControllerTxExList2:
        # Basic Config
        basic: Union[Basic1, Basic2]
        # Cable Config
        cable: Optional[Union[Cable1, Cable2, Cable3]]
        # Channel Group List
        channel_group: Optional[List[ChannelGroup]]
        clock_source: Optional[
            Union[
                OneOfControllerTxExListClockSourceOptionsDef1,
                OneOfControllerTxExListClockSourceOptionsDef2,
            ]
        ]
        description: Optional[
            Union[
                OneOfControllerTxExListDescriptionOptionsDef1,
                OneOfControllerTxExListDescriptionOptionsDef2,
                OneOfControllerTxExListDescriptionOptionsDef3,
            ]
        ]
        line_mode: Optional[
            Union[
                OneOfControllerTxExListLineModeOptionsDef1,
                OneOfControllerTxExListLineModeOptionsDef2,
                OneOfControllerTxExListLineModeOptionsDef3,
            ]
        ]


    class T1E1ControllerData:
        # Controller tx-ex List
        controller_tx_ex_list: List[
            Union[ControllerTxExList1, ControllerTxExList2]
        ]
        slot: Union[OneOfSlotOptionsDef1, OneOfSlotOptionsDef2]
        type_: OneOfTypeOptionsDef


    class Payload:
        """
        T1E1Controller profile parcel schema for POST/PUT request
        """

        data: T1E1ControllerData
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
        # T1E1Controller profile parcel schema for POST/PUT request
        payload: Optional[Payload]


    class GetListSdwanTransportT1E1ControllerPayload:
        data: Optional[List[Data]]


    class CreateT1E1ControllerProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportT1E1ControllerData:
        # Controller tx-ex List
        controller_tx_ex_list: List[
            Union[ControllerTxExList1, ControllerTxExList2]
        ]
        slot: Union[OneOfSlotOptionsDef1, OneOfSlotOptionsDef2]
        type_: OneOfTypeOptionsDef


    class CreateT1E1ControllerProfileParcelForTransportPostRequest:
        """
        T1E1Controller profile parcel schema for POST/PUT request
        """

        data: TransportT1E1ControllerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanTransportT1E1ControllerPayload:
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
        # T1E1Controller profile parcel schema for POST/PUT request
        payload: Optional[Payload]


    class EditT1E1ControllerProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanTransportT1E1ControllerData:
        # Controller tx-ex List
        controller_tx_ex_list: List[
            Union[ControllerTxExList1, ControllerTxExList2]
        ]
        slot: Union[OneOfSlotOptionsDef1, OneOfSlotOptionsDef2]
        type_: OneOfTypeOptionsDef


    class EditT1E1ControllerProfileParcelForTransportPutRequest:
        """
        T1E1Controller profile parcel schema for POST/PUT request
        """

        data: SdwanTransportT1E1ControllerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


