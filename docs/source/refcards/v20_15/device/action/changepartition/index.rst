=============================
device.action.changepartition
=============================


Operation: GET /dataservice/device/action/changepartition
---------------------------------------------------------


Get change partition information

.. code:: python

    def generate_change_partition_info(
        device_id: List[DeviceIp],
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
        client.device.action.changepartition.generate_change_partition_info()


Operation: POST /dataservice/device/action/changepartition
----------------------------------------------------------


Process change partition operation

.. code:: python

    def process_change_partition(
        payload: Optional[Any] = None,
    ) -> Any: ...


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
        client.device.action.changepartition.process_change_partition()


.. toctree::
    :maxdepth: 1

    models

