========================================================
v1.feature_profile.sd_routing.system.flexible_port_speed
========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed
------------------------------------------------------------------------------------------------


Create a SD-Routing Flexible Port Speed Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateSdroutingFlexiblePortSpeedFeaturePostRequest,
    ) -> CreateSdroutingFlexiblePortSpeedFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
---------------------------------------------------------------------------------------------------------------------


Edit a SD-Routing Flexible Port Speed Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        flexible_port_speed_id: str,
        payload: EditSdroutingFlexiblePortSpeedFeaturePutRequest,
    ) -> EditSdroutingFlexiblePortSpeedFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
------------------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Flexible Port Speed Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, flexible_port_speed_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed
-----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemFlexiblePortSpeedPayload: ...


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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/flexible-port-speed/{flexiblePortSpeedId}
---------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, flexible_port_speed_id: str
    ) -> GetSingleSdRoutingSystemFlexiblePortSpeedPayload: ...


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
        client.v1.feature_profile.sd_routing.system.flexible_port_speed.get()


.. toctree::
    :maxdepth: 1

    models

