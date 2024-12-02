==========================
statistics.settings.status
==========================


Operation: GET /dataservice/statistics/settings/status
------------------------------------------------------


Get statistics settings

.. code:: python

    def get_statistics_settings() -> Any: ...


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
        client.statistics.settings.status.get_statistics_settings()


Operation: PUT /dataservice/statistics/settings/status
------------------------------------------------------


Update statistics settings

.. code:: python

    def update_statistics_settings(
        payload: Optional[Any] = None,
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
        client.statistics.settings.status.update_statistics_settings()


.. toctree::
    :maxdepth: 1

    device

