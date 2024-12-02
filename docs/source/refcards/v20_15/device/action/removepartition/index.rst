=============================
device.action.removepartition
=============================


Operation: GET /dataservice/device/action/removepartition
---------------------------------------------------------


Get remove partition information

.. code:: python

    def generate_remove_partition_info(
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
        client.device.action.removepartition.generate_remove_partition_info()


Operation: POST /dataservice/device/action/removepartition
----------------------------------------------------------


Process remove partition operation

.. code:: python

    def process_remove_partition(
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
        client.device.action.removepartition.process_remove_partition()


.. toctree::
    :maxdepth: 1

    models

