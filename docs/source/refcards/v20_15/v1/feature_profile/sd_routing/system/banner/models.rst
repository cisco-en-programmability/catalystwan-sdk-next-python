======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    EmptyStringDef = Literal[""]


    class OneOfOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: EmptyStringDef  # pytype: disable=annotation-type-mismatch


    class BannerData:
        login: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]
        motd: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]


    class Payload:
        """
        Banner profile parcel schema for POST request
        """

        data: BannerData
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
        # Banner profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingSystemBannerPayload:
        data: Optional[List[Data]]


    class CreateSdroutingBannerFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemBannerData:
        login: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]
        motd: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]


    class CreateSdroutingBannerFeaturePostRequest:
        """
        Banner profile parcel schema for POST request
        """

        data: SystemBannerData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class BannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemBannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingSystemBannerData:
        login: Union[
            OneOfOptionsDef1, BannerOneOfOptionsDef2, OneOfOptionsDef3
        ]
        motd: Union[
            OneOfOptionsDef1,
            SystemBannerOneOfOptionsDef2,
            OneOfOptionsDef3,
        ]


    class BannerPayload:
        """
        Banner profile parcel schema for PUT request
        """

        data: SdRoutingSystemBannerData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemBannerPayload:
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
        # Banner profile parcel schema for PUT request
        payload: Optional[BannerPayload]


    class EditSdroutingBannerFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemBannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingSystemBannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingSystemBannerData:
        login: Union[
            OneOfOptionsDef1,
            SdRoutingSystemBannerOneOfOptionsDef2,
            OneOfOptionsDef3,
        ]
        motd: Union[
            OneOfOptionsDef1,
            FeatureProfileSdRoutingSystemBannerOneOfOptionsDef2,
            OneOfOptionsDef3,
        ]


    class EditSdroutingBannerFeaturePutRequest:
        """
        Banner profile parcel schema for PUT request
        """

        data: FeatureProfileSdRoutingSystemBannerData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


