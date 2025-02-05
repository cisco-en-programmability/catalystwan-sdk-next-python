====================
auditlog.aggregation
====================


Operation: GET /dataservice/auditlog/aggregation
------------------------------------------------


Get raw property data aggregated

.. code:: python

    def get_property_aggregation_data(
        query: str,
    ) -> GetAuditLogAggregation: ...


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
        client.auditlog.aggregation.get_property_aggregation_data()


Operation: POST /dataservice/auditlog/aggregation
-------------------------------------------------


Get raw property data aggregated with post action

.. code:: python

    def get_post_property_aggregation_data(
        payload: Optional[Any] = None,
    ) -> GetAuditLogAggregation: ...


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
        client.auditlog.aggregation.get_post_property_aggregation_data()


.. toctree::
    :maxdepth: 1

    models

