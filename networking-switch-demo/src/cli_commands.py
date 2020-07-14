# === Resource Data ===
def get_chassis_list(cli):
    """CLI flow to get chassis of chassis"""
    return ["chassis1"]


def get_module_list(cli, chassis_name):
    """CLI flow to get modules of chassis"""
    return ["module1", "module2", "module3"]


def get_ports_list(cli, module_name):
    """CLI flow to get ports of module"""
    return ["port1", "port2", "port3"]

# === Attribute Data ===
def get_root_vendor(cli):
    pass


def get_root_model(cli):
    pass


def get_port_ip(cli, port_name):
    pass


if __name__ == "__main__":
    from cloudshell_cli_handler import CreateSession
    host = "192.168.105.40"
    username = "admin"
    password = "admin"

    sample_command = 'show interface | no-more'
    cli = CreateSession(host, username, password)
    chassis_list = get_chassis_list()

