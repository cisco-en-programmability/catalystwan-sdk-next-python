================================
stream.device.nwpi.domain_metric
================================


Operation: GET /dataservice/stream/device/nwpi/domainMetric
-----------------------------------------------------------


Deprecated!!!

.. code:: python

    def get_domain_metric(
        trace_id: int,
        timestamp: int,
        domain: str,
        first_timestamp: int,
        last_timestamp: int,
        trace_model: Optional[str] = None,
    ) -> List[DomainMetricResponsePayloadInner]: ...


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
        client.stream.device.nwpi.domain_metric.get_domain_metric()


.. toctree::
    :maxdepth: 1

    models

