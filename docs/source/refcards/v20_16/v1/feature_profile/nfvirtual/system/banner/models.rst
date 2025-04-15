======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]


    class CreateNfvirtualBannerParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfLoginOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLoginOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLoginOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMotdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMotdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMotdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Data:
        login: Optional[
            Union[
                OneOfLoginOptionsDef1,
                OneOfLoginOptionsDef2,
                OneOfLoginOptionsDef3,
            ]
        ]
        motd: Optional[
            Union[
                OneOfMotdOptionsDef1,
                OneOfMotdOptionsDef2,
                OneOfMotdOptionsDef3,
            ]
        ]


    class CreateNfvirtualBannerParcelPostRequest:
        """
        Banner profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class BannerOneOfLoginOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class BannerOneOfMotdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class BannerData:
        login: Optional[
            Union[
                BannerOneOfLoginOptionsDef1,
                OneOfLoginOptionsDef2,
                OneOfLoginOptionsDef3,
            ]
        ]
        motd: Optional[
            Union[
                BannerOneOfMotdOptionsDef1,
                OneOfMotdOptionsDef2,
                OneOfMotdOptionsDef3,
            ]
        ]


    class Payload:
        """
        Banner profile parcel schema for PUT request
        """

        data: BannerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemBannerPayload:
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
        payload: Optional[Payload]


    class EditNfvirtualBannerParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemBannerOneOfLoginOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemBannerOneOfMotdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemBannerData:
        login: Optional[
            Union[
                SystemBannerOneOfLoginOptionsDef1,
                OneOfLoginOptionsDef2,
                OneOfLoginOptionsDef3,
            ]
        ]
        motd: Optional[
            Union[
                SystemBannerOneOfMotdOptionsDef1,
                OneOfMotdOptionsDef2,
                OneOfMotdOptionsDef3,
            ]
        ]


    class EditNfvirtualBannerParcelPutRequest:
        """
        Banner profile parcel schema for PUT request
        """

        data: SystemBannerData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


