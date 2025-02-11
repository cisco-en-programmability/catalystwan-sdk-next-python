=============
msla.template
=============


Operation: GET /dataservice/msla/template
-----------------------------------------


Retrieve all MSLA template

.. code:: python

    def get_all_template() -> Any: ...


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
        client.msla.template.get_all_template()


.. toctree::
    :maxdepth: 1

    licenses/index

