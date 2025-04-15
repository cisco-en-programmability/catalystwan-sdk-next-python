================
device.omp.links
================


Operation: GET /dataservice/device/omp/links
--------------------------------------------


Get OMP connection list

.. code:: python

    def get(state: str) -> Any: ...


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
        client.device.omp.links.get()


