============
alarms.topic
============


Operation: GET /dataservice/alarms/topic
----------------------------------------


Get topic on which alarms for given device are publishing.

.. code:: python

    def get_device_topic(ip: str) -> AlarmTopic: ...


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
        client.alarms.topic.get_device_topic()


.. toctree::
    :maxdepth: 1

    models

