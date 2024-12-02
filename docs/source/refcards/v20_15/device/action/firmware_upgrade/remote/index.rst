=====================================
device.action.firmware_upgrade.remote
=====================================


Operation: GET /dataservice/device/action/firmware-upgrade/remote
-----------------------------------------------------------------


firmware remote image package

.. code:: python

    def get_firmware_remote_image() -> (
        ProcessGetFirmwareRemoteImageReq
    ): ...


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
        client.device.action.firmware_upgrade.remote.get_firmware_remote_image()


Operation: POST /dataservice/device/action/firmware-upgrade/remote
------------------------------------------------------------------


firmware remote image package

.. code:: python

    def process_firmware_remote_image(
        payload: Optional[Any] = None,
    ) -> ProcessFirmwareRemoteImageReq: ...


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
        client.device.action.firmware_upgrade.remote.process_firmware_remote_image()


Operation: PUT /dataservice/device/action/firmware-upgrade/remote/{versionId}
-----------------------------------------------------------------------------


Download software package file

.. code:: python

    def edit_firmware_upgarde_remote_image(
        version_id: str, payload: Optional[Any] = None
    ) -> ProcessGetFirmwareRemoteImageReq: ...


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
        client.device.action.firmware_upgrade.remote.edit_firmware_upgarde_remote_image()


.. toctree::
    :maxdepth: 1

    models

