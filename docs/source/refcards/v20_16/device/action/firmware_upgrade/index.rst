==============================
device.action.firmware_upgrade
==============================


Operation: POST /dataservice/device/action/firmware-upgrade
-----------------------------------------------------------


Eemote firmware on device

.. code:: python

    def remote_firmware_image_upgrade(
        payload: Optional[Any] = None,
    ) -> FirmwareImageRemoteUpgrade: ...


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
        client.device.action.firmware_upgrade.remote_firmware_image_upgrade()


Operation: DELETE /dataservice/device/action/firmware-upgrade/{versionId}
-------------------------------------------------------------------------


Download software package file

.. code:: python

    def delete_firmware_upgarde_remote_image(version_id: str) -> None: ...


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
        client.device.action.firmware_upgrade.delete_firmware_upgarde_remote_image()


.. toctree::
    :maxdepth: 1

    devices/index
    remote/index
    models

