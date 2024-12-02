=========================
template.policy.customapp
=========================


Operation: GET /dataservice/template/policy/customapp
-----------------------------------------------------


Get all policy custom applications

.. code:: python

    def get_custom_apps() -> List[Any]: ...


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
        client.template.policy.customapp.get_custom_apps()


Operation: POST /dataservice/template/policy/customapp
------------------------------------------------------


Create a policy custom applications

.. code:: python

    def create_custom_app(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.customapp.create_custom_app()


Operation: GET /dataservice/template/policy/customapp/{id}
----------------------------------------------------------


Get a policy custom applications

.. code:: python

    def get_custom_app_by_id(id: str) -> Any: ...


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
        client.template.policy.customapp.get_custom_app_by_id()


Operation: PUT /dataservice/template/policy/customapp/{id}
----------------------------------------------------------


Edit a policy custom applications

.. code:: python

    def edit_custom_app(
        id: str, payload: Optional[Any] = None
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
        client.template.policy.customapp.edit_custom_app()


Operation: DELETE /dataservice/template/policy/customapp/{id}
-------------------------------------------------------------


Delete a policy custom applications

.. code:: python

    def delete_custom_app(id: str) -> None: ...


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
        client.template.policy.customapp.delete_custom_app()


