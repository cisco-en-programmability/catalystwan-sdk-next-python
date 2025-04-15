============
alarms.topic
============


Operation: GET /dataservice/alarms/topic
----------------------------------------


Get topic on which alarms for given device are publishing.

.. code:: python

    def get(ip: str) -> AlarmTopic: ...


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
        client.alarms.topic.get()


.. toctree::
    :maxdepth: 1

    models

