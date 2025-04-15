============================================
v1.feature_profile.sd_routing.system.logging
============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging
------------------------------------------------------------------------------------


Create a SD-Routing Logging Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str, payload: CreateSdroutingLoggingFeaturePostRequest
    ) -> CreateSdroutingLoggingFeaturePostResponse: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sd_routing.system.logging.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
-----------------------------------------------------------------------------------------------


Edit a SD-Routing Logging Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        logging_id: str,
        payload: EditSdroutingLoggingFeaturePutRequest,
    ) -> EditSdroutingLoggingFeaturePutResponse: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sd_routing.system.logging.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
--------------------------------------------------------------------------------------------------


Delete a SD-Routing Logging Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, logging_id: str) -> None: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sd_routing.system.logging.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging
-----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemLoggingSdRoutingPayload: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sd_routing.system.logging.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}
-----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, logging_id: str
    ) -> GetSingleSdRoutingSystemLoggingSdRoutingPayload: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sd_routing.system.logging.get()


.. toctree::
    :maxdepth: 1

    models

