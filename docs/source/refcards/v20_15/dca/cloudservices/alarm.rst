=======================
dca.cloudservices.alarm
=======================


Operation: POST /dataservice/dca/cloudservices/alarm
----------------------------------------------------


Generate DCA alarms

.. code:: python

    def generate_alarm(payload: Optional[Any] = None) -> None: ...


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
        client.dca.cloudservices.alarm.generate_alarm()


