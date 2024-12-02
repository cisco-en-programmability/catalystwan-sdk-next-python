============
admin.tacacs
============


Operation: GET /dataservice/admin/tacacs
----------------------------------------


Get tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get_tacacs_config() -> Tacacs: ...


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
        client.admin.tacacs.get_tacacs_config()


Operation: PUT /dataservice/admin/tacacs
----------------------------------------


Update tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def update_tacacs_config(
        payload: Optional[Tacacs] = None,
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
        client.admin.tacacs.update_tacacs_config()


Operation: POST /dataservice/admin/tacacs
-----------------------------------------


Create tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def create_tacacs_config(
        payload: Optional[Tacacs] = None,
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
        client.admin.tacacs.create_tacacs_config()


Operation: DELETE /dataservice/admin/tacacs
-------------------------------------------


Delete tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def delete_tacacs_config() -> Tacacs: ...


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
        client.admin.tacacs.delete_tacacs_config()


.. toctree::
    :maxdepth: 1

    models

