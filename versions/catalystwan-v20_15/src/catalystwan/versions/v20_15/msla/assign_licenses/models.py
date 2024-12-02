# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class AssignMslaLicensesBaseLicense:
    billing_type: Optional[str] = _field(default=None)
    license_type: Optional[str] = _field(default=None)
    sa_id: Optional[str] = _field(default=None, metadata={"alias": "saId"})
    subscription_id: Optional[str] = _field(default=None)
    tag: Optional[str] = _field(default=None)
    va_id: Optional[str] = _field(default=None, metadata={"alias": "vaId"})


@dataclass
class AssignMslaLicensesTenantLicense:
    billing_type: Optional[str] = _field(default=None)
    count: Optional[int] = _field(default=None)
    license_type: Optional[str] = _field(default=None)
    sa_id: Optional[str] = _field(default=None, metadata={"alias": "saId"})
    subscription_id: Optional[str] = _field(default=None)
    tag: Optional[str] = _field(default=None)
    va_id: Optional[str] = _field(default=None, metadata={"alias": "vaId"})


@dataclass
class AssignMslaLicenses:
    base_license: Optional[AssignMslaLicensesBaseLicense] = _field(
        default=None, metadata={"alias": "baseLicense"}
    )
    tenant_license: Optional[List[AssignMslaLicensesTenantLicense]] = _field(
        default=None, metadata={"alias": "tenantLicense"}
    )
    uuid: Optional[List[str]] = _field(default=None)
