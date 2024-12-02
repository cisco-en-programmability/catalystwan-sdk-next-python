================
app_registry.app
================


Operation: GET /dataservice/app-registry/app
--------------------------------------------


Get All the App for the given conditions

.. code:: python

    def get_all_app_list(
        filter_attribute_type: Optional[str] = None,
        filter_attribute_value: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.app_registry.app.get_all_app_list()


.. toctree::
    :maxdepth: 1

    category
    discoveredapps
    filtermap
    kubernetesapps/index

