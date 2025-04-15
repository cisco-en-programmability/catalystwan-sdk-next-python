======
alarms
======


Operation: GET /dataservice/alarms
----------------------------------


Get alarms for given query. If query is empty then last 30 mins data will be returned.

.. code:: python

    def get(
        query: Optional[str] = None, site_id: Optional[str] = None
    ) -> AlarmResponse: ...


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
        client.alarms.get()


Operation: POST /dataservice/alarms
-----------------------------------


Get alarms for given query.

.. code:: python

    def post(
        payload: Any,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        site_id: Optional[str] = None,
    ) -> AlarmResponse: ...


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
        client.alarms.post()


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

