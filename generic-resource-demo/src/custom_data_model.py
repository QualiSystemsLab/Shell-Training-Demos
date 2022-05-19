from data_model import GenericResourceDemo, ResourcePort
from cloudshell.shell.core.driver_context import ResourceCommandContext, AutoLoadDetails, AutoLoadAttribute, \
    AutoLoadResource
from collections import defaultdict


class CustomGenericResource(GenericResourceDemo):
    def __init__(self, name, root_unique_id):
        super(CustomGenericResource, self).__init__(name)
        self._root_unique_id = root_unique_id

    def create_autoload_details(self, relative_path=''):
        """
        :param relative_path:
        :type relative_path: str
        :return
        """
        resources = [AutoLoadResource(model=self.resources[r].cloudshell_model_name,
                                      name=self.resources[r].name,
                                      relative_address=self._get_relative_path(r, relative_path),
                                      unique_identifier="{}.{}".format(self._root_unique_id, self.resources[r].name))
                     for r in self.resources]
        attributes = [AutoLoadAttribute(relative_path, a, self.attributes[a]) for a in self.attributes]
        autoload_details = AutoLoadDetails(resources, attributes)
        for r in self.resources:
            curr_path = relative_path + '/' + r if relative_path else r
            curr_auto_load_details = self.resources[r].create_autoload_details(curr_path)
            autoload_details = self._merge_autoload_details(autoload_details, curr_auto_load_details)
        return autoload_details

    @classmethod
    def create_from_context(cls, context, root_unique_id):
        """
        Creates an instance of NXOS by given context
        :param context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :return:
        :rtype GenericResourceDemo
        """
        result = CustomGenericResource(name=context.resource.name, root_unique_id=root_unique_id)
        for attr in context.resource.attributes:
            result.attributes[attr] = context.resource.attributes[attr]
        return result


class CustomResourcePort(ResourcePort):
    def __init__(self, name, root_unique_id):
        super(CustomResourcePort, self).__init__(name)
        self._root_unique_id = root_unique_id

    def create_autoload_details(self, relative_path=''):
        """
        :param relative_path:
        :type relative_path: str
        :return
        """
        resources = [AutoLoadResource(model=self.resources[r].cloudshell_model_name,
                                      name=self.resources[r].name,
                                      relative_address=self._get_relative_path(r, relative_path),
                                      unique_identifier="{}.{}".format(self._root_unique_id, self._name))
                     for r in self.resources]
        attributes = [AutoLoadAttribute(relative_path, a, self.attributes[a]) for a in self.attributes]
        autoload_details = AutoLoadDetails(resources, attributes)
        for r in self.resources:
            curr_path = relative_path + '/' + r if relative_path else r
            curr_auto_load_details = self.resources[r].create_autoload_details(curr_path)
            autoload_details = self._merge_autoload_details(autoload_details, curr_auto_load_details)
        return autoload_details
