=================
device.omp.status
=================


Operation: GET /dataservice/device/omp/status
---------------------------------------------


Get device OMP status

.. code:: python

    def get_device_omp_status() -> Any: ...


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
        client.device.omp.status.get_device_omp_status()


