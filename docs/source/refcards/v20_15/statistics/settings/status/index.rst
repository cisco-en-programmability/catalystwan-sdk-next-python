==========================
statistics.settings.status
==========================


Operation: GET /dataservice/statistics/settings/status
------------------------------------------------------


Get statistics settings

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
        client.statistics.settings.status.get()


Operation: PUT /dataservice/statistics/settings/status
------------------------------------------------------


Update statistics settings

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.statistics.settings.status.put()


.. toctree::
    :maxdepth: 1

    device

