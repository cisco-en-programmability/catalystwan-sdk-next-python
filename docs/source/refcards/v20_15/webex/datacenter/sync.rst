=====================
webex.datacenter.sync
=====================


Operation: POST /dataservice/webex/datacenter/sync
--------------------------------------------------


TEMP-Update webex data center data in DB with data from Webex API

.. code:: python

    def post() -> bool: ...


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
        client.webex.datacenter.sync.post()


