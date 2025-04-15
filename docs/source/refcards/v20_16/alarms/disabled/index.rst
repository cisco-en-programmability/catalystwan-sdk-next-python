===============
alarms.disabled
===============


Operation: GET /dataservice/alarms/disabled
-------------------------------------------


List all disabled alarms

.. code:: python

    def get() -> List[DisabledAlarmDetails]: ...


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
        client.alarms.disabled.get()


Operation: POST /dataservice/alarms/disabled
--------------------------------------------


Enable/Disable alarms by event name

.. code:: python

    def post(
        event_name: str,
        disable: Optional[bool] = None,
        time: Optional[int] = None,
    ) -> None: ...


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
        client.alarms.disabled.post()


.. toctree::
    :maxdepth: 1

    models

