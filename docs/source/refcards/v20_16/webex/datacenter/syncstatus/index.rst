===========================
webex.datacenter.syncstatus
===========================


Operation: GET /dataservice/webex/datacenter/syncstatus
-------------------------------------------------------


Get webex data center sync status from DB

.. code:: python

    def get() -> SyncStatusResponse: ...


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
        client.webex.datacenter.syncstatus.get()


Operation: PUT /dataservice/webex/datacenter/syncstatus
-------------------------------------------------------


Set webex data center sync needed            to false

.. code:: python

    def put() -> bool: ...


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
        client.webex.datacenter.syncstatus.put()


.. toctree::
    :maxdepth: 1

    models

