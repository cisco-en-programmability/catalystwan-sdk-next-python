============
admin.radius
============


Operation: GET /dataservice/admin/radius
----------------------------------------


Get radius configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get_radius_config() -> Radius: ...


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
        client.admin.radius.get_radius_config()


Operation: PUT /dataservice/admin/radius
----------------------------------------


Update radius configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def update_radius_config(
        payload: Optional[Radius] = None,
    ) -> None: ...


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
        client.admin.radius.update_radius_config()


Operation: POST /dataservice/admin/radius
-----------------------------------------


Create radius configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def create_radius_config(
        payload: Optional[Radius] = None,
    ) -> None: ...


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
        client.admin.radius.create_radius_config()


Operation: DELETE /dataservice/admin/radius
-------------------------------------------


Delete radius configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def delete_radius_config() -> Radius: ...


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
        client.admin.radius.delete_radius_config()


.. toctree::
    :maxdepth: 1

    models

