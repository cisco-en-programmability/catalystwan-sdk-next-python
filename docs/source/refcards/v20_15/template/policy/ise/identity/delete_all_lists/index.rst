=============================================
template.policy.ise.identity.delete_all_lists
=============================================


Operation: DELETE /dataservice/template/policy/ise/identity/deleteAllLists
--------------------------------------------------------------------------


Delete all lists of the specified list type

.. code:: python

    def delete(payload: Optional[DeleteAllListsBody] = None) -> bool: ...


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
        client.template.policy.ise.identity.delete_all_lists.delete()


.. toctree::
    :maxdepth: 1

    models

