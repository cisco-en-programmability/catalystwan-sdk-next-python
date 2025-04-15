================
template.feature
================


Operation: POST /dataservice/template/feature
---------------------------------------------


Create feature template

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.feature.post()


Operation: PUT /dataservice/template/feature/{templateId}
---------------------------------------------------------


Update feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.template.feature.put()


Operation: DELETE /dataservice/template/feature/{templateId}
------------------------------------------------------------


Delete feature template

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
        client.template.feature.delete()


Operation: GET /dataservice/template/feature
--------------------------------------------


.. code:: python

    @overload
    def get(
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
        client.template.feature.get()


Operation: GET /dataservice/template/feature/{deviceType}
---------------------------------------------------------


.. code:: python

    @overload
    def get(device_type: str) -> List[Any]: ...


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
        client.template.feature.get()


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

