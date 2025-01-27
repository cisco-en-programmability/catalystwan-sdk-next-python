======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    ClaimStatusParam = Literal["claimed", "unclaimed"]


    class SigningKeyCdendpointsControllerDelete:
        url: Optional[str]


    class SigningKeyCdendpoints:
        controller_delete: Optional[SigningKeyCdendpointsControllerDelete]


    class SigningKeyCdtrustfedKeys:
        crv: Optional[str]
        kty: Optional[str]
        x: Optional[str]
        y: Optional[str]


    class SigningKeyCdtrustfedJwks:
        issuer: Optional[str]
        keys: Optional[SigningKeyCdtrustfedKeys]
        public_key: Optional[str]


    class SigningKeyCdtrustfedKongTlsCert:
        tls_cert: Optional[str]


    class SigningKeyCdtrustfed:
        jwks: Optional[List[SigningKeyCdtrustfedJwks]]
        kong_tls_cert: Optional[List[SigningKeyCdtrustfedKongTlsCert]]


    class SigningKey:
        cd_end_points: Optional[SigningKeyCdendpoints]
        cd_fqdn: Optional[str]
        cd_trust_fed: Optional[SigningKeyCdtrustfed]


