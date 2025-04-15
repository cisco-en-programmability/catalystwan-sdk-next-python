===========================================
statistics.dpi.device.application.flowcount
===========================================


Operation: GET /dataservice/statistics/dpi/device/application/flowcount
-----------------------------------------------------------------------


Get application flow count per tunnel

.. code:: python

    def get(
        device_id: str,
        interval: str,
        window: int,
        application: Optional[str] = None,
        family: Optional[str] = None,
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
        client.statistics.dpi.device.application.flowcount.get()


