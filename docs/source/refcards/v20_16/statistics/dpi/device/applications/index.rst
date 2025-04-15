==================================
statistics.dpi.device.applications
==================================


Operation: GET /dataservice/statistics/dpi/device/applications
--------------------------------------------------------------


Get DPI application flows device aggregation data

.. code:: python

    def get(
        query: str, limit: Optional[int] = None
    ) -> DeviceAppResponse: ...


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
        client.statistics.dpi.device.applications.get()


.. toctree::
    :maxdepth: 1

    models

