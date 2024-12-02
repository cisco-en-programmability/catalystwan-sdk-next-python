========================================================
device.file_based.data_collection.file_generation_status
========================================================


Operation: POST /dataservice/device/file-based/data-collection/file-generation-status
-------------------------------------------------------------------------------------


Device notify when file is ready and vManage has to download them

.. code:: python

    def handle_file_generation_status_response_from_device(
        payload: Optional[
            HandleFileGenerationStatusNotificationRequest
        ] = None,
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
        client.device.file_based.data_collection.file_generation_status.handle_file_generation_status_response_from_device()


.. toctree::
    :maxdepth: 1

    models

