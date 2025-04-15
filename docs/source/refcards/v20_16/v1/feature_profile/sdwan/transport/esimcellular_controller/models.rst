======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    RefTypeDef = Literal["esimcellular-profile"]

    EsimcellularControllerRefTypeDef = Literal["esimcellular-profile"]

    TransportEsimcellularControllerRefTypeDef = Literal[
        "esimcellular-profile"
    ]

    SdwanTransportEsimcellularControllerRefTypeDef = Literal[
        "esimcellular-profile"
    ]

    FeatureProfileSdwanTransportEsimcellularControllerRefTypeDef = (
        Literal["esimcellular-profile"]
    )


    class OneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEsimSlotOptionsDef:
        option_type: DefaultOptionTypeDef
        value: int


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
        value: bool


    class EsimControllerConfigDef:
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
        slot: Optional[OneOfEsimSlotOptionsDef]


    class RefIdOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RefTypeOptionDef:
        option_type: DefaultOptionTypeDef
        value: RefTypeDef  # pytype: disable=annotation-type-mismatch


    class ProfileRefOptionDef:
        ref_id: RefIdOptionDef
        ref_type: RefTypeOptionDef


    class CommonSlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        attach_profile: ProfileRefOptionDef
        data_profile: Optional[ProfileRefOptionDef]


    class SlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        # Set the slot specific attach and data profile feature ids
        slot0_config: CommonSlotConfigDef


    class EsimControllerConfigOptionDef:
        """
        eSim Cellular controller config
        """

        controller_config: EsimControllerConfigDef
        # Set the slot specific attach and data profile feature ids
        slot_config: SlotConfigDef


    class Payload:
        """
        eSimCellularController feature schema for POST request
        """

        # eSim Cellular controller config
        data: EsimControllerConfigOptionDef
        name: str
        # Set the eSimCellularController feature schema description
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
        # eSimCellularController feature schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportEsimcellularControllerPayload:
        data: Optional[List[Data]]


    class CreateEsimCellularControllerProfileFeatureForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateEsimCellularControllerProfileFeatureForTransportPostRequest:
        """
        eSimCellularController feature schema for POST request
        """

        # eSim Cellular controller config
        data: EsimControllerConfigOptionDef
        name: str
        # Set the eSimCellularController feature schema description
        description: Optional[str]
        metadata: Optional[Any]


    class EsimcellularControllerOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularControllerOneOfMaxRetryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EsimcellularControllerOneOfFailovertimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EsimcellularControllerEsimControllerConfigDef:
        id: Union[
            EsimcellularControllerOneOfIdOptionsDef1, OneOfIdOptionsDef2
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
                EsimcellularControllerOneOfFailovertimerOptionsDef1,
                OneOfFailovertimerOptionsDef2,
                OneOfFailovertimerOptionsDef3,
            ]
        ]
        max_retry: Optional[
            Union[
                EsimcellularControllerOneOfMaxRetryOptionsDef1,
                OneOfMaxRetryOptionsDef2,
                OneOfMaxRetryOptionsDef3,
            ]
        ]
        slot: Optional[OneOfEsimSlotOptionsDef]


    class EsimcellularControllerRefTypeOptionDef:
        option_type: DefaultOptionTypeDef
        value: EsimcellularControllerRefTypeDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularControllerProfileRefOptionDef:
        ref_id: RefIdOptionDef
        ref_type: EsimcellularControllerRefTypeOptionDef


    class TransportEsimcellularControllerRefTypeOptionDef:
        option_type: DefaultOptionTypeDef
        value: TransportEsimcellularControllerRefTypeDef  # pytype: disable=annotation-type-mismatch


    class TransportEsimcellularControllerProfileRefOptionDef:
        ref_id: RefIdOptionDef
        ref_type: TransportEsimcellularControllerRefTypeOptionDef


    class EsimcellularControllerCommonSlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        attach_profile: EsimcellularControllerProfileRefOptionDef
        data_profile: Optional[
            TransportEsimcellularControllerProfileRefOptionDef
        ]


    class EsimcellularControllerSlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        # Set the slot specific attach and data profile feature ids
        slot0_config: EsimcellularControllerCommonSlotConfigDef


    class EsimcellularControllerEsimControllerConfigOptionDef:
        """
        eSim Cellular controller config
        """

        controller_config: EsimcellularControllerEsimControllerConfigDef
        # Set the slot specific attach and data profile feature ids
        slot_config: EsimcellularControllerSlotConfigDef


    class EsimcellularControllerPayload:
        """
        eSimCellularController feature schema for PUT request
        """

        # eSim Cellular controller config
        data: EsimcellularControllerEsimControllerConfigOptionDef
        name: str
        # Set the eSimCellularController feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportEsimcellularControllerPayload:
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
        # eSimCellularController feature schema for PUT request
        payload: Optional[EsimcellularControllerPayload]


    class EditEsimCellularControllerProfileFeatureForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportEsimcellularControllerOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportEsimcellularControllerOneOfMaxRetryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportEsimcellularControllerOneOfFailovertimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportEsimcellularControllerEsimControllerConfigDef:
        id: Union[
            TransportEsimcellularControllerOneOfIdOptionsDef1,
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
                TransportEsimcellularControllerOneOfFailovertimerOptionsDef1,
                OneOfFailovertimerOptionsDef2,
                OneOfFailovertimerOptionsDef3,
            ]
        ]
        max_retry: Optional[
            Union[
                TransportEsimcellularControllerOneOfMaxRetryOptionsDef1,
                OneOfMaxRetryOptionsDef2,
                OneOfMaxRetryOptionsDef3,
            ]
        ]
        slot: Optional[OneOfEsimSlotOptionsDef]


    class SdwanTransportEsimcellularControllerRefTypeOptionDef:
        option_type: DefaultOptionTypeDef
        value: SdwanTransportEsimcellularControllerRefTypeDef  # pytype: disable=annotation-type-mismatch


    class SdwanTransportEsimcellularControllerProfileRefOptionDef:
        ref_id: RefIdOptionDef
        ref_type: SdwanTransportEsimcellularControllerRefTypeOptionDef


    class FeatureProfileSdwanTransportEsimcellularControllerRefTypeOptionDef:
        option_type: DefaultOptionTypeDef
        value: FeatureProfileSdwanTransportEsimcellularControllerRefTypeDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanTransportEsimcellularControllerProfileRefOptionDef:
        ref_id: RefIdOptionDef
        ref_type: FeatureProfileSdwanTransportEsimcellularControllerRefTypeOptionDef


    class TransportEsimcellularControllerCommonSlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        attach_profile: (
            SdwanTransportEsimcellularControllerProfileRefOptionDef
        )
        data_profile: Optional[
            FeatureProfileSdwanTransportEsimcellularControllerProfileRefOptionDef
        ]


    class TransportEsimcellularControllerSlotConfigDef:
        """
        Set the slot specific attach and data profile feature ids
        """

        # Set the slot specific attach and data profile feature ids
        slot0_config: TransportEsimcellularControllerCommonSlotConfigDef


    class TransportEsimcellularControllerEsimControllerConfigOptionDef:
        """
        eSim Cellular controller config
        """

        controller_config: (
            TransportEsimcellularControllerEsimControllerConfigDef
        )
        # Set the slot specific attach and data profile feature ids
        slot_config: TransportEsimcellularControllerSlotConfigDef


    class EditEsimCellularControllerProfileFeatureForTransportPutRequest:
        """
        eSimCellularController feature schema for PUT request
        """

        # eSim Cellular controller config
        data: TransportEsimcellularControllerEsimControllerConfigOptionDef
        name: str
        # Set the eSimCellularController feature description
        description: Optional[str]
        metadata: Optional[Any]


