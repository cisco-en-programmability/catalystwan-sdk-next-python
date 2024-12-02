==================
dashboard.profiles
==================


Operation: GET /dataservice/dashboard/profiles
----------------------------------------------


Retrieve CD profiles from CRS

.. code:: python

    def list_cd_profiles(
        claim_status: Optional[ClaimStatusParam] = None,
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
        client.dashboard.profiles.list_cd_profiles()


Operation: PUT /dataservice/dashboard/profiles
----------------------------------------------


Update BiFrost Dashboard Info (by BiFrost)

.. code:: python

    def update_bi_frost_info(
        payload: Optional[SigningKey] = None,
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
        client.dashboard.profiles.update_bi_frost_info()


.. toctree::
    :maxdepth: 1

    models

