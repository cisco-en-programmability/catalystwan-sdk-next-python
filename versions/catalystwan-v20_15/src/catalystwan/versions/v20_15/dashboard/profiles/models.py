# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import List, Literal, Optional

ClaimStatusParam = Literal["claimed", "unclaimed"]


@dataclass
class SigningKeyCdendpointsControllerDelete:
    url: Optional[str] = _field(default=None)


@dataclass
class SigningKeyCdendpoints:
    controller_delete: Optional[SigningKeyCdendpointsControllerDelete] = _field(
        default=None, metadata={"alias": "controllerDelete"}
    )


@dataclass
class SigningKeyCdtrustfedKeys:
    crv: Optional[str] = _field(default=None)
    kty: Optional[str] = _field(default=None)
    x: Optional[str] = _field(default=None)
    y: Optional[str] = _field(default=None)


@dataclass
class SigningKeyCdtrustfedJwks:
    issuer: Optional[str] = _field(default=None)
    keys: Optional[SigningKeyCdtrustfedKeys] = _field(default=None)
    public_key: Optional[str] = _field(default=None)


@dataclass
class SigningKeyCdtrustfedKongTlsCert:
    tls_cert: Optional[str] = _field(default=None)


@dataclass
class SigningKeyCdtrustfed:
    jwks: Optional[List[SigningKeyCdtrustfedJwks]] = _field(default=None)
    kong_tls_cert: Optional[List[SigningKeyCdtrustfedKongTlsCert]] = _field(default=None)


@dataclass
class SigningKey:
    cd_end_points: Optional[SigningKeyCdendpoints] = _field(default=None, metadata={"alias": "cd-end-points"})
    cd_fqdn: Optional[str] = _field(default=None, metadata={"alias": "cd-fqdn"})
    cd_trust_fed: Optional[SigningKeyCdtrustfed] = _field(default=None, metadata={"alias": "cd-trust-fed"})
