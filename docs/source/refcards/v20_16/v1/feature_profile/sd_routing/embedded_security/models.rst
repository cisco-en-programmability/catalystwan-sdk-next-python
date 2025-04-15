======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ProfileType = Literal["embedded-security"]

    Solution = Literal["sd-routing"]


    class GetSdRoutingEmbeddedSecurityFeatureProfilesGetResponse:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        description: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[ProfileType]
        solution: Optional[Solution]


    class CreateSdRoutingEmbeddedSecurityFeatureProfilePostResponse:
        """
        Feature Profile POST Response schema
        """

        id: str


    class FromFeatureProfileDef:
        copy: str


    class CreateSdRoutingEmbeddedSecurityFeatureProfilePostRequest:
        """
        Feature Profile Schema for POST Request
        """

        description: str
        name: str
        from_feature_profile: Optional[FromFeatureProfileDef]


    class AssociatedProfileParcels:
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        payload: Optional[Any]
        subparcels: Optional[List[Any]]


    class GetSingleSdRoutingEmbeddedSecurityPayload:
        associated_profile_parcels: Optional[
            List[AssociatedProfileParcels]
        ]
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        description: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[ProfileType]
        solution: Optional[Solution]


    class EditSdRoutingEmbeddedSecurityFeatureProfilePutResponse:
        """
        Feature Profile PUT Response schema
        """

        id: str


    class EditSdRoutingEmbeddedSecurityFeatureProfilePutRequest:
        """
        Feature Profile Schema for PUT Request
        """

        description: str
        name: str


