==============================================
device.file_based.data_collection.all_statuses
==============================================


Operation: GET /dataservice/device/file-based/data-collection/all-statuses/{deviceUUID}
---------------------------------------------------------------------------------------


Get Data Collection status for given Device UUID

.. code:: python

    def get_data_collection_status_for_device(
        device_uuid: str,
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
        client.device.file_based.data_collection.all_statuses.get_data_collection_status_for_device()


