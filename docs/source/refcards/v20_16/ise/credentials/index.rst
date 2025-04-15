===============
ise.credentials
===============


Operation: GET /dataservice/ise/credentials
-------------------------------------------


Get Ise server credentials

.. code:: python

    def get() -> IseServer: ...


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
        client.ise.credentials.get()


Operation: PUT /dataservice/ise/credentials
-------------------------------------------


update Ise server credentials

.. code:: python

    def put(payload: IseServer) -> bool: ...


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
        client.ise.credentials.put()


Operation: POST /dataservice/ise/credentials
--------------------------------------------


Add Ise server credentials

.. code:: python

    def post(payload: IseServer) -> bool: ...


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
        client.ise.credentials.post()


.. toctree::
    :maxdepth: 1

    iseandpxgrid
    pxgrid/index
    vsmart/index
    models

