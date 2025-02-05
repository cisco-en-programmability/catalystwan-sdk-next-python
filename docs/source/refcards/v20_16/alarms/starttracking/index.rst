====================
alarms.starttracking
====================


Operation: POST /dataservice/alarms/starttracking/{testName}
------------------------------------------------------------


Start tracking events

.. code:: python

    def start_tracking(test_name: str) -> SimpleMessageResponse: ...


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
        client.alarms.starttracking.start_tracking()


.. toctree::
    :maxdepth: 1

    models

