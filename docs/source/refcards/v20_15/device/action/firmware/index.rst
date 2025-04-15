======================
device.action.firmware
======================


Operation: POST /dataservice/device/action/firmware
---------------------------------------------------


Deprecated!!!

Upload firmware image package

.. code:: python

    def post() -> None: ...


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
        client.device.action.firmware.post()


Operation: DELETE /dataservice/device/action/firmware/{versionId}
-----------------------------------------------------------------


Deprecated!!!

Delete firmware image package

.. code:: python

    def delete(version_id: str) -> None: ...


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
        client.device.action.firmware.delete()


Operation: GET /dataservice/device/action/firmware
--------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get() -> None: ...


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
        client.device.action.firmware.get()


Operation: GET /dataservice/device/action/firmware/{versionId}
--------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(version_id: str) -> None: ...


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
        client.device.action.firmware.get()


.. toctree::
    :maxdepth: 1

    activate
    devices
    install
    remove

