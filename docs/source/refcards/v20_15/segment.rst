=======
segment
=======


Operation: GET /dataservice/segment
-----------------------------------


Get network segments

.. code:: python

    def get_segments() -> List[Any]: ...


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
        client.segment.get_segments()


Operation: POST /dataservice/segment
------------------------------------


Create network segment

.. code:: python

    def create_segment(payload: Optional[Any] = None) -> Any: ...


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
        client.segment.create_segment()


Operation: GET /dataservice/segment/{id}
----------------------------------------


Get network segment

.. code:: python

    def get_segment(id: str) -> List[Any]: ...


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
        client.segment.get_segment()


Operation: PUT /dataservice/segment/{id}
----------------------------------------


Edit network segment

.. code:: python

    def edit_segment(id: str, payload: Optional[Any] = None) -> None: ...


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
        client.segment.edit_segment()


Operation: DELETE /dataservice/segment/{id}
-------------------------------------------


Delete network segment

.. code:: python

    def delete_segment(id: str) -> None: ...


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
        client.segment.delete_segment()


