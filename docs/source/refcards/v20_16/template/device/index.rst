===============
template.device
===============


Operation: GET /dataservice/template/device
-------------------------------------------


Generate template list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get(feature: FeatureParam) -> List[Any]: ...


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
        client.template.device.get()


Operation: PUT /dataservice/template/device/{templateId}
--------------------------------------------------------


Edit template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def put(template_id: str, payload: Any) -> Any: ...


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
        client.template.device.put()


Operation: DELETE /dataservice/template/device/{templateId}
-----------------------------------------------------------


Delete template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def delete(template_id: str) -> None: ...


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
        client.template.device.delete()


.. toctree::
    :maxdepth: 1

    cli
    config/index
    feature
    is_migration_required
    migration
    migration_info
    object
    resource_group
    syncstatus
    featuretemplates
    models

