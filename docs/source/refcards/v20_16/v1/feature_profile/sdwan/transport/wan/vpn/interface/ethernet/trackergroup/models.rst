======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    TrackGroupBooleanDef = Literal["and", "or"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultTrackGroupBooleanDef = Literal["or"]


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


    class Data:
        combine_boolean: Union[
            OneOfTrackerBooleanOptionsDef1,
            OneOfTrackerBooleanOptionsDef2,
            OneOfTrackerBooleanOptionsDef3,
        ]
        # tracker parcel ref list
        tracker_refs: List[TrackGroupRefDef]


    class Payload:
        """
        TrackerGroup profile parcel schema for common request
        """

        data: Data
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransportGetResponse:
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
        # TrackerGroup profile parcel schema for common request
        payload: Optional[Payload]


    class GetSingleSdwanTransportWanVpnInterfaceEthernetTrackergroupPayload:
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
        # TrackerGroup profile parcel schema for common request
        payload: Optional[Payload]


    class EditWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


