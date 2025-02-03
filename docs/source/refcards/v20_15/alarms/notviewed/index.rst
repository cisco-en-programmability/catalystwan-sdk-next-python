================
alarms.notviewed
================


Operation: GET /dataservice/alarms/notviewed
--------------------------------------------


Get alarms which are not acknowledged by the user.

.. code:: python

    def get_non_viewed_alarms(
        state: Optional[str] = None,
    ) -> List[Alarm]: ...


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
        client.alarms.notviewed.get_non_viewed_alarms()


.. toctree::
    :maxdepth: 1

    models

