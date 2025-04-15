=======================
alarms.severitymappings
=======================


Operation: GET /dataservice/alarms/severitymappings
---------------------------------------------------


Gets alarm severity mappings

.. code:: python

    def get() -> List[AlarmSeverityMapping]: ...


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
        client.alarms.severitymappings.get()


.. toctree::
    :maxdepth: 1

    models

