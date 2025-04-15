======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FullConfigData:
        fullconfig: str


    class Payload:
        """
        Full Config profile parcel schema for POST request
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
        # Full Config profile parcel schema for POST request
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
        Full Config profile parcel schema for POST request
        """

        data: CliFullConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdRoutingCliFullConfigData:
        fullconfig: str


    class FullConfigPayload:
        """
        Full Config profile parcel schema for PUT request
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
        # Full Config profile parcel schema for PUT request
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
        Full Config profile parcel schema for PUT request
        """

        data: FeatureProfileSdRoutingCliFullConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


