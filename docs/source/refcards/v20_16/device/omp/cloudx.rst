=================
device.omp.cloudx
=================


Operation: GET /dataservice/device/omp/cloudx
---------------------------------------------


Get CloudExpress routes received list

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.omp.cloudx.get()


