==================
mdp.detach_devices
==================


Operation: POST /dataservice/mdp/detachDevices/{nmsId}
------------------------------------------------------


Disconnect devices from mpd controller

.. code:: python

    def post(nms_id: str, payload: Any) -> Any: ...


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
        client.mdp.detach_devices.post()


