=======================
cloudservices.app.webex
=======================


Operation: PUT /dataservice/cloudservices/app/webex
---------------------------------------------------


Day N- Update Webex App

.. code:: python

    def enable_webex_1(payload: Optional[Any] = None) -> List[Any]: ...


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
        client.cloudservices.app.webex.enable_webex_1()


Operation: POST /dataservice/cloudservices/app/webex
----------------------------------------------------


Add Webex App

.. code:: python

    def enable_webex(payload: Optional[Any] = None) -> List[Any]: ...


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
        client.cloudservices.app.webex.enable_webex()


Operation: DELETE /dataservice/cloudservices/app/webex
------------------------------------------------------


deleteWebexPrefixLists

.. code:: python

    def delete_webex_prefix_lists(
        payload: Optional[Any] = None,
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
        client.cloudservices.app.webex.delete_webex_prefix_lists()


