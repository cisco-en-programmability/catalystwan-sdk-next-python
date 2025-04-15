======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    TrackGroupBooleanDef = Literal["and", "or"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultTrackGroupBooleanDef = Literal["or"]


    class OneOfTrackerObjectIdDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerObjectIdDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class TrackGroupRefDef:
        tracker_ref: ParcelReferenceDef


    class OneOfTrackerBooleanOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerBooleanOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TrackGroupBooleanDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackerBooleanOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultTrackGroupBooleanDef  # pytype: disable=annotation-type-mismatch


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


    class ObjecttrackergroupData:
        criteria: Union[
            OneOfTrackerBooleanOptionsDef1,
            OneOfTrackerBooleanOptionsDef2,
            OneOfTrackerBooleanOptionsDef3,
        ]
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
        object_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]
        # Group Tracks ID Refs
        tracker_refs: List[TrackGroupRefDef]


    class Payload:
        """
        SD-Routing object tracker group feature schema
        """

        data: ObjecttrackergroupData
        name: str
        # Feature description
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
        # SD-Routing object tracker group feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportObjecttrackergroupPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportObjectTrackerGroupFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportObjecttrackergroupData:
        criteria: Union[
            OneOfTrackerBooleanOptionsDef1,
            OneOfTrackerBooleanOptionsDef2,
            OneOfTrackerBooleanOptionsDef3,
        ]
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
        object_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]
        # Group Tracks ID Refs
        tracker_refs: List[TrackGroupRefDef]


    class CreateSdroutingTransportObjectTrackerGroupFeaturePostRequest:
        """
        SD-Routing object tracker group feature schema
        """

        data: TransportObjecttrackergroupData
        name: str
        # Feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportObjecttrackergroupPayload:
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
        # SD-Routing object tracker group feature schema
        payload: Optional[Payload]


    class EditSdroutingTransportObjectTrackerGroupFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportObjecttrackergroupData:
        criteria: Union[
            OneOfTrackerBooleanOptionsDef1,
            OneOfTrackerBooleanOptionsDef2,
            OneOfTrackerBooleanOptionsDef3,
        ]
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
        object_id: Union[
            OneOfTrackerObjectIdDef1, OneOfTrackerObjectIdDef2
        ]
        # Group Tracks ID Refs
        tracker_refs: List[TrackGroupRefDef]


    class EditSdroutingTransportObjectTrackerGroupFeaturePutRequest:
        """
        SD-Routing object tracker group feature schema
        """

        data: SdRoutingTransportObjecttrackergroupData
        name: str
        # Feature description
        description: Optional[str]
        metadata: Optional[Any]


