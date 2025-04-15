========================
device.action.deactivate
========================


Operation: GET /dataservice/device/action/deactivate
----------------------------------------------------


Get deactivate partition information

.. code:: python

    def get(device_id: List[DeviceIp]) -> GenerateDeactivateInfo: ...


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
        client.device.action.deactivate.get()


Operation: POST /dataservice/device/action/deactivate
-----------------------------------------------------


Process deactivate operation for smu image

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
        client.device.action.deactivate.post()


.. toctree::
    :maxdepth: 1

    models

