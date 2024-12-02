==========================
device.action.image_remove
==========================


Operation: POST /dataservice/device/action/image-remove
-------------------------------------------------------


Process remove software image operation

.. code:: python

    def process_remove_software_image(
        payload: Optional[Any] = None,
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
        client.device.action.image_remove.process_remove_software_image()


