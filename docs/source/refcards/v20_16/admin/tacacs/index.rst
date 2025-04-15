============
admin.tacacs
============


Operation: GET /dataservice/admin/tacacs
----------------------------------------


Get tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get() -> Tacacs: ...


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
        client.admin.tacacs.get()


Operation: PUT /dataservice/admin/tacacs
----------------------------------------


Update tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def put(payload: Tacacs) -> None: ...


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
        client.admin.tacacs.put()


Operation: POST /dataservice/admin/tacacs
-----------------------------------------


Create tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def post(payload: Tacacs) -> None: ...


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
        client.admin.tacacs.post()


Operation: DELETE /dataservice/admin/tacacs
-------------------------------------------


Delete tacacs configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def delete() -> Tacacs: ...


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
        client.admin.tacacs.delete()


.. toctree::
    :maxdepth: 1

    models

