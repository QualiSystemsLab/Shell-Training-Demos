from cloudshell_cli_handler import CreateSession


def get_all_ips(cli):
    """
    :param CreateSession cli:
    :return: list of ips
    :rtype: list
    """
    sample_command = 'hostname -I'
    outp = cli.send_terminal_command(sample_command)
    if not outp:
        raise Exception("Output is empty")
    split_outp = outp.split()
    # remove command line
    all_ips = [line for line in split_outp if _is_valid_ip(line.strip())]
    if not all_ips:
        raise Exception("No valid IPs. input list: {}".format(split_outp))
    return all_ips


def _is_valid_ip(address):
    import socket
    try:
        socket.inet_aton(address)
        return True
    except:
        return False


def _test_valid_ips():
    print _is_valid_ip('10.10.20.30')
    print _is_valid_ip('999.10.20.30')
    print _is_valid_ip('gibberish')


def check_python_version(cli):
    """
    :param CreateSession cli: 
    :return: 
    """
    action_map = {r">>>": lambda session, logger: session.send_line("exit()", logger)}
    # error_map = {r"2.7": "Python Version Incorrect, expected Python 3"}
    outp = cli.send_terminal_command("python", action_map=action_map)
    first_line = outp.splitlines()[0]
    python_version = first_line.split()[1]
    return python_version


if __name__ == "__main__":
    host = "192.168.85.40"
    username = "root"
    password = "qs1234"
    cli = CreateSession(host=host, username=username, password=password)
    # all_ips = get_all_ips(cli)
    python_outp = check_python_version(cli)
    print(python_outp)
    pass

