=======================
v1.smart_licensing.sync
=======================


Operation: POST /dataservice/v1/smart-licensing/sync
----------------------------------------------------


Sync licenses from CSSM to vManage db

.. code:: python

    def post(payload: SyncRequest) -> None: ...


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
        client.v1.smart_licensing.sync.post()


.. toctree::
    :maxdepth: 1

    models

