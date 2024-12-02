====================
fedramp.wazuh.status
====================


Operation: GET /dataservice/fedramp/wazuh/status
------------------------------------------------


Get Wazuh agent status

.. code:: python

    def get_wazuh_agent_status() -> List[Any]: ...


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
        client.fedramp.wazuh.status.get_wazuh_agent_status()


