======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    ProfileType = Literal["embedded-security"]

    Solution = Literal["sdwan"]


    class GetSdwanEmbeddedSecurityFeatureProfilesGetResponse:
        description: Optional[str]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[ProfileType]
        solution: Optional[Solution]


    class CreateSdwanEmbeddedSecurityFeatureProfilePostResponse:
        """
        Feature Profile POST Response schema
        """

        id: str
        # This is the documentation for POST response schema for feature profile
        documentation: Optional[Any]


    class FromFeatureProfileDef:
        copy: str


    class CreateSdwanEmbeddedSecurityFeatureProfilePostRequest:
        """
        Feature Profile Schema for POST Request
        """

        description: str
        name: str
        # This is the documentation for POST request api schema for feature profile
        documentation: Optional[Any]
        from_feature_profile: Optional[FromFeatureProfileDef]


    class AssociatedProfileParcels:
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        payload: Optional[Any]
        subparcels: Optional[List[Any]]


    class GetSingleSdwanEmbeddedSecurityPayload:
        associated_profile_parcels: Optional[
            List[AssociatedProfileParcels]
        ]
        description: Optional[str]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[ProfileType]
        solution: Optional[Solution]


