======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class IosConfigData:
        iosconfig: str


    class Payload:
        """
        Ios Classic CLI config feature schema for POST/PUT request
        """

        data: IosConfigData
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
        # Ios Classic CLI config feature schema for POST/PUT request
        payload: Optional[Payload]


    class GetListSdRoutingCliIosConfigPayload:
        data: Optional[List[Data]]


    class CreateSdroutingIosClassicCliAddOnFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CliIosConfigData:
        iosconfig: str


    class CreateSdroutingIosClassicCliAddOnFeaturePostRequest:
        """
        Ios Classic CLI config feature schema for POST/PUT request
        """

        data: CliIosConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingCliIosConfigPayload:
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
        # Ios Classic CLI config feature schema for POST/PUT request
        payload: Optional[Payload]


    class EditSdroutingIosClassicCliAddOnFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingCliIosConfigData:
        iosconfig: str


    class EditSdroutingIosClassicCliAddOnFeaturePutRequest:
        """
        Ios Classic CLI config feature schema for POST/PUT request
        """

        data: SdRoutingCliIosConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


