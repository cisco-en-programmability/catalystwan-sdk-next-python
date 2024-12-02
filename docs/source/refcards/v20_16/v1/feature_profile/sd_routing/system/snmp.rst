=========================================
v1.feature_profile.sd_routing.system.snmp
=========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp
--------------------------------------------------------------------------------


Get all SD-Routing SNMP features from a specific system feature profile

.. code:: python

    def get_sdrouting_snmp_features(system_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.get_sdrouting_snmp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp
---------------------------------------------------------------------------------


Create a SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def create_sdrouting_snmp_feature(
        system_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.create_sdrouting_snmp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
-----------------------------------------------------------------------------------------


Get the SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def get_sdrouting_snmp_feature(
        system_id: str, snmp_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.get_sdrouting_snmp_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
-----------------------------------------------------------------------------------------


Edit the SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def edit_sdrouting_snmp_feature(
        system_id: str, snmp_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.edit_sdrouting_snmp_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
--------------------------------------------------------------------------------------------


Delete the SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def delete_sdrouting_snmp_feature(
        system_id: str, snmp_id: str
    ) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.delete_sdrouting_snmp_feature()


