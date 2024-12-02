====================================================
device.file_based.data_collection.supported_commands
====================================================


Operation: GET /dataservice/device/file-based/data-collection/supported-commands/{deviceUUID}
---------------------------------------------------------------------------------------------


Get Supported Command list for given Device UUID

.. code:: python

    def get_supported_commands_list(device_uuid: str) -> str: ...


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
        client.device.file_based.data_collection.supported_commands.get_supported_commands_list()


