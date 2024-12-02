===============================
data.device.statistics.doccount
===============================


Operation: GET /dataservice/data/device/statistics/{state_data_type}/doccount
-----------------------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_with_state_data_type(
        state_data_type: str,
        start_date: str,
        end_date: str,
        time_zone: Optional[str] = None,
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
        client.data.device.statistics.doccount.get_count_with_state_data_type()


