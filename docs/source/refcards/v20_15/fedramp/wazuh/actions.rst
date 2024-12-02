=====================
fedramp.wazuh.actions
=====================


Operation: GET /dataservice/fedramp/wazuh/actions
-------------------------------------------------


Wazuh agent action

.. code:: python

    def request_wazuh_actions(
        action: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.fedramp.wazuh.actions.request_wazuh_actions()


