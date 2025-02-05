===============
ise.credentials
===============


Operation: GET /dataservice/ise/credentials
-------------------------------------------


Get Ise server credentials

.. code:: python

    def get_ise_server_credentials() -> IseServer: ...


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
        client.ise.credentials.get_ise_server_credentials()


Operation: PUT /dataservice/ise/credentials
-------------------------------------------


update Ise server credentials

.. code:: python

    def update_ise_server_credentials(
        payload: Optional[IseServer] = None,
    ) -> bool: ...


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
        client.ise.credentials.update_ise_server_credentials()


Operation: POST /dataservice/ise/credentials
--------------------------------------------


Add Ise server credentials

.. code:: python

    def add_ise_server_credentials(
        payload: Optional[IseServer] = None,
    ) -> bool: ...


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
        client.ise.credentials.add_ise_server_credentials()


.. toctree::
    :maxdepth: 1

    iseandpxgrid
    pxgrid/index
    vsmart/index
    models

