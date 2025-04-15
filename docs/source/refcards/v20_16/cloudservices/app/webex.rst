=======================
cloudservices.app.webex
=======================


Operation: PUT /dataservice/cloudservices/app/webex
---------------------------------------------------


Day N- Update Webex App

.. code:: python

    def put(payload: Any) -> List[Any]: ...


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
        client.cloudservices.app.webex.put()


Operation: POST /dataservice/cloudservices/app/webex
----------------------------------------------------


Add Webex App

.. code:: python

    def post(payload: Any) -> List[Any]: ...


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
        client.cloudservices.app.webex.post()


Operation: DELETE /dataservice/cloudservices/app/webex
------------------------------------------------------


deleteWebexPrefixLists

.. code:: python

    def delete(payload: Optional[Any] = None) -> List[Any]: ...


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
        client.cloudservices.app.webex.delete()


