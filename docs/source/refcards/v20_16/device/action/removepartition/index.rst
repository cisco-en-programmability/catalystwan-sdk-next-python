=============================
device.action.removepartition
=============================


Operation: GET /dataservice/device/action/removepartition
---------------------------------------------------------


Get remove partition information

.. code:: python

    def get(
        device_id: Optional[List[DeviceIp]] = None,
    ) -> GenerateRemovePartitionInfo: ...


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
        client.device.action.removepartition.get()


Operation: POST /dataservice/device/action/removepartition
----------------------------------------------------------


Process remove partition operation

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
        client.device.action.removepartition.post()


.. toctree::
    :maxdepth: 1

    models

