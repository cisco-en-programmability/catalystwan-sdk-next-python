=======================================
template.policy.ise.identity.referenced
=======================================


Operation: GET /dataservice/template/policy/ise/identity/referenced/{listType}
------------------------------------------------------------------------------


Get all referenced Lists

.. code:: python

    def get_list_reference(list_type: str) -> List[ReferencedList]: ...


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
        client.template.policy.ise.identity.referenced.get_list_reference()


.. toctree::
    :maxdepth: 1

    models

