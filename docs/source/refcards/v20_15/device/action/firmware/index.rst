======================
device.action.firmware
======================


Operation: GET /dataservice/device/action/firmware
--------------------------------------------------


Deprecated!!!

Get list of firmware images in the repository

.. code:: python

    def get_firmware_images() -> None: ...


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
        client.device.action.firmware.get_firmware_images()


Operation: POST /dataservice/device/action/firmware
---------------------------------------------------


Deprecated!!!

Upload firmware image package

.. code:: python

    def process_firmware_image() -> None: ...


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
        client.device.action.firmware.process_firmware_image()


Operation: GET /dataservice/device/action/firmware/{versionId}
--------------------------------------------------------------


Deprecated!!!

Get firmware image details for a given version

.. code:: python

    def get_firmware_image_details(version_id: str) -> None: ...


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
        client.device.action.firmware.get_firmware_image_details()


Operation: DELETE /dataservice/device/action/firmware/{versionId}
-----------------------------------------------------------------


Deprecated!!!

Delete firmware image package

.. code:: python

    def delete_firmware_image(version_id: str) -> None: ...


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
        client.device.action.firmware.delete_firmware_image()


.. toctree::
    :maxdepth: 1

    activate
    devices
    install
    remove

