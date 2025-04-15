==============================
dca.settings.configuration.dca
==============================


Operation: POST /dataservice/dca/settings/configuration/{type}/dca
------------------------------------------------------------------


Create analytics config data

.. code:: python

    def post(type_: TypeParam, payload: Any) -> Any: ...


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
        client.dca.settings.configuration.dca.post()


.. toctree::
    :maxdepth: 1

    models

