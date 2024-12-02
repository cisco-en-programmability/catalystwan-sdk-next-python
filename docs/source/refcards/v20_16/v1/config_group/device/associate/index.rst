================================
v1.config_group.device.associate
================================


Operation: GET /dataservice/v1/config-group/{configGroupId}/device/associate
----------------------------------------------------------------------------


Get devices association with a config group

.. code:: python

    def get_config_group_association(
        config_group_id: str,
    ) -> ResponseSchema: ...


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
        client.v1.config_group.device.associate.get_config_group_association()


Operation: PUT /dataservice/v1/config-group/{configGroupId}/device/associate
----------------------------------------------------------------------------


Move the devices from one config group to another

.. code:: python

    def update_config_group_association(
        config_group_id: str, payload: Optional[Any] = None
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
        client.v1.config_group.device.associate.update_config_group_association()


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/associate
-----------------------------------------------------------------------------


Create associations with device and a config group

.. code:: python

    def create_config_group_association(
        config_group_id: str, payload: Optional[Any] = None
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
        client.v1.config_group.device.associate.create_config_group_association()


Operation: DELETE /dataservice/v1/config-group/{configGroupId}/device/associate
-------------------------------------------------------------------------------


Delete Config Group Association from devices

.. code:: python

    def delete_config_group_association(
        config_group_id: str, payload: Optional[Any] = None
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
        client.v1.config_group.device.associate.delete_config_group_association()


.. toctree::
    :maxdepth: 1

    models

