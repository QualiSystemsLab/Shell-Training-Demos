from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder
from cloudshell.devices.driver_helper import get_api
from cloudshell.devices.driver_helper import get_logger_with_thread_id
from cloudshell.devices.standards.sdn.autoload_structure import GenericSDNSwitch
from cloudshell.devices.standards.sdn.autoload_structure import GenericSDNPort
from cloudshell.devices.standards.sdn.autoload_structure import SDNControllerResource
from cloudshell.devices.standards.sdn.configuration_attributes_structure import GenericSDNResource
from cloudshell.shell.core.driver_utils import GlobalLock
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import AutoLoadDetails
from data_model import *


class SdnDemoDriver(ResourceDriverInterface, GlobalLock):

    def __init__(self):
        """Must be without arguments, it is created with reflection at a run time"""
        pass

    def initialize(self, context):
        """Initialize method

        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param cloudshell.shell.core.context.driver_context.InitCommandContext context:
        """
        pass

    @GlobalLock.lock
    def get_inventory(self, context):
        """Return device structure with all standard attributes
        :param AutoLoadCommandContext context: the context the command runs on
        :return Attribute and sub-resource information for the Shell resource you can return an AutoLoadDetails object
        :rtype: AutoLoadDetails
        """

        # === SAMPLE CODE ===
        resource = SDNControllerResource(shell_name="shell name",
                                         name="snd controller name",
                                         unique_id="snd controller id")

        switch1 = GenericSDNSwitch(shell_name="shell name",
                                   name="sdn switch 1",
                                   unique_id="sdn switch id 1")

        resource.add_sub_resource("1", switch1)

        port1 = GenericSDNPort(shell_name="shell name",
                               name="sdn port 1",
                               unique_id="sdn port id 1")

        port1.mac_address = 'fe80::e10c:f055:f7f1:bb7t16'
        port1.ipv4_address = '192.168.10.7'
        switch1.add_sub_resource("1", port1)

        return AutoloadDetailsBuilder(resource).autoload_details()

        # return AutoLoadDetails([], [])

    def cleanup(self):
        """Destroy the driver session

        This function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    def ApplyConnectivityChanges(self, context, request):
        """Create vlan and add or remove it to/from network interface

        :param ResourceCommandContext context: ResourceCommandContext object with all Resource Attributes inside
        :param str request: request json
        :return:
        """
        pass

    @GlobalLock.lock
    def remove_openflow(self, context, node_id, table_id, flow_id):
        """Remove openflow entry from controller by its id

        :param ResourceCommandContext context: ResourceCommandContext object with all Resource Attributes inside
        :param str node_id:
        :param int table_id:
        :param str flow_id:
        :return: response
        :rtype: str
        """
        pass
