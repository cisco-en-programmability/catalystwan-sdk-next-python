=============================
template.cloudx.availableapps
=============================


Operation: GET /dataservice/template/cloudx/availableapps
---------------------------------------------------------


Get CloudX available apps list

.. code:: python

    def get_cloud_x_available_apps() -> List[Any]: ...


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
        client.template.cloudx.availableapps.get_cloud_x_available_apps()


