===============
alarms.severity
===============


Operation: GET /dataservice/alarms/severity
-------------------------------------------


Get alarms by severity

.. code:: python

    def get_by_severity(
        severity_level: List[str],
        device_id: Optional[List[str]] = None,
        query: Optional[str] = None,
        site_id: Optional[str] = None,
    ) -> AlarmResponse: ...


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
        client.alarms.severity.get_by_severity()


.. toctree::
    :maxdepth: 1

    summary
    models

