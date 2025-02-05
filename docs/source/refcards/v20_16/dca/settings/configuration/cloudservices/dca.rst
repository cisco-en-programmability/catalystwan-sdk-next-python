============================================
dca.settings.configuration.cloudservices.dca
============================================


Operation: GET /dataservice/dca/settings/configuration/cloudservices/dca
------------------------------------------------------------------------


Get DCA cloud service configuration

.. code:: python

    def get_cloud_services_configuration_dca() -> Any: ...


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
        client.dca.settings.configuration.cloudservices.dca.get_cloud_services_configuration_dca()


