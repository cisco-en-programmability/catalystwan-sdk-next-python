============================
device.action.image_download
============================


Operation: POST /dataservice/device/action/image-download
---------------------------------------------------------


Intitate image download on the given device.

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.device.action.image_download.post()


