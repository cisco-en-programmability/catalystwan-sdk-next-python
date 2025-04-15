==============================
stream.device.capture.download
==============================


Operation: GET /dataservice/stream/device/capture/download/{sessionId}
----------------------------------------------------------------------


Download packet capture file

.. code:: python

    def get(session_id: str) -> str: ...


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
        client.stream.device.capture.download.get()


