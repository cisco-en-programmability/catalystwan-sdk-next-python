===========================
template.cloudx.attacheddia
===========================


Operation: GET /dataservice/template/cloudx/attacheddia
-------------------------------------------------------


Get attached Dia site list

.. code:: python

    def get_attached_dia_list() -> List[Any]: ...


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
        client.template.cloudx.attacheddia.get_attached_dia_list()


