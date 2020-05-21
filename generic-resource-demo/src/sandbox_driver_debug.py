from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, ConnectivityContext, \
    Connector, ReservationContextDetails, ResourceContextDetails
import driver as my_driver

LIVE_SANDBOX_ID = "33b70f5a-ed37-40de-87a0-b2125fa7245b"
RESOURCE_NAME = "<Resource name>"
CS_SERVER = "qs-il-lt-nattik"

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

debug_driver_instance = my_driver.GenericResourceDemoDriver()
res = debug_driver_instance.hello_world(context)
pass
