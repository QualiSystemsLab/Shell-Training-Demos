from cloudshell_cli_handler import CreateSession


def get_chassis_data(cli):
    commands = ["command1", "command "]
    outp = cli.send_terminal_commands(commands)
    pass


def get_module_data(cli, chassis_name):
    pass


def get_port_data(cli, module_name):
    pass


if __name__ == "__main__":
    host = "192.168.105.40"
    username = "admin"
    password = "admin"
    cli = CreateSession(host, username, password)
    chassis_list = get_chassis_data(cli)
    for chassis in chassis_list:
        module_list = get_module_data(chassis)
        for module in module_list:
            port_list = get_port_data(module)
    print(outp)