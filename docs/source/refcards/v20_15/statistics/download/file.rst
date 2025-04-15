========================
statistics.download.file
========================


Operation: GET /dataservice/statistics/download/{processType}/file/{fileType}/{queue}/{deviceIp}/{token}/{fileName}
-------------------------------------------------------------------------------------------------------------------


Downloading stats file

.. code:: python

    def get(
        process_type: str,
        file_type: str,
        queue: str,
        device_ip: str,
        token: str,
        file_name: str,
    ) -> Any: ...


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
        client.statistics.download.file.get()


