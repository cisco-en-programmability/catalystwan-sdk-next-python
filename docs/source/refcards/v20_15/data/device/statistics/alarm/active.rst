===================================
data.device.statistics.alarm.active
===================================


Operation: GET /dataservice/data/device/statistics/alarm/active
---------------------------------------------------------------


Get active alarms

.. code:: python

    def get(
        scroll_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        count: Optional[int] = None,
        time_zone: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.data.device.statistics.alarm.active.get()


