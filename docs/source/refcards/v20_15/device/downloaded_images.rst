========================
device.downloaded_images
========================


Operation: GET /dataservice/device/downloadedImages
---------------------------------------------------


Get images list from device

.. code:: python

    def create_software_list(device_id: str) -> List[Any]: ...


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
        client.device.downloaded_images.create_software_list()


