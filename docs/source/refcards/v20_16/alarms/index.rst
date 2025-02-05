======
alarms
======


Operation: GET /dataservice/alarms
----------------------------------


Get alarms for given query. If query is empty then last 30 mins data will be returned.

.. code:: python

    def get_raw_alarm_data(
        query: Optional[str] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
    ) -> List[Alarm]: ...


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
        client.alarms.get_raw_alarm_data()


Operation: POST /dataservice/alarms
-----------------------------------


Get alarms for given query.

.. code:: python

    def post_raw_alarm_data(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
    ) -> List[Alarm]: ...


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
        client.alarms.post_raw_alarm_data()


.. toctree::
    :maxdepth: 1

    aggregation/index
    clear
    count/index
    disabled/index
    doccount
    dump/index
    fields
    link_state_alarm
    markallasviewed
    markviewed/index
    master
    notviewed/index
    page/index
    purgefrequency/index
    query/index
    reset/index
    restart/index
    rulenamedisplay/index
    severity/index
    severitymappings/index
    starttracking/index
    stats/index
    stoptracking/index
    topic/index
    topn
    uuid/index
    models

