==================================
template.policy.clouddiscoveredapp
==================================


Operation: GET /dataservice/template/policy/clouddiscoveredapp
--------------------------------------------------------------


Get all cloud discovered applications

.. code:: python

    def get_cloud_discovered_apps() -> List[Any]: ...


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
        client.template.policy.clouddiscoveredapp.get_cloud_discovered_apps()


Operation: POST /dataservice/template/policy/clouddiscoveredapp
---------------------------------------------------------------


Set SLA class for policy cloud discovered applications

.. code:: python

    def map_traffic_profiles(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.clouddiscoveredapp.map_traffic_profiles()


