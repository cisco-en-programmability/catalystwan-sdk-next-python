===================================
v1.feature_profile.nfvirtual.system
===================================


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system
---------------------------------------------------------------


Get all Nfvirtual System Feature Profiles

.. code:: python

    def get_all_nfvirtual_system_feature_profiles(
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
        client.v1.feature_profile.nfvirtual.system.get_all_nfvirtual_system_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system
----------------------------------------------------------------


Create a nfvirtual System Feature Profile

.. code:: python

    def create_nfvirtual_system_feature_profile(
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
        client.v1.feature_profile.nfvirtual.system.create_nfvirtual_system_feature_profile()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
--------------------------------------------------------------------------


Get a Nfvirtual System Feature Profile with systemId

.. code:: python

    def get_nfvirtual_system_feature_profile_by_profile_id(
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
        client.v1.feature_profile.nfvirtual.system.get_nfvirtual_system_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
--------------------------------------------------------------------------


Edit a Nfvirtual System Feature Profile

.. code:: python

    def edit_nfvirtual_system_feature_profile(
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
        client.v1.feature_profile.nfvirtual.system.edit_nfvirtual_system_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
-----------------------------------------------------------------------------


Delete a Nfvirtual System Feature Profile

.. code:: python

    def delete_nfvirtual_system_feature_profile(
        system_id: str,
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
        client.v1.feature_profile.nfvirtual.system.delete_nfvirtual_system_feature_profile()


.. toctree::
    :maxdepth: 1

    aaa
    banner
    logging
    ntp
    snmp
    system_settings

