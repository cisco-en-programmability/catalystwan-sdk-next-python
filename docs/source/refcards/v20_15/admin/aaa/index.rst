=========
admin.aaa
=========


Operation: GET /dataservice/admin/aaa
-------------------------------------


Get aaa configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get_aaa_config() -> Aaa: ...


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
        client.admin.aaa.get_aaa_config()


Operation: PUT /dataservice/admin/aaa
-------------------------------------


Update aaa configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def update_aaa_config(payload: Optional[Aaa] = None) -> None: ...


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
        client.admin.aaa.update_aaa_config()


Operation: POST /dataservice/admin/aaa
--------------------------------------


Create aaa configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def create_aaa_config(payload: Optional[Aaa] = None) -> None: ...


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
        client.admin.aaa.create_aaa_config()


Operation: DELETE /dataservice/admin/aaa
----------------------------------------


Delete aaa configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def delete_aaa_config() -> None: ...


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
        client.admin.aaa.delete_aaa_config()


.. toctree::
    :maxdepth: 1

    models

