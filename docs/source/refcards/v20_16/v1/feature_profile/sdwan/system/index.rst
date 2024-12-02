===============================
v1.feature_profile.sdwan.system
===============================


Operation: GET /dataservice/v1/feature-profile/sdwan/system
-----------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_system_feature_profiles(
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
        client.v1.feature_profile.sdwan.system.get_sdwan_system_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/system
------------------------------------------------------------


Create a SDWAN System Feature Profile

.. code:: python

    def create_sdwan_system_feature_profile(
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
        client.v1.feature_profile.sdwan.system.create_sdwan_system_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}
----------------------------------------------------------------------


Get a SDWAN System Feature Profile with systemId

.. code:: python

    def get_sdwan_system_feature_profile_by_profile_id(
        system_id: str,
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
        client.v1.feature_profile.sdwan.system.get_sdwan_system_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}
----------------------------------------------------------------------


Edit a SDWAN System Feature Profile

.. code:: python

    def edit_sdwan_system_feature_profile(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.edit_sdwan_system_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}
-------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_system_feature_profile(system_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.delete_sdwan_system_feature_profile()


.. toctree::
    :maxdepth: 1

    aaa/index
    banner/index
    basic/index
    bfd/index
    global_/index
    logging/index
    mrf/index
    ntp/index
    omp/index
    snmp/index
    security

