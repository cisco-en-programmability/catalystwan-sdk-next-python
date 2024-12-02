========================
device.action.rediscover
========================


Operation: GET /dataservice/device/action/rediscover
----------------------------------------------------


Get rediscover operation information

.. code:: python

    def generate_rediscover_info() -> GenerateRediscoverInfo: ...


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
        client.device.action.rediscover.generate_rediscover_info()


Operation: POST /dataservice/device/action/rediscover
-----------------------------------------------------


Rediscover device

.. code:: python

    def re_discover_devices(payload: Optional[Any] = None) -> None: ...


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
        client.device.action.rediscover.re_discover_devices()


.. toctree::
    :maxdepth: 1

    models

