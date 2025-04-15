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
        Banner feature schema
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
        # Banner feature schema
        payload: Optional[Payload]


    class GetListSdwanSystemBannerPayload:
        data: Optional[List[Data]]


    class CreateBannerProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemBannerData:
        login: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]
        motd: Union[OneOfOptionsDef1, OneOfOptionsDef2, OneOfOptionsDef3]


    class CreateBannerProfileParcelForSystemPostRequest:
        """
        Banner feature schema
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


    class SdwanSystemBannerData:
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
        Banner feature schema
        """

        data: SdwanSystemBannerData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemBannerPayload:
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
        # Banner feature schema
        payload: Optional[BannerPayload]


    class EditBannerProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanSystemBannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanSystemBannerOneOfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanSystemBannerData:
        login: Union[
            OneOfOptionsDef1,
            SdwanSystemBannerOneOfOptionsDef2,
            OneOfOptionsDef3,
        ]
        motd: Union[
            OneOfOptionsDef1,
            FeatureProfileSdwanSystemBannerOneOfOptionsDef2,
            OneOfOptionsDef3,
        ]


    class EditBannerProfileParcelForSystemPutRequest:
        """
        Banner feature schema
        """

        data: FeatureProfileSdwanSystemBannerData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


