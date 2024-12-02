====================
system.device.unlock
====================


Operation: POST /dataservice/system/device/{uuid}/unlock
--------------------------------------------------------


Unlock device

.. code:: python

    def unlock_device(
        uuid: str, payload: Optional[Any] = None
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
        client.system.device.unlock.unlock_device()


