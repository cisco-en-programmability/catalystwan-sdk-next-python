================
template.feature
================


Operation: GET /dataservice/template/feature
--------------------------------------------


Get feature template list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def generate_feature_template_list(
        summary: Optional[bool] = False,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
    ) -> List[Any]: ...


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
        client.template.feature.generate_feature_template_list()


Operation: POST /dataservice/template/feature
---------------------------------------------


Create feature template

.. code:: python

    def create_feature_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.feature.create_feature_template()


Operation: GET /dataservice/template/feature/{deviceType}
---------------------------------------------------------


Generate template based on device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def generate_template_by_device_type(
        device_type: str,
    ) -> List[Any]: ...


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
        client.template.feature.generate_template_by_device_type()


Operation: PUT /dataservice/template/feature/{templateId}
---------------------------------------------------------


Update feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def edit_feature_template(
        template_id: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.template.feature.edit_feature_template()


Operation: DELETE /dataservice/template/feature/{templateId}
------------------------------------------------------------


Delete feature template

.. code:: python

    def delete_general_template(template_id: str) -> None: ...


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
        client.template.feature.delete_general_template()


.. toctree::
    :maxdepth: 1

    clone
    default/index
    definition
    devicetemplates
    li
    master
    migration
    object
    resource_group
    types/index

