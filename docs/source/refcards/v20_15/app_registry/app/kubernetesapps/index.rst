===============================
app_registry.app.kubernetesapps
===============================


Operation: GET /dataservice/app-registry/app/kubernetesapps
-----------------------------------------------------------


Obtain all services associated with clusters

.. code:: python

    def get_kubernetes_services(
        is_cached: Optional[bool] = False,
        offset: Optional[int] = 0,
        limit: Optional[int] = 0,
    ) -> List[DiscoveredServices]: ...


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
        client.app_registry.app.kubernetesapps.get_kubernetes_services()


.. toctree::
    :maxdepth: 1

    models

