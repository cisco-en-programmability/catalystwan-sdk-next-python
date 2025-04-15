=========================
template.config.rmaupdate
=========================


Operation: PUT /dataservice/template/config/rmaupdate
-----------------------------------------------------


Update new device

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.template.config.rmaupdate.put()


