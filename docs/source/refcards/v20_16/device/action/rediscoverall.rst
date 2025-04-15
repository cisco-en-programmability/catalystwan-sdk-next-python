===========================
device.action.rediscoverall
===========================


Operation: POST /dataservice/device/action/rediscoverall
--------------------------------------------------------


Rediscover all devices

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
        client.device.action.rediscoverall.post()


