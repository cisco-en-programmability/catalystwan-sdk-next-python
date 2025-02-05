======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    CloudTypeParam = Literal["AWS", "AZURE", "GCP"]


    class GcpInterconnectAttachment:
        """
        Google cloud Interconnect Attachment Object.
        """

        cloud_router_ip_address: Optional[str]
        customer_ip_address: Optional[str]
        id: Optional[str]
        # MTU of the Interconnect attachment
        mtu: Optional[str]
        name: Optional[str]
        pairing_key: Optional[str]
        region: Optional[str]
        # Option to create Interconnect attachment in secondary zone
        secondary_zone: Optional[str]
        state: Optional[str]


    class GcpCloudRouter:
        """
        Google cloud GCR Object.
        """

        name: str
        network: str
        # List of GCR Attachments
        attachment_details: Optional[List[GcpInterconnectAttachment]]
        cloud_router_asn: Optional[str]
        id: Optional[str]
        region: Optional[str]


    class InlineResponse20010:
        gcp_cloud_routers: Optional[List[GcpCloudRouter]]


