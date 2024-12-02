==========================
statistics.on_demand.queue
==========================


Operation: GET /dataservice/statistics/on-demand/queue
------------------------------------------------------


gets current on-demand queue entries

.. code:: python

    def get_queue_entries() -> Any: ...


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
        client.statistics.on_demand.queue.get_queue_entries()


Operation: POST /dataservice/statistics/on-demand/queue
-------------------------------------------------------


Create on-demand troubleshooting queue entry

.. code:: python

    def create_queue_entry(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.on_demand.queue.create_queue_entry()


Operation: PUT /dataservice/statistics/on-demand/queue/{entryId}
----------------------------------------------------------------


Updates on-demand troubleshooting queue entry

.. code:: python

    def update_queue_entry(
        entry_id: str, payload: Optional[Any] = None
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
        client.statistics.on_demand.queue.update_queue_entry()


Operation: DELETE /dataservice/statistics/on-demand/queue/{entryId}
-------------------------------------------------------------------


removes on-demand queue entry

.. code:: python

    def delete_queue_entry(entry_id: str) -> None: ...


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
        client.statistics.on_demand.queue.delete_queue_entry()


.. toctree::
    :maxdepth: 1

    properties

