=============
template.lock
=============


Operation: PUT /dataservice/template/lock/{processId}
-----------------------------------------------------


Update lease

.. code:: python

    def put(process_id: str) -> None: ...


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
        client.template.lock.put()


Operation: DELETE /dataservice/template/lock/{processId}
--------------------------------------------------------


Remove lock

.. code:: python

    def delete(process_id: str) -> None: ...


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
        client.template.lock.delete()


