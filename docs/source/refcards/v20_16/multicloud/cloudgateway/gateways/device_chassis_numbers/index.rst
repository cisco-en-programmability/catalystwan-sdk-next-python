=======================================================
multicloud.cloudgateway.gateways.device_chassis_numbers
=======================================================


Operation: GET /dataservice/multicloud/cloudgateway/{cloudType}/gateways/device-chassis-numbers
-----------------------------------------------------------------------------------------------


API to retrieve available devices or devices associated to a config group.

.. code:: python

    def get(
        cloud_type: str,
        config_group_id: Optional[str] = None,
        device_solution_type: Optional[str] = None,
    ) -> List[InlineResponse200]: ...


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
        client.multicloud.cloudgateway.gateways.device_chassis_numbers.get()


.. toctree::
    :maxdepth: 1

    models

