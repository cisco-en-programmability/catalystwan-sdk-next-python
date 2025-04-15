======================
data.device.statistics
======================


Operation: GET /dataservice/data/device/statistics
--------------------------------------------------


.. code:: python

    @overload
    def get() -> Any: ...


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
        client.data.device.statistics.get()


Operation: GET /dataservice/data/device/statistics/{state_data_type}
--------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        state_data_type: str,
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
        client.data.device.statistics.get()


.. toctree::
    :maxdepth: 1

    alarm/index
    doccount
    fields

