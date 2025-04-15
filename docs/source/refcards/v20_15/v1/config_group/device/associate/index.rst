================================
v1.config_group.device.associate
================================


Operation: GET /dataservice/v1/config-group/{configGroupId}/device/associate
----------------------------------------------------------------------------


Get devices association with a config group

.. code:: python

    def get(
        config_group_id: str,
    ) -> GetConfigGroupAssociationGetResponse: ...


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
        client.v1.config_group.device.associate.get()


Operation: PUT /dataservice/v1/config-group/{configGroupId}/device/associate
----------------------------------------------------------------------------


Move the devices from one config group to another

.. code:: python

    def put(
        config_group_id: str,
        payload: UpdateConfigGroupAssociationPutRequest,
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
        client.v1.config_group.device.associate.put()


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/associate
-----------------------------------------------------------------------------


Create associations with device and a config group

.. code:: python

    def post(
        config_group_id: str,
        payload: CreateConfigGroupAssociationPostRequest,
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
        client.v1.config_group.device.associate.post()


Operation: DELETE /dataservice/v1/config-group/{configGroupId}/device/associate
-------------------------------------------------------------------------------


Delete Config Group Association from devices

.. code:: python

    def delete(
        config_group_id: str,
        payload: Optional[
            DeleteConfigGroupAssociationDeleteRequest
        ] = None,
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
        client.v1.config_group.device.associate.delete()


.. toctree::
    :maxdepth: 1

    models

