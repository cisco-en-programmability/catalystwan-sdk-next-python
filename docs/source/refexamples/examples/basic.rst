Basic Examples
===============

Create client
-------------

Snippet below will load version during runtime, based on the SDWAN version it connects to. It will provide type hints for all installed versions.

.. code-block:: python

    from catalystwan.core.client import create_client

    with create_client(
        url=SDWAN_URL,
        port=SDWAN_PORT,
        username=SDWAN_USERNAME,
        password=SDWAN_PASSWORD,
    ) as client:
        ...

If you want to choose version manually (and use type hints for that version alone), you can pass desired ``ApiClient`` version to the ``api_client_class`` argument.

.. note::

    Keep in mind: ``api_client_class`` is a keyword only argument.

.. code-block:: python
    
    from catalystwan.core.client import create_client
    from catalystwan.core.loader import load_client


    with create_client(
        url=SDWAN_URL,
        port=SDWAN_PORT,
        username=SDWAN_USERNAME,
        password=SDWAN_PASSWORD,
        api_client_class=load_client(version="20.15"),
    ) as client:
        ...

Client Annotation
-----------------

For typing purposes, we provide the ApiClient type. It can be used to annotate the client.

.. code-block:: python

    from __future__ import annotations
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from catalystwan.core.loader import ApiClient

    def foo(client: ApiClient):
        ...

API calls and Models
--------------------

Sending requests is done through the ApiClient object.
Wherever it is possible, we use dataclass objects for modelling payloads and responses.
If one of the apis uses such model, it can be conveniently accessed by an ``m`` property of that api.

.. code-block:: python

    def create_embedded_security_profile(client: ApiClient) -> str:
        es_api = client.v1.feature_profile.sdwan.embedded_security
        # Access models through m property.
        es = es_api.m.CreateSdwanEmbeddedSecurityFeatureProfilePostRequest(
            name="NAME",
            description="DESC"
        )
        es_response = es_api.post(es)
        return es_response.id

Device
-------

The easiest way of of finding a device/group of devices with a specific parameter (for example, a hostname or a personality) is to obtain a list of all devices and filter them out.

.. code-block:: python

    def get_device(client: ApiClient, personality="vedge") -> str:
        devices = client.device.get()
        filtered_devices = [device for device in devices if device.personality == personality]

        return filtered_devices
