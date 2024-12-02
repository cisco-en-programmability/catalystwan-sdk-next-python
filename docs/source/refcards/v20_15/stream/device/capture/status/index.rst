============================
stream.device.capture.status
============================


Operation: GET /dataservice/stream/device/capture/status/{sessionId}
--------------------------------------------------------------------


Get packet capture session status

.. code:: python

    def get_file_download_status(
        session_id: str,
    ) -> GetFileDownloadStatusRes: ...


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
        client.stream.device.capture.status.get_file_download_status()


.. toctree::
    :maxdepth: 1

    models

