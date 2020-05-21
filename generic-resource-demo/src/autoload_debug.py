from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
from cloudshell.shell.core.driver_context import AutoLoadCommandContext, ResourceCommandContext, ConnectivityContext, \
    Connector, ReservationContextDetails, ResourceContextDetails, AppContext
import driver as my_driver

RESOURCE_NAME = "generic_resource_1"
RESOURCE_ADDRESS = "1.1.1.1"
RESOURCE_FAMILY = "CS_GenericResource"
RESOURCE_MODEL = "Generic Resource Demo"
USER_NAME = "root"
PASSWORD = "Password1"
SNMP_READ_COMMUNITY = "public"

CS_SERVER = "localhost"

# ==== Setting resource attributes ===
resource_attributes = dict()
resource_attributes["{}.User".format(RESOURCE_MODEL)] = USER_NAME
resource_attributes["{}.Password".format(RESOURCE_MODEL)] = PASSWORD
resource_attributes["{}.SNMP Read Community".format(RESOURCE_MODEL)] = SNMP_READ_COMMUNITY

resource_context = ResourceContextDetails(id="",
                                          name=RESOURCE_NAME,
                                          fullname="",
                                          type="Resource",
                                          address=RESOURCE_ADDRESS,
                                          model=RESOURCE_MODEL,
                                          family=RESOURCE_FAMILY,
                                          description="",
                                          attributes=resource_attributes,
                                          app_context=AppContext("", ""),
                                          networks_info=None,
                                          shell_standard="",
                                          shell_standard_version="")


connectivity_context = ConnectivityContext(server_address=CS_SERVER,
                                           cloudshell_api_port="8028",
                                           quali_api_port="9000",
                                           admin_auth_token="",
                                           cloudshell_version="9.3",
                                           cloudshell_api_scheme="")

context = AutoLoadCommandContext(
    connectivity=connectivity_context,
    resource=resource_context,
)

debug_driver = my_driver.GenericResourceDemoDriver()
debug_driver.get_inventory(context)
pass
