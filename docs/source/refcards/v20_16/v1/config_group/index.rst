===============
v1.config_group
===============


Operation: GET /dataservice/v1/config-group
-------------------------------------------


Get a Configuration Group by Solution

.. code:: python

    def get_config_group_by_solution(
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
        client.v1.config_group.get_config_group_by_solution()


Operation: POST /dataservice/v1/config-group
--------------------------------------------


Create a new Configuration Group

.. code:: python

    def create_config_group(payload: Optional[str] = None) -> str: ...


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
        client.v1.config_group.create_config_group()


Operation: GET /dataservice/v1/config-group/{configGroupId}
-----------------------------------------------------------


Get a Configuration Group by ID

.. code:: python

    def get_config_group(
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
        client.v1.config_group.get_config_group()


Operation: PUT /dataservice/v1/config-group/{configGroupId}
-----------------------------------------------------------


Edit a Configuration Group

.. code:: python

    def edit_config_group(
        config_group_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.config_group.edit_config_group()


Operation: DELETE /dataservice/v1/config-group/{configGroupId}
--------------------------------------------------------------


Delete Config Group

.. code:: python

    def delete_config_group(
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
        client.v1.config_group.delete_config_group()


.. toctree::
    :maxdepth: 1

    device/index
    rules
    models

