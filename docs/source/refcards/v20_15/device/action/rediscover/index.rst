========================
device.action.rediscover
========================


Operation: GET /dataservice/device/action/rediscover
----------------------------------------------------


Get rediscover operation information

.. code:: python

    def get() -> GenerateRediscoverInfo: ...


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
        client.device.action.rediscover.get()


Operation: POST /dataservice/device/action/rediscover
-----------------------------------------------------


Rediscover device

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.device.action.rediscover.post()


.. toctree::
    :maxdepth: 1

    models

