# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Literal, Optional, Union

GlobalOptionTypeDef = Literal["global"]

VariableOptionTypeDef = Literal["variable"]

DefaultOptionTypeDef = Literal["default"]


@dataclass
class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
    parcel_id: Optional[str] = _field(default=None, metadata={"alias": "parcelId"})


@dataclass
class OneOfDescriptionOptionsDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfDescriptionOptionsDef2:
    option_type: VariableOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str
    default: Optional[str] = _field(default=None)
    description: Optional[str] = _field(default=None)


@dataclass
class OneOfDescriptionOptionsDef3:
    option_type: DefaultOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch


@dataclass
class OneOfEntriesAddressTypeHostOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: Any


@dataclass
class OneOfEntriesHostOptionsDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: Any


@dataclass
class Entries1:
    address_type: OneOfEntriesAddressTypeHostOptionsDef = _field(metadata={"alias": "addressType"})
    host: Union[OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2]


@dataclass
class OneOfEntriesAddressTypeIpPrefixOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: Any


@dataclass
class OneOfEntriesIpPrefixOptionsDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class Entries2:
    address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef = _field(
        metadata={"alias": "addressType"}
    )
    ip_prefix: Union[OneOfEntriesIpPrefixOptionsDef1, OneOfDescriptionOptionsDef2] = _field(
        metadata={"alias": "ipPrefix"}
    )


@dataclass
class OneOfEntriesAddressTypeObjectGroupOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: Any


@dataclass
class RefId:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class ParcelReferenceDef:
    ref_id: RefId = _field(metadata={"alias": "refId"})


@dataclass
class Entries3:
    address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef = _field(
        metadata={"alias": "addressType"}
    )
    object_group: ParcelReferenceDef = _field(metadata={"alias": "objectGroup"})


@dataclass
class OneOfEntriesAddressTypeHostRangeOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: Any


@dataclass
class HostRange:
    """
    Host Address Range
    """

    end: Union[OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2]
    start: Union[OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2]


@dataclass
class Entries4:
    address_type: OneOfEntriesAddressTypeHostRangeOptionsDef = _field(
        metadata={"alias": "addressType"}
    )
    # Host Address Range
    host_range: HostRange = _field(metadata={"alias": "hostRange"})


@dataclass
class Data:
    # object-group Entries
    entries: List[Union[Entries1, Entries2, Entries3, Entries4]]
    description: Optional[
        Union[OneOfDescriptionOptionsDef1, OneOfDescriptionOptionsDef2, OneOfDescriptionOptionsDef3]
    ] = _field(default=None)


@dataclass
class Default:
    """
    Ipv4 Network Object Group profile parcel schema
    """

    data: Data
    name: str
    description: Optional[str] = _field(default=None)
    # This is the documentation for POST/PUT request schema for Ipv4 Network Object Group profile parcel
    documentation: Optional[Any] = _field(default=None)
    metadata: Optional[Any] = _field(default=None)


@dataclass
class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
    created_by: Optional[str] = _field(default=None, metadata={"alias": "createdBy"})
    created_on: Optional[int] = _field(default=None, metadata={"alias": "createdOn"})
    last_updated_by: Optional[str] = _field(default=None, metadata={"alias": "lastUpdatedBy"})
    last_updated_on: Optional[int] = _field(default=None, metadata={"alias": "lastUpdatedOn"})
    parcel_id: Optional[str] = _field(default=None, metadata={"alias": "parcelId"})
    parcel_type: Optional[str] = _field(default=None, metadata={"alias": "parcelType"})
    # Ipv4 Network Object Group profile parcel schema
    payload: Optional[Default] = _field(default=None)
