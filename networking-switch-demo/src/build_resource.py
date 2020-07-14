from data_model import *  # run 'shellfoundry generate' to generate data model classes
from cli_commands import *


class BuildResourceFlow(object):
    def __init__(self, resource, cli):
        """
        :param cli:
        :param NetworkingSwitchDemo resource:
        """
        self._cli = cli
        self.resource = resource

    def _build_ports(self, module_resource, port_index, port_name):
        port = GenericPort(port_name)
        port.mac_address = 'fe80::e10c:f055:f7f1:bb7t16'
        port.ipv4_address = '192.168.10.7'
        module_resource.add_sub_resource(str(port_index + 1), port)

    def _build_modules(self, chassis_resource, module_index, module_name):
        """ Add Module sub resource then build ports """
        module_resource = GenericModule(module_name)
        module_resource.model = 'WS-X4232-GB-RJ'
        chassis_resource.add_sub_resource(str(module_index + 1), module_resource)

        # build ports of modules
        ports_list = get_ports_list(self._cli, module_name)
        for port_index, port_name in enumerate(ports_list):
            self._build_ports(module_resource, port_index, port_name)

    def _build_chassis(self, chassis_index, chassis_name):
        """ Add Chassis sub resource then build modules """
        chassis_resource = GenericChassis(chassis_name)
        chassis_resource.model = 'WS-X4232-GB-RJ'
        self.resource.add_sub_resource(str(chassis_index + 1), chassis_resource)

        # build modules of chassis
        module_list = get_module_list(self._cli, chassis_name)
        for module_index, module_name in enumerate(module_list):
            self._build_modules(chassis_resource, module_index, module_name)

    def build_resource(self):
        self.resource.vendor = 'specify the shell vendor'
        self.resource.model = 'specify the shell model'

        chassis_list = get_chassis_list(self._cli)
        for chassis_index, chassis_name in enumerate(chassis_list):
            self._build_chassis(chassis_index, chassis_name)

        return self.resource


