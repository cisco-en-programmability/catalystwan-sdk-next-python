==================================
v1.feature_profile.sdwan.transport
==================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport
--------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_transport_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.transport.get_sdwan_transport_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport
---------------------------------------------------------------


Create a SDWAN Transport Feature Profile

.. code:: python

    def create_sdwan_transport_feature_profile(
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
        client.v1.feature_profile.sdwan.transport.create_sdwan_transport_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}
----------------------------------------------------------------------------


Get a SDWAN Transport Feature Profile with transportId

.. code:: python

    def get_sdwan_transport_feature_profile_by_profile_id(
        transport_id: str,
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.transport.get_sdwan_transport_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}
----------------------------------------------------------------------------


Edit a SDWAN Transport Feature Profile

.. code:: python

    def edit_sdwan_transport_feature_profile(
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
        client.v1.feature_profile.sdwan.transport.edit_sdwan_transport_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}
-------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_transport_feature_profile(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.delete_sdwan_transport_feature_profile()


.. toctree::
    :maxdepth: 1

    cellular_controller/index
    cellular_profile/index
    ipv6_tracker/index
    ipv6_trackergroup/index
    management/index
    routing/index
    t1_e1_controller/index
    tracker/index
    trackergroup/index
    wan/index
    esimcellular_controller
    esimcellular_profile
    gps

