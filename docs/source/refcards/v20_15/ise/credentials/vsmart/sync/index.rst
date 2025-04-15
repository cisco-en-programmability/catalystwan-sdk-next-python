===========================
ise.credentials.vsmart.sync
===========================


Operation: POST /dataservice/ise/credentials/vsmart/sync
--------------------------------------------------------


Send pxGrid and ISE server configuration to vSmarts

.. code:: python

    def post() -> VsmartSyncResponse: ...


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
        client.ise.credentials.vsmart.sync.post()


.. toctree::
    :maxdepth: 1

    models

