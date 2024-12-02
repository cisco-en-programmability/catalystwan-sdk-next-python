==================
device.unreachable
==================


Operation: GET /dataservice/device/unreachable
----------------------------------------------


Get list of unreachable devices

.. code:: python

    def list_unreachable_devices(personality: str) -> List[Any]: ...


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
        client.device.unreachable.list_unreachable_devices()


Operation: DELETE /dataservice/device/unreachable/{deviceIP}
------------------------------------------------------------


Delete unreachable device

.. code:: python

    def remove_unreachable_device(device_ip: str) -> None: ...


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
        client.device.unreachable.remove_unreachable_device()


