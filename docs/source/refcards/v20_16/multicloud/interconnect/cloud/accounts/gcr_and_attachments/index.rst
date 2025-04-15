==========================================================
multicloud.interconnect.cloud.accounts.gcr_and_attachments
==========================================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/gcr-and-attachments
----------------------------------------------------------------------------------------------------------------------


API to get Google Cloud Router and Attachments.

.. code:: python

    def get(
        cloud_type: CloudTypeParam,
        cloud_account_id: str,
        connectivity_gateway_name: Optional[str] = None,
        cloud_gateway_name: Optional[str] = None,
        region: Optional[str] = None,
        network: Optional[str] = None,
        resource_state: Optional[str] = None,
        refresh: Optional[str] = "false",
    ) -> InlineResponse20010: ...


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
        client.multicloud.interconnect.cloud.accounts.gcr_and_attachments.get()


.. toctree::
    :maxdepth: 1

    models

