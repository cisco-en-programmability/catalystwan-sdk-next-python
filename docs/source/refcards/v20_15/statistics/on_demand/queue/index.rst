==========================
statistics.on_demand.queue
==========================


Operation: GET /dataservice/statistics/on-demand/queue
------------------------------------------------------


gets current on-demand queue entries

.. code:: python

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
        client.statistics.on_demand.queue.get()


Operation: POST /dataservice/statistics/on-demand/queue
-------------------------------------------------------


Create on-demand troubleshooting queue entry

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.statistics.on_demand.queue.post()


Operation: PUT /dataservice/statistics/on-demand/queue/{entryId}
----------------------------------------------------------------


Updates on-demand troubleshooting queue entry

.. code:: python

    def put(entry_id: str, payload: Any) -> Any: ...


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
        client.statistics.on_demand.queue.put()


Operation: DELETE /dataservice/statistics/on-demand/queue/{entryId}
-------------------------------------------------------------------


removes on-demand queue entry

.. code:: python

    def delete(entry_id: str) -> None: ...


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
        client.statistics.on_demand.queue.delete()


.. toctree::
    :maxdepth: 1

    properties

