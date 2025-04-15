==================
device.unreachable
==================


Operation: GET /dataservice/device/unreachable
----------------------------------------------


Get list of unreachable devices

.. code:: python

    def get(personality: str) -> List[Any]: ...


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
        client.device.unreachable.get()


Operation: DELETE /dataservice/device/unreachable/{deviceIP}
------------------------------------------------------------


Delete unreachable device

.. code:: python

    def delete(device_ip: str) -> None: ...


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
        client.device.unreachable.delete()


