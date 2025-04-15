==================
template.cor.cloud
==================


Operation: GET /dataservice/template/cor/cloud
----------------------------------------------


Deprecated!!!

Get cloud list

.. code:: python

    def get() -> List[Any]: ...


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
        client.template.cor.cloud.get()


.. toctree::
    :maxdepth: 1

    account
    authenticate
    host/index
    mappedhostaccounts

