==============
fedramp.status
==============


Operation: POST /dataservice/fedramp/status
-------------------------------------------


Set network deployment mode

.. code:: python

    def config_fedramp_mode(payload: Optional[Any] = None) -> None: ...


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
        client.fedramp.status.config_fedramp_mode()


