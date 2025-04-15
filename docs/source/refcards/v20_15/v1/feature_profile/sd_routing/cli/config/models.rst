======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ConfigData:
        config: str


    class Payload:
        """
        Config profile parcel schema for POST request
        """

        data: ConfigData
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
        # Config profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingCliConfigPayload:
        data: Optional[List[Data]]


    class CreateSdroutingCliAddOnFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CliConfigData:
        config: str


    class CreateSdroutingCliAddOnFeaturePostRequest:
        """
        Config profile parcel schema for POST request
        """

        data: CliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdRoutingCliConfigData:
        config: str


    class ConfigPayload:
        """
        Config profile parcel schema for PUT request
        """

        data: SdRoutingCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingCliConfigPayload:
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
        # Config profile parcel schema for PUT request
        payload: Optional[ConfigPayload]


    class EditSdroutingCliAddOnFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileSdRoutingCliConfigData:
        config: str


    class EditSdroutingCliAddOnFeaturePutRequest:
        """
        Config profile parcel schema for PUT request
        """

        data: FeatureProfileSdRoutingCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


