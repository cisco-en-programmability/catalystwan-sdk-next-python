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


    class GetListSdwanCliConfigPayload:
        data: Optional[List[Data]]


    class CreateSdwanConfigProfileParcelForCliPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CliConfigData:
        config: str


    class CreateSdwanConfigProfileParcelForCliPostRequest:
        """
        Config profile parcel schema for POST request
        """

        data: CliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class SdwanCliConfigData:
        config: str


    class ConfigPayload:
        """
        Config profile parcel schema for PUT request
        """

        data: SdwanCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanCliConfigPayload:
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


    class EditConfigProfileParcelForCliPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileSdwanCliConfigData:
        config: str


    class EditConfigProfileParcelForCliPutRequest:
        """
        Config profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanCliConfigData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


