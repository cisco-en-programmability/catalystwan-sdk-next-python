=====================
networkdesign.circuit
=====================


Operation: GET /dataservice/networkdesign/circuit
-------------------------------------------------


Deprecated!!!

Get network circuits

.. code:: python

    def get_circuits() -> Any: ...


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
        client.networkdesign.circuit.get_circuits()


Operation: POST /dataservice/networkdesign/circuit
--------------------------------------------------


Deprecated!!!

Create network circuits

.. code:: python

    def create_circuit(payload: Optional[Any] = None) -> Any: ...


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
        client.networkdesign.circuit.create_circuit()


Operation: DELETE /dataservice/networkdesign/circuit/{id}
---------------------------------------------------------


Deprecated!!!

Delete network circuits

.. code:: python

    def delete_circuit(id: str) -> None: ...


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
        client.networkdesign.circuit.delete_circuit()


