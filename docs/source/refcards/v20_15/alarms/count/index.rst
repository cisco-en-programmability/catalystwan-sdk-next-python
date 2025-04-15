============
alarms.count
============


Operation: GET /dataservice/alarms/count
----------------------------------------


Get the count of alarms which are active and not acknowledged by user.

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
        client.alarms.count.get()


Operation: POST /dataservice/alarms/count
-----------------------------------------


Get the count of alarms as per the query passed.

.. code:: python

    def post(
        payload: Any, site_id: Optional[str] = None
    ) -> List[AlarmCountPost]: ...


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
        client.alarms.count.post()


.. toctree::
    :maxdepth: 1

    models

