==========================================
device.file_based.data_collection.download
==========================================


Operation: GET /dataservice/device/file-based/data-collection/download/{requestUUID}
------------------------------------------------------------------------------------


Download generated file

.. code:: python

    def get(request_uuid: str) -> None: ...


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
        client.device.file_based.data_collection.download.get()


