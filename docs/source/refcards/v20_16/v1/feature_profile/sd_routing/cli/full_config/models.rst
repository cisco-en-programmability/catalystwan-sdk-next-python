======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FullConfigData:
        fullconfig: str


    class Payload:
        """
        Full config feature schema
        """

        data: FullConfigData
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
        # Full config feature schema
        payload: Optional[Payload]


    class GetListSdRoutingCliFullConfigPayload:
        data: Optional[List[Data]]


    class CreateSdroutingCliConfigGroupFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CliFullConfigData:
        fullconfig: str


    class CreateSdroutingCliConfigGroupFeaturePostRequest:
        """
        Full config feature schema
        """

        data: CliFullConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdRoutingCliFullConfigData:
        fullconfig: str


    class FullConfigPayload:
        """
        Full config feature schema
        """

        data: SdRoutingCliFullConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingCliFullConfigPayload:
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
        # Full config feature schema
        payload: Optional[FullConfigPayload]


    class EditSdroutingCliConfigGroupFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileSdRoutingCliFullConfigData:
        fullconfig: str


    class EditSdroutingCliConfigGroupFeaturePutRequest:
        """
        Full config feature schema
        """

        data: FeatureProfileSdRoutingCliFullConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


