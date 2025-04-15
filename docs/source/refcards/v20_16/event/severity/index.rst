==============
event.severity
==============


Operation: GET /dataservice/event/severity
------------------------------------------


Get alarms by severity

.. code:: python

    def get(
        severity_level: List[str],
        device_id: Optional[List[str]] = None,
        query: Optional[str] = None,
        site_id: Optional[str] = None,
    ) -> List[EventsBySeverity]: ...


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
        client.event.severity.get()


.. toctree::
    :maxdepth: 1

    summary
    models

