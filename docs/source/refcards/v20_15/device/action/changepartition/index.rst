=============================
device.action.changepartition
=============================


Operation: GET /dataservice/device/action/changepartition
---------------------------------------------------------


Get change partition information

.. code:: python

    def get(device_id: List[DeviceIp]) -> None: ...


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
        client.device.action.changepartition.get()


Operation: POST /dataservice/device/action/changepartition
----------------------------------------------------------


Process change partition operation

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
        client.device.action.changepartition.post()


.. toctree::
    :maxdepth: 1

    models

