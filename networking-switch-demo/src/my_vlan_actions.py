from cloudshell.shell.flows.connectivity.models.connectivity_request import ConnectivityActionRequest
from cloudshell.shell.flows.connectivity.models.connectivity_result import ConnectivitySuccessResponse


def my_add_vlan_action(cli, action):
    """

    :param ConnectivityActionRequest action:
    :return:
    """
    action_target = action.actionTarget
    full_address = action_target.fullAddress
    port = full_address.split("/")[-1]

    params = action.connectionParams
    vlan_id = params.vlanId

    # DO CLI ACTIONS


    return ConnectivitySuccessResponse(action, "Success")

    pass


def my_remove_vlan_action(action):
    """

    :param ConnectivityActionRequest action:
    :return:
    """
    action_target = action.actionTarget
    full_name = action_target.fullName
    pass