======================================
statistics.download.fetchv_manage_list
======================================


Operation: GET /dataservice/statistics/download/{processType}/fetchvManageList
------------------------------------------------------------------------------


.. code:: python

    def fetch_list(process_type: str) -> None: ...


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
        client.statistics.download.fetchv_manage_list.fetch_list()


