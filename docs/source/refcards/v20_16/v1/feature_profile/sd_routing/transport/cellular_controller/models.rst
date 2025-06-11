======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["non-eSim"]

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    BooleanTrueDef = Literal[True]


    class ConfigType:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSlotOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSlotOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSlotOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMaxRetryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxRetryOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxRetryOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfFailovertimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfFailovertimerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfFailovertimerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAutoSimOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAutoSimOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAutoSimOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class CommonControllerConfigDef:
        id: Union[OneOfIdOptionsDef1, OneOfIdOptionsDef2]
        auto_sim: Optional[
            Union[
                OneOfAutoSimOptionsDef1,
                OneOfAutoSimOptionsDef2,
                OneOfAutoSimOptionsDef3,
            ]
        ]
        failovertimer: Optional[
            Union[
                OneOfFailovertimerOptionsDef1,
                OneOfFailovertimerOptionsDef2,
                OneOfFailovertimerOptionsDef3,
            ]
        ]
        max_retry: Optional[
            Union[
                OneOfMaxRetryOptionsDef1,
                OneOfMaxRetryOptionsDef2,
                OneOfMaxRetryOptionsDef3,
            ]
        ]
        slot: Optional[
            Union[
                OneOfSlotOptionsDef1,
                OneOfSlotOptionsDef2,
                OneOfSlotOptionsDef3,
            ]
        ]


    class NonEsimControllerConfigDef:
        """
        Regular Cellular controller (non-eSim) config
        """

        config_type: ConfigType
        controller_config: CommonControllerConfigDef


    class Payload:
        """
        CellularController profile parcel schema for POST request
        """

        data: NonEsimControllerConfigDef
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
        # CellularController profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingTransportCellularControllerPayload:
        data: Optional[List[Data]]


    class CreateCellularControllerProfileParcelForTransport1PostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateCellularControllerProfileParcelForTransport1PostRequest:
        """
        CellularController profile parcel schema for POST request
        """

        data: NonEsimControllerConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class CellularControllerOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularControllerOneOfSlotOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularControllerOneOfMaxRetryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularControllerOneOfFailovertimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularControllerCommonControllerConfigDef:
        id: Union[
            CellularControllerOneOfIdOptionsDef1, OneOfIdOptionsDef2
        ]
        auto_sim: Optional[
            Union[
                OneOfAutoSimOptionsDef1,
                OneOfAutoSimOptionsDef2,
                OneOfAutoSimOptionsDef3,
            ]
        ]
        failovertimer: Optional[
            Union[
                CellularControllerOneOfFailovertimerOptionsDef1,
                OneOfFailovertimerOptionsDef2,
                OneOfFailovertimerOptionsDef3,
            ]
        ]
        max_retry: Optional[
            Union[
                CellularControllerOneOfMaxRetryOptionsDef1,
                OneOfMaxRetryOptionsDef2,
                OneOfMaxRetryOptionsDef3,
            ]
        ]
        slot: Optional[
            Union[
                CellularControllerOneOfSlotOptionsDef1,
                OneOfSlotOptionsDef2,
                OneOfSlotOptionsDef3,
            ]
        ]


    class CellularControllerNonEsimControllerConfigDef:
        """
        Regular Cellular controller (non-eSim) config
        """

        config_type: ConfigType
        controller_config: CellularControllerCommonControllerConfigDef


    class CellularControllerPayload:
        """
        CellularController profile parcel schema for PUT request
        """

        data: CellularControllerNonEsimControllerConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportCellularControllerPayload:
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
        # CellularController profile parcel schema for PUT request
        payload: Optional[CellularControllerPayload]


    class EditCellularControllerProfileParcelForTransport1PutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportCellularControllerOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportCellularControllerOneOfSlotOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportCellularControllerOneOfMaxRetryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportCellularControllerOneOfFailovertimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportCellularControllerCommonControllerConfigDef:
        id: Union[
            TransportCellularControllerOneOfIdOptionsDef1,
            OneOfIdOptionsDef2,
        ]
        auto_sim: Optional[
            Union[
                OneOfAutoSimOptionsDef1,
                OneOfAutoSimOptionsDef2,
                OneOfAutoSimOptionsDef3,
            ]
        ]
        failovertimer: Optional[
            Union[
                TransportCellularControllerOneOfFailovertimerOptionsDef1,
                OneOfFailovertimerOptionsDef2,
                OneOfFailovertimerOptionsDef3,
            ]
        ]
        max_retry: Optional[
            Union[
                TransportCellularControllerOneOfMaxRetryOptionsDef1,
                OneOfMaxRetryOptionsDef2,
                OneOfMaxRetryOptionsDef3,
            ]
        ]
        slot: Optional[
            Union[
                TransportCellularControllerOneOfSlotOptionsDef1,
                OneOfSlotOptionsDef2,
                OneOfSlotOptionsDef3,
            ]
        ]


    class TransportCellularControllerNonEsimControllerConfigDef:
        """
        Regular Cellular controller (non-eSim) config
        """

        config_type: ConfigType
        controller_config: (
            TransportCellularControllerCommonControllerConfigDef
        )


    class EditCellularControllerProfileParcelForTransport1PutRequest:
        """
        CellularController profile parcel schema for PUT request
        """

        data: TransportCellularControllerNonEsimControllerConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


