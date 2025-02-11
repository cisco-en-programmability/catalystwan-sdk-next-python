================
webex.datacenter
================


Operation: POST /dataservice/webex/datacenter
---------------------------------------------


TEMP-Insert webex data center details manually for test setup

.. code:: python

    def get_webex_data_centers(
        payload: Optional[WebexDataCenter] = None,
    ) -> bool: ...


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
        client.webex.datacenter.get_webex_data_centers()


Operation: DELETE /dataservice/webex/datacenter
-----------------------------------------------


Delete webex data center data in DB

.. code:: python

    def delete_webex_data_centers() -> bool: ...


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
        client.webex.datacenter.delete_webex_data_centers()


.. toctree::
    :maxdepth: 1

    sync
    syncstatus/index
    models

