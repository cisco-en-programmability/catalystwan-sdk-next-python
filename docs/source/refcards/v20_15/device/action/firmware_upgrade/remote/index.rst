=====================================
device.action.firmware_upgrade.remote
=====================================


Operation: GET /dataservice/device/action/firmware-upgrade/remote
-----------------------------------------------------------------


firmware remote image package

.. code:: python

    def get() -> ProcessGetFirmwareRemoteImageReq: ...


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
        client.device.action.firmware_upgrade.remote.get()


Operation: POST /dataservice/device/action/firmware-upgrade/remote
------------------------------------------------------------------


firmware remote image package

.. code:: python

    def post(payload: Any) -> ProcessFirmwareRemoteImageReq: ...


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
        client.device.action.firmware_upgrade.remote.post()


Operation: PUT /dataservice/device/action/firmware-upgrade/remote/{versionId}
-----------------------------------------------------------------------------


Download software package file

.. code:: python

    def put(
        version_id: str, payload: Any
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
        client.device.action.firmware_upgrade.remote.put()


.. toctree::
    :maxdepth: 1

    models

