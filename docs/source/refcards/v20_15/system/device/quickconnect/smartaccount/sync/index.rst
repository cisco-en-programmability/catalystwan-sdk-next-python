============================================
system.device.quickconnect.smartaccount.sync
============================================


Operation: POST /dataservice/system/device/quickconnect/smartaccount/sync
-------------------------------------------------------------------------


Sync devices from Smart-Account

.. code:: python

    def post(payload: SmartAccountModel) -> SyncDevicesResp: ...


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
        client.system.device.quickconnect.smartaccount.sync.post()


.. toctree::
    :maxdepth: 1

    models

