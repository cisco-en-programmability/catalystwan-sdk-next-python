=======================
template.cor.devicepair
=======================


Operation: POST /dataservice/template/cor/devicepair
----------------------------------------------------


Deprecated!!!

Add device pair

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.cor.devicepair.post()


.. toctree::
    :maxdepth: 1

    hostvpc

