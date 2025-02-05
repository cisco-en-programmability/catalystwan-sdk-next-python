========
auditlog
========


Operation: GET /dataservice/auditlog
------------------------------------


Get stat raw data

.. code:: python

    def get_stat_data_raw_audit_log_data(
        query: str,
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
        client.auditlog.get_stat_data_raw_audit_log_data()


Operation: POST /dataservice/auditlog
-------------------------------------


Get raw property data with post action

.. code:: python

    def get_raw_property_data(
        payload: Optional[Any] = None,
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
        client.auditlog.get_raw_property_data()


.. toctree::
    :maxdepth: 1

    aggregation/index
    doccount/index
    fields/index
    page/index
    query/index
    severity/index
    models

