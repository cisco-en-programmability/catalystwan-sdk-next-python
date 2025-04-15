===================
template.cortex.map
===================


Operation: GET /dataservice/template/cortex/map
-----------------------------------------------


Get Mapped WAN Resource Groups

.. code:: python

    def get(accountid: str, cloudregion: str) -> Any: ...


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
        client.template.cortex.map.get()


