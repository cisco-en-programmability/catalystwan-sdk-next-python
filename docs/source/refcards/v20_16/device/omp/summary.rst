==================
device.omp.summary
==================


Operation: GET /dataservice/device/omp/summary
----------------------------------------------


Get OMP summary

.. code:: python

    def create_omp_summary(device_id: str) -> Any: ...


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
        client.device.omp.summary.create_omp_summary()


