import argparse, configparser, nmap3, getpass


def run_nmap(host):
    class Target(object):
        def __init__(self, host):
            config.read("/home/lerusse/Documents/python_projects/ctf_scanner/config.ini")
            
            if "http" in host:
                self.host_ip = host.split("://")[1]
            else:
                self.host_ip = host

            if getpass.getuser() == "root":
                self.is_root = True
            else:
                self.is_root = False
            # From the config file

            self.speed = config.get("NMAP", "SPEED", fallback=4)
            self.os_scan = config.get("NMAP", "OS", fallback=False)
            self.service_ver = config.get("NMAP", "SERVICE_VERSION", fallback=True)
            self.subnet = config.get("NMAP", "SUBNET", fallback=False)
            self.no_ping = config.get("NMAP", "NO_PING", fallback=False)
            self.quick_scan = config.get("NMAP", "QUICK_SCAN", fallback=False)
            self.port_first = config.get("NMAP", "FIRST_PORT", fallback=1)
            self.port_last = config.get("NMAP", "LAST_PORT", fallback=65535)
            self.scripts = config.get("NMAP", "SCRIPTS", fallback="Default")
            # determine how to handle the output files and name
            self.output = config.get("NMAP", "OUTPUT", fallback="./")

    def gen_arguments():
        arguments = f"-T{target.speed} -p{target.port_first}-{target.port_last}"
        if target.is_root == True:
            arguments += " -sS"
            if target.os_scan == "True":
                arguments += " -O"
        if target.os_scan == "True" and not target.is_root:
            print("To use OS scan please run as root.")
            exit()
        
        if target.service_ver == "True":
            arguments += " -sV"
        if target.no_ping == "True":
            arguments += " -Pn"
        if target.subnet == "True":
            target.host_ip += "/24"
        #arguments += f"-oN {target.output}"

        print(target.host_ip, arguments)
        return arguments

    target = Target(host)
    nmap = nmap3.Nmap()
    arguments = gen_arguments()
    print(nmap.scan_top_ports(target.host_ip, args=arguments))



if __name__ == "__main__":
    # Make this more intelligent
    parser = argparse.ArgumentParser(
        description="Scan web challenges from TryHackme or Vulnhub",
        usage="%(prog)s [config directory]",
    )

    # if len(sys.argv) == 1:
    #     parser.print_help()

    args = parser.parse_args()

    # Implement file existence check
    config = configparser.ConfigParser()
    try:
        with open("config.ini", "r") as f:
            run_nmap("192.168.0.28")
    except IOError:
        print("Couldn't find 'config.ini'. Please make sure it's in the same folder.")
