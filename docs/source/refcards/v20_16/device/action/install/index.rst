=====================
device.action.install
=====================


Operation: GET /dataservice/device/action/install
-------------------------------------------------


Generate install info

.. code:: python

    def get(device_id: List[DeviceIp]) -> Any: ...


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
        client.device.action.install.get()


Operation: POST /dataservice/device/action/install
--------------------------------------------------


Process an installation operation

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.device.action.install.post()


.. toctree::
    :maxdepth: 1

    devices/index
    models

