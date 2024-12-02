======================================
statistics.settings.disable.devicelist
======================================


Operation: GET /dataservice/statistics/settings/disable/devicelist/{indexName}
------------------------------------------------------------------------------


Get list of disabled devices for a statistics index

.. code:: python

    def get_disabled_device_list(index_name: str) -> Any: ...


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
        client.statistics.settings.disable.devicelist.get_disabled_device_list()


Operation: PUT /dataservice/statistics/settings/disable/devicelist/{indexName}
------------------------------------------------------------------------------


Update list of disabled devices for a statistics index

.. code:: python

    def update_statistics_device_list(
        index_name: str, payload: Optional[Any] = None
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
        client.statistics.settings.disable.devicelist.update_statistics_device_list()


