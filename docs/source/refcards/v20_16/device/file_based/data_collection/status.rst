========================================
device.file_based.data_collection.status
========================================


Operation: GET /dataservice/device/file-based/data-collection/status/{requestUUID}
----------------------------------------------------------------------------------


Get Data Collection status for given Request UUID

.. code:: python

    def get(request_uuid: str) -> str: ...


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
        client.device.file_based.data_collection.status.get()


