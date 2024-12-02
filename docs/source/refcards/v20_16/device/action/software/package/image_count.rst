==========================================
device.action.software.package.image_count
==========================================


Operation: GET /dataservice/device/action/software/package/imageCount
---------------------------------------------------------------------


Number of software image presented in vManage repository

.. code:: python

    def get_upload_images_count(
        image_type: Optional[List[str]] = None,
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
        client.device.action.software.package.image_count.get_upload_images_count()


