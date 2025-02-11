=============
auditlog.page
=============


Operation: GET /dataservice/auditlog/page
-----------------------------------------


Get raw property data in bulk

.. code:: python

    def get_stat_bulk_raw_property_data(
        query: str, count: int, scroll_id: Optional[str] = None
    ) -> GetAuditLogData: ...


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
        client.auditlog.page.get_stat_bulk_raw_property_data()


Operation: POST /dataservice/auditlog/page
------------------------------------------


Get raw property data in bulk with post action

.. code:: python

    def get_post_stat_bulk_raw_property_data(
        count: int,
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
    ) -> GetAuditLogData: ...


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
        client.auditlog.page.get_post_stat_bulk_raw_property_data()


.. toctree::
    :maxdepth: 1

    models

