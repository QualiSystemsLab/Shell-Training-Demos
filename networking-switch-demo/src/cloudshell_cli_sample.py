from cloudshell.cli.service.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.service.command_mode import CommandMode

host = "192.168.105.40"
username = "admin"
password = "admin"

cli = CLI()
mode = CommandMode(r'#') # for example r'%\s*$'

session_types = [SSHSession(host=host,username=username,password=password)]

# extract a session from the pool, send the command and return the session to the pool upon completing the "with"
# block:
with cli.get_session(session_types, mode) as cli_service:
    out = cli_service.send_command('show interface | no-more')
    print(out)

