from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, ConnectivityContext, \
    Connector, ReservationContextDetails, ResourceContextDetails
import driver as my_driver

LIVE_SANDBOX_ID = "97bf055e-dddc-46ed-a868-f2946bda9444"
RESOURCE_NAME = "compute demo"
CS_SERVER = "localhost"

attach_to_cloudshell_as(
    user='admin',
    password='admin',
    domain='Global',
    server_address=CS_SERVER,
    reservation_id=LIVE_SANDBOX_ID,
    resource_name=RESOURCE_NAME
)

session = sh.get_api_session()
token = session.token_id

resource_context_details = sh.get_resource_context_details()
reservation_context_details = sh.get_reservation_context_details()
reservation_context = ReservationContextDetails(environment_name=reservation_context_details.environment_name,
                                                environment_path=reservation_context_details.environment_path,
                                                domain=reservation_context_details.domain,
                                                description=reservation_context_details.description,
                                                owner_user=reservation_context_details.owner_user,
                                                owner_email="natti.k@quali.com",
                                                reservation_id=reservation_context_details.id,
                                                saved_sandbox_name="",
                                                saved_sandbox_id="",
                                                running_user="")

connectivity_context_details = sh.get_connectivity_context_details()
cs_api_port = connectivity_context_details.cloudshell_api_port
connectivity_context = ConnectivityContext(server_address=CS_SERVER, cloudshell_api_port=cs_api_port,
                                           quali_api_port="9000",
                                           admin_auth_token=token, cloudshell_version="9.3", cloudshell_api_scheme="")

context = ResourceCommandContext(
    connectivity=connectivity_context,
    resource=resource_context_details,
    reservation=reservation_context,
    connectors=[]
)

debug_driver_instance = my_driver.ComputeDemoDriver()
# res = debug_driver_instance.send_custom_command(context, "ifconfig")
res = debug_driver_instance.get_all_ips(context)
print(res)
pass
