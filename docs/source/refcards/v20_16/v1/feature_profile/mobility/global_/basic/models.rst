======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    UserNameDef = Literal["admin"]

    BasicUserNameDef = Literal["admin"]

    GlobalBasicUserNameDef = Literal["admin"]


    class OneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UserNameDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        # Password should contain atleast 1 uppercase letter, 1 lowercase letter, 1 special character, 1 number and have minimum length of 8 characters and maximum length of 32 characters
        value: Any


    class User:
        name: OneOfUserNameOptionsDef
        password: OneOfUserPasswordOptionsDef


    class BasicData:
        # Create local login account
        user: List[User]


    class Payload:
        """
        AON Basic profile parcel schema for POST request
        """

        data: BasicData
        name: str
        # Set the parcel description
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
        # AON Basic profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListMobilityGlobalBasicPayload:
        data: Optional[List[Data]]


    class CreateBasicProfileParcelForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalBasicData:
        # Create local login account
        user: List[User]


    class CreateBasicProfileParcelForMobilityPostRequest:
        """
        AON Basic profile parcel schema for POST request
        """

        data: GlobalBasicData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class BasicOneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            BasicUserNameDef  # pytype: disable=annotation-type-mismatch
        )


    class BasicOneOfUserPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        # Password should contain atleast 1 uppercase letter, 1 lowercase letter, 1 special character, 1 number and have minimum length of 8 characters and maximum length of 32 characters
        value: Any


    class BasicUser:
        name: BasicOneOfUserNameOptionsDef
        password: BasicOneOfUserPasswordOptionsDef


    class MobilityGlobalBasicData:
        # Create local login account
        user: List[BasicUser]


    class BasicPayload:
        """
        AON Basic profile parcel schema for PUT request
        """

        data: MobilityGlobalBasicData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalBasicPayload:
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
        # AON Basic profile parcel schema for PUT request
        payload: Optional[BasicPayload]


    class EditBasicProfileParcelForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class GlobalBasicOneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: GlobalBasicUserNameDef  # pytype: disable=annotation-type-mismatch


    class GlobalBasicOneOfUserPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        # Password should contain atleast 1 uppercase letter, 1 lowercase letter, 1 special character, 1 number and have minimum length of 8 characters and maximum length of 32 characters
        value: Any


    class GlobalBasicUser:
        name: GlobalBasicOneOfUserNameOptionsDef
        password: GlobalBasicOneOfUserPasswordOptionsDef


    class FeatureProfileMobilityGlobalBasicData:
        # Create local login account
        user: List[GlobalBasicUser]


    class EditBasicProfileParcelForMobilityPutRequest:
        """
        AON Basic profile parcel schema for PUT request
        """

        data: FeatureProfileMobilityGlobalBasicData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


