===============================
system.device.smartaccount.sync
===============================


Operation: POST /dataservice/system/device/smartaccount/sync
------------------------------------------------------------


Sync devices from Smart-Account

.. code:: python

    def post(payload: Any) -> SyncDevicesResp: ...


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
        client.system.device.smartaccount.sync.post()


.. toctree::
    :maxdepth: 1

    models

