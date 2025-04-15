==========================================
statistics.dpi.device.details.applications
==========================================


Operation: GET /dataservice/statistics/dpi/device/details/applications
----------------------------------------------------------------------


Get detailed DPI device and application list

.. code:: python

    def get(query: str) -> DeviceAppDetailResponse: ...


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
        client.statistics.dpi.device.details.applications.get()


.. toctree::
    :maxdepth: 1

    models

