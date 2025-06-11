======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    ModeDef = Literal["ms-based", "standalone"]

    DefaultModeDef = Literal["ms-based"]

    GpsModeDef = Literal["ms-based", "standalone"]

    GpsDefaultModeDef = Literal["ms-based"]

    TransportGpsModeDef = Literal["ms-based", "standalone"]

    TransportGpsDefaultModeDef = Literal["ms-based"]


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


    class OneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ModeDef


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfNmeaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNmeaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNmeaOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfSourceAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfSourceAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSourceAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDestinationAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfDestinationAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDestinationAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDestinationPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDestinationPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDestinationPortOptionsDef3:
        option_type: DefaultOptionTypeDef


    class GpsData:
        destination_address: Optional[
            Union[
                OneOfDestinationAddressOptionsDef1,
                OneOfDestinationAddressOptionsDef2,
                OneOfDestinationAddressOptionsDef3,
            ]
        ]
        destination_port: Optional[
            Union[
                OneOfDestinationPortOptionsDef1,
                OneOfDestinationPortOptionsDef2,
                OneOfDestinationPortOptionsDef3,
            ]
        ]
        enable: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                OneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                OneOfModeOptionsDef3,
            ]
        ]
        nmea: Optional[
            Union[
                OneOfNmeaOptionsDef1,
                OneOfNmeaOptionsDef2,
                OneOfNmeaOptionsDef3,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSourceAddressOptionsDef1,
                OneOfSourceAddressOptionsDef2,
                OneOfSourceAddressOptionsDef3,
            ]
        ]


    class Payload:
        """
        Gps profile parcel schema for POST request
        """

        data: GpsData
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
        # Gps profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportGpsPayload:
        data: Optional[List[Data]]


    class CreateGpsProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportGpsData:
        destination_address: Optional[
            Union[
                OneOfDestinationAddressOptionsDef1,
                OneOfDestinationAddressOptionsDef2,
                OneOfDestinationAddressOptionsDef3,
            ]
        ]
        destination_port: Optional[
            Union[
                OneOfDestinationPortOptionsDef1,
                OneOfDestinationPortOptionsDef2,
                OneOfDestinationPortOptionsDef3,
            ]
        ]
        enable: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                OneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                OneOfModeOptionsDef3,
            ]
        ]
        nmea: Optional[
            Union[
                OneOfNmeaOptionsDef1,
                OneOfNmeaOptionsDef2,
                OneOfNmeaOptionsDef3,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSourceAddressOptionsDef1,
                OneOfSourceAddressOptionsDef2,
                OneOfSourceAddressOptionsDef3,
            ]
        ]


    class CreateGpsProfileParcelForTransportPostRequest:
        """
        Gps profile parcel schema for POST request
        """

        data: TransportGpsData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GpsOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GpsModeDef


    class GpsOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            GpsDefaultModeDef  # pytype: disable=annotation-type-mismatch
        )


    class SdwanTransportGpsData:
        destination_address: Optional[
            Union[
                OneOfDestinationAddressOptionsDef1,
                OneOfDestinationAddressOptionsDef2,
                OneOfDestinationAddressOptionsDef3,
            ]
        ]
        destination_port: Optional[
            Union[
                OneOfDestinationPortOptionsDef1,
                OneOfDestinationPortOptionsDef2,
                OneOfDestinationPortOptionsDef3,
            ]
        ]
        enable: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                GpsOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                GpsOneOfModeOptionsDef3,
            ]
        ]
        nmea: Optional[
            Union[
                OneOfNmeaOptionsDef1,
                OneOfNmeaOptionsDef2,
                OneOfNmeaOptionsDef3,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSourceAddressOptionsDef1,
                OneOfSourceAddressOptionsDef2,
                OneOfSourceAddressOptionsDef3,
            ]
        ]


    class GpsPayload:
        """
        Gps profile parcel schema for PUT request
        """

        data: SdwanTransportGpsData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanTransportGpsPayload:
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
        # Gps profile parcel schema for PUT request
        payload: Optional[GpsPayload]


    class EditGpsProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportGpsOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportGpsModeDef


    class TransportGpsOneOfModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: TransportGpsDefaultModeDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanTransportGpsData:
        destination_address: Optional[
            Union[
                OneOfDestinationAddressOptionsDef1,
                OneOfDestinationAddressOptionsDef2,
                OneOfDestinationAddressOptionsDef3,
            ]
        ]
        destination_port: Optional[
            Union[
                OneOfDestinationPortOptionsDef1,
                OneOfDestinationPortOptionsDef2,
                OneOfDestinationPortOptionsDef3,
            ]
        ]
        enable: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                TransportGpsOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
                TransportGpsOneOfModeOptionsDef3,
            ]
        ]
        nmea: Optional[
            Union[
                OneOfNmeaOptionsDef1,
                OneOfNmeaOptionsDef2,
                OneOfNmeaOptionsDef3,
            ]
        ]
        source_address: Optional[
            Union[
                OneOfSourceAddressOptionsDef1,
                OneOfSourceAddressOptionsDef2,
                OneOfSourceAddressOptionsDef3,
            ]
        ]


    class EditGpsProfileParcelForTransportPutRequest:
        """
        Gps profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanTransportGpsData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


