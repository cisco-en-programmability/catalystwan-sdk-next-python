=====================
opentaccase.scmwidget
=====================


Operation: GET /dataservice/opentaccase/scmwidget/{var}
-------------------------------------------------------


Deprecated!!!

Proxy API for SCM Widget

.. code:: python

    def get() -> List[Any]: ...


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
        client.opentaccase.scmwidget.get()


Operation: POST /dataservice/opentaccase/scmwidget/{var}
--------------------------------------------------------


Deprecated!!!

Prxoy API for SCM Widget

.. code:: python

    def post() -> List[Any]: ...


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
        client.opentaccase.scmwidget.post()


Operation: DELETE /dataservice/opentaccase/scmwidget/{var}
----------------------------------------------------------


Deprecated!!!

Proxy API for SCM Widget

.. code:: python

    def delete() -> List[Any]: ...


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
        client.opentaccase.scmwidget.delete()


