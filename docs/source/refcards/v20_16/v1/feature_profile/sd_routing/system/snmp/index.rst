=========================================
v1.feature_profile.sd_routing.system.snmp
=========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp
---------------------------------------------------------------------------------


Create a SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateSdroutingSnmpFeaturePostRequest
    ) -> CreateSdroutingSnmpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
-----------------------------------------------------------------------------------------


Edit the SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def put(
        system_id: str,
        snmp_id: str,
        payload: EditSdroutingSnmpFeaturePutRequest,
    ) -> EditSdroutingSnmpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
--------------------------------------------------------------------------------------------


Delete the SD-Routing SNMP feature from a specific system feature profile

.. code:: python

    def delete(system_id: str, snmp_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemSnmpSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, snmp_id: str
    ) -> GetSingleSdRoutingSystemSnmpSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.snmp.get()


.. toctree::
    :maxdepth: 1

    models

