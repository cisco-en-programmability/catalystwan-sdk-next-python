================
webex.datacenter
================


Operation: POST /dataservice/webex/datacenter
---------------------------------------------


TEMP-Insert webex data center details manually for test setup

.. code:: python

    def post(payload: WebexDataCenter) -> bool: ...


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
        client.webex.datacenter.post()


Operation: DELETE /dataservice/webex/datacenter
-----------------------------------------------


Delete webex data center data in DB

.. code:: python

    def delete() -> bool: ...


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
        client.webex.datacenter.delete()


.. toctree::
    :maxdepth: 1

    sync
    syncstatus/index
    models

