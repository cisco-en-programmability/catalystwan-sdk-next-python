# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Literal, Optional

ProfileType = Literal["embedded-security"]

Solution = Literal["sdwan"]


@dataclass
class GetSdwanEmbeddedSecurityFeatureProfilesGetResponse:
    description: Optional[str] = _field(default=None)
    profile_id: Optional[str] = _field(default=None, metadata={"alias": "profileId"})
    profile_name: Optional[str] = _field(default=None, metadata={"alias": "profileName"})
    profile_type: Optional[ProfileType] = _field(default=None, metadata={"alias": "profileType"})
    solution: Optional[Solution] = _field(default=None)


@dataclass
class Default:
    """
    Feature Profile POST Response schema
    """

    id: str
    # This is the documentation for POST response schema for feature profile
    documentation: Optional[Any] = _field(default=None)


@dataclass
class FromFeatureProfileDef:
    copy: str


@dataclass
class EmbeddedSecurityDefault:
    """
    Feature Profile Schema for POST Request
    """

    description: str
    name: str
    # This is the documentation for POST request api schema for feature profile
    documentation: Optional[Any] = _field(default=None)
    from_feature_profile: Optional[FromFeatureProfileDef] = _field(
        default=None, metadata={"alias": "fromFeatureProfile"}
    )


@dataclass
class AssociatedProfileParcels:
    parcel_id: Optional[str] = _field(default=None, metadata={"alias": "parcelId"})
    parcel_type: Optional[str] = _field(default=None, metadata={"alias": "parcelType"})
    payload: Optional[Any] = _field(default=None)
    subparcels: Optional[List[Any]] = _field(default=None)


@dataclass
class GetSingleSdwanEmbeddedSecurityPayload:
    associated_profile_parcels: Optional[List[AssociatedProfileParcels]] = _field(
        default=None, metadata={"alias": "associatedProfileParcels"}
    )
    description: Optional[str] = _field(default=None)
    profile_id: Optional[str] = _field(default=None, metadata={"alias": "profileId"})
    profile_name: Optional[str] = _field(default=None, metadata={"alias": "profileName"})
    profile_type: Optional[ProfileType] = _field(default=None, metadata={"alias": "profileType"})
    solution: Optional[Solution] = _field(default=None)
