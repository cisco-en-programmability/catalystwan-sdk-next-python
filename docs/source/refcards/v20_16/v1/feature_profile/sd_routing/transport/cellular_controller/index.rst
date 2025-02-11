===========================================================
v1.feature_profile.sd_routing.transport.cellular_controller
===========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller
-----------------------------------------------------------------------------------------------------


Get Cellular Controller Profile Features for Transport feature profile

.. code:: python

    def get_cellular_controller_profile_parcel_for_transport_1(
        transport_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.get_cellular_controller_profile_parcel_for_transport_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller
------------------------------------------------------------------------------------------------------


Create a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def create_cellular_controller_profile_parcel_for_transport_1(
        transport_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.create_cellular_controller_profile_parcel_for_transport_1()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
----------------------------------------------------------------------------------------------------------------------------


Get Cellular Controller Profile Feature by parcelId for Transport feature profile

.. code:: python

    def get_cellular_controller_profile_parcel_by_parcel_id_for_transport_1(
        transport_id: str, cellular_controller_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.get_cellular_controller_profile_parcel_by_parcel_id_for_transport_1()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
----------------------------------------------------------------------------------------------------------------------------


Update a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def edit_cellular_controller_profile_parcel_for_transport_1(
        transport_id: str,
        cellular_controller_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.edit_cellular_controller_profile_parcel_for_transport_1()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def delete_cellular_controller_profile_parcel_for_transport_1(
        transport_id: str, cellular_controller_id: str
    ) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.delete_cellular_controller_profile_parcel_for_transport_1()


.. toctree::
    :maxdepth: 1

    cellular_profile
    gps

