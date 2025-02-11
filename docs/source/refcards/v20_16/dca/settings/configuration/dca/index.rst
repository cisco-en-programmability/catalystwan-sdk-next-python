==============================
dca.settings.configuration.dca
==============================


Operation: POST /dataservice/dca/settings/configuration/{type}/dca
------------------------------------------------------------------


Create analytics config data

.. code:: python

    def create_dca_analytics_data_file(
        type_: TypeParam, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.dca.settings.configuration.dca.create_dca_analytics_data_file()


.. toctree::
    :maxdepth: 1

    models

