===============
v1.config_group
===============


Operation: POST /dataservice/v1/config-group
--------------------------------------------


Create a new Configuration Group

.. code:: python

    def post(
        payload: CreateConfigGroupPostRequest,
    ) -> CreateConfigGroupPostResponse: ...


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
        client.v1.config_group.post()


Operation: PUT /dataservice/v1/config-group/{configGroupId}
-----------------------------------------------------------


Edit a Configuration Group

.. code:: python

    def put(
        config_group_id: str, payload: EditConfigGroupPutRequest
    ) -> EditConfigGroupPutResponse: ...


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
        client.v1.config_group.put()


Operation: DELETE /dataservice/v1/config-group/{configGroupId}
--------------------------------------------------------------


Delete Config Group

.. code:: python

    def delete(
        config_group_id: str, delete_profiles: Optional[bool] = None
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
        client.v1.config_group.delete()


Operation: GET /dataservice/v1/config-group
-------------------------------------------


.. code:: python

    @overload
    def get(
        solution: Optional[str] = None, name: Optional[str] = None
    ) -> List[ConfigGroup]: ...


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
        client.v1.config_group.get()


Operation: GET /dataservice/v1/config-group/{configGroupId}
-----------------------------------------------------------


.. code:: python

    @overload
    def get(
        config_group_id: str, device_list: Optional[bool] = True
    ) -> ConfigGroup: ...


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
        client.v1.config_group.get()


.. toctree::
    :maxdepth: 1

    device/index
    rules
    models

