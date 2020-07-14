from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, CancellationContext, AutoLoadCommandContext
from data_model import *  # run 'shellfoundry generate' to generate data model classes


class PduDemoDriver(ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    # <editor-fold desc="Discovery">

    def get_inventory(self, context):
        """
        Discovers the resource structure and attributes.
        :param AutoLoadCommandContext context: the context the command runs on
        :return Attribute and sub-resource information for the Shell resource you can return an AutoLoadDetails object
        :rtype: AutoLoadDetails
        """
        # See below some example code demonstrating how to return the resource structure and attributes
        # In real life, this code will be preceded by SNMP/other calls to the resource details and will not be static
        # run 'shellfoundry generate' in order to create classes that represent your data model

        resource = PduDemo.create_from_context(context)
        context.
        resource.vendor = 'specify the shell vendor'
        resource.model = 'specify the shell model'

        p1 = PowerSocket('p1')
        resource.add_sub_resource('1', p1)

        p2 = PowerSocket('p2')
        resource.add_sub_resource('2', p2)

        p3 = PowerSocket('p3')
        resource.add_sub_resource('3', p3)
        return resource.create_autoload_details()

        # return AutoLoadDetails([], [])

    # </editor-fold>

    def PowerOn(self, context, ports):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        context.
        api = CloudShellAPISession(host=context.connectivity.server_address,
                                   token_id=context.connectivity.admin_auth_token,
                                   domain=context.remote_reservation.domain)
        res_id = context.remote_reservation.reservation_id
        remote_endpoint_1 = context.remote_endpoints[0]
        remote_ep1_full_name = remote_endpoint_1.fullname
        remote_ep1_model = remote_endpoint_1.model
        endpoint_names = [ep.name for ep in context.remote_endpoints]
        all_ep_msg = "DUT ports passed: {}, Remote Endpoint Names: {}".format(ports, endpoint_names)
        api.WriteMessageToReservationOutput(res_id, all_ep_msg)
        return "Running command on single end point '{}', with model '{}'".format(remote_ep1_full_name,
                                                                                  remote_ep1_model)

    def PowerOff(self, context, ports):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        pass

    def PowerCycle(self, context, ports, delay):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        pass

    def my_power_on(self, context, ports, custom_var):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        api = CloudShellAPISession(host=context.connectivity.server_address,
                                   token_id=context.connectivity.admin_auth_token,
                                   domain=context.remote_reservation.domain)
        res_id = context.remote_reservation.reservation_id
        context.
        remote_endpoint_1 = context.remote_endpoints[0]
        remote_ep1_full_name = remote_endpoint_1.fullname
        remote_ep1_model = remote_endpoint_1.model
        endpoint_names = [ep.name for ep in context.remote_endpoints]
        all_ep_msg = "DUT ports passed: {}, Remote Endpoint Names: {}".format(ports, endpoint_names)
        api.WriteMessageToReservationOutput(res_id, all_ep_msg)
        return "Running command on single end point '{}', with model '{}'".format(remote_ep1_full_name,
                                                                                  remote_ep1_model)
        pass

    # </editor-fold>
