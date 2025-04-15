===========================
device.app_route.statistics
===========================


Operation: GET /dataservice/device/app-route/statistics
-------------------------------------------------------


Get application-aware routing statistics from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        remote_system_ip: Optional[str] = None,
        local_color: Optional[LocalColorParam] = None,
        remote_color: Optional[RemoteColorParam] = None,
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
        client.device.app_route.statistics.get()


.. toctree::
    :maxdepth: 1

    models

