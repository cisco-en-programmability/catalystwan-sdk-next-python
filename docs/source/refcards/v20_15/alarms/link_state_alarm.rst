=======================
alarms.link_state_alarm
=======================


Operation: GET /dataservice/alarms/link-state-alarm
---------------------------------------------------


Get configuration for link-state alarm

.. code:: python

    def get_link_state_alarm_config() -> str: ...


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
        client.alarms.link_state_alarm.get_link_state_alarm_config()


Operation: POST /dataservice/alarms/link-state-alarm
----------------------------------------------------


Enable/Disable a specific link-state alarm

.. code:: python

    def enable_disable_link_state_alarm(
        link_name: str, enable: bool
    ) -> None: ...


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
        client.alarms.link_state_alarm.enable_disable_link_state_alarm()


