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


    class GetListMobilityCliConfigPayload:
        data: Optional[List[Data]]


    class CreateConfigFeatureForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CliConfigData:
        config: str


    class CreateConfigFeatureForMobilityPostRequest:
        """
        Config profile parcel schema for POST request
        """

        data: CliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class MobilityCliConfigData:
        config: str


    class ConfigPayload:
        """
        Config profile parcel schema for PUT request
        """

        data: MobilityCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityCliConfigPayload:
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


    class EditConfigFeatureForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileMobilityCliConfigData:
        config: str


    class EditConfigFeatureForMobilityPutRequest:
        """
        Config profile parcel schema for PUT request
        """

        data: FeatureProfileMobilityCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


