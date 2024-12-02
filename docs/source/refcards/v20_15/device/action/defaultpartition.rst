==============================
device.action.defaultpartition
==============================


Operation: POST /dataservice/device/action/defaultpartition
-----------------------------------------------------------


Process marking default partition operation

.. code:: python

    def process_default_partition(
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
        client.device.action.defaultpartition.process_default_partition()


