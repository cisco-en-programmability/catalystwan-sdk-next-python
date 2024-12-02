===================
template.feature.li
===================


Operation: GET /dataservice/template/feature/li
-----------------------------------------------


Get LI feature template

.. code:: python

    def list_li_template() -> List[Any]: ...


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
        client.template.feature.li.list_li_template()


Operation: POST /dataservice/template/feature/li
------------------------------------------------


Create LI feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_li_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.feature.li.create_li_template()


Operation: PUT /dataservice/template/feature/li/{templateId}
------------------------------------------------------------


Update LI feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def edit_li_template(
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
        client.template.feature.li.edit_li_template()


