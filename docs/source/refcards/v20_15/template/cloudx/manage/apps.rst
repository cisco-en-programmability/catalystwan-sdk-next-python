===========================
template.cloudx.manage.apps
===========================


Operation: GET /dataservice/template/cloudx/manage/apps
-------------------------------------------------------


Get apps and vpns

.. code:: python

    def get_apps() -> List[Any]: ...


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
        client.template.cloudx.manage.apps.get_apps()


Operation: PUT /dataservice/template/cloudx/manage/apps
-------------------------------------------------------


Edit apps and vpns

.. code:: python

    def edit_apps(payload: Optional[Any] = None) -> Any: ...


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
        client.template.cloudx.manage.apps.edit_apps()


Operation: POST /dataservice/template/cloudx/manage/apps
--------------------------------------------------------


Add apps and vpns

.. code:: python

    def add_apps(payload: Optional[Any] = None) -> List[Any]: ...


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
        client.template.cloudx.manage.apps.add_apps()


