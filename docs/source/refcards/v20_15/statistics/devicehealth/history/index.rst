===============================
statistics.devicehealth.history
===============================


Operation: GET /dataservice/statistics/devicehealth/history
-----------------------------------------------------------


Get all device health history

.. code:: python

    def get(
        last_n_hours: Optional[int] = 12,
        site: Optional[str] = None,
        limit: Optional[int] = 30,
    ) -> List[DeviceHealthHistoryItem]: ...


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
        client.statistics.devicehealth.history.get()


.. toctree::
    :maxdepth: 1

    models

