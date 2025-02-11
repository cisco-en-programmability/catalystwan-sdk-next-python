================================
networkdesign.global_.parameters
================================


Operation: GET /dataservice/networkdesign/global/parameters
-----------------------------------------------------------


Deprecated!!!

Get global parameter templates

.. code:: python

    def get_global_parameters() -> Any: ...


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
        client.networkdesign.global_.parameters.get_global_parameters()


