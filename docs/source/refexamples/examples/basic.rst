Basic Examples
===============

.. dropdown:: Create client

    .. code-block:: python
        
        from catalystwan.core.client import create_client
            
        with create_client(
            url=SDWAN_URL,
            port=SDWAN_PORT,
            username=SDWAN_USERNAME,
            password=SDWAN_PASSWORD,
        ) as client:
            ...

.. dropdown:: Client Annotation

    For typing purposes, we provide the ApiClient type. It can be used to annotate the client.

    .. code-block:: python

        from __future__ import annotations
        from typing import TYPE_CHECKING
        if TYPE_CHECKING:
            from catalystwan.core.loader import ApiClient
    
        def foo(client: ApiClient):
            ...

.. dropdown:: API calls and Models

    Sending requests is done through the ApiClient object.
    Wherever it is possible, we use dataclass objects for modelling payloads and responses.
    If one of the apis uses such model, it can be conveniently accessed by an ``m`` property of that api. 

    .. code-block:: python

        def create_embedded_security_profile(client: ApiClient) -> str:
            es_api = client.v1.feature_profile.sdwan.embedded_security
            # Access models through m property.
            es = es_api.m.EmbeddedSecurityDefault(name="NAME", description="DESC")
            es_response = es_api.create_sdwan_embedded_security_feature_profile(es)
            return es_response.id
