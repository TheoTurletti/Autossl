import os
import subprocess
import sys
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException

instructions = (
    "Autossl - ( https://github.com/TheoTurletti/Autossl )\n"	
    "\nUSAGE: python3 autossl.py [nmap-output.xml | domain-list.txt] [output-file]"
)

if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--h", "-help", "--help"):
    print(instructions)
    sys.exit()
elif len(sys.argv) > 3:
    print(instructions)
    sys.exit()
else:
    input_file = sys.argv[1]
    myfile = sys.argv[2]

    with open(myfile, 'w') as f:
        f.write("====================================================================\n")
        f.write("Autossl - ( https://github.com/TheoTurletti/Autossl )\n")
        f.write("====================================================================\n\n")

    temp = ".tmp-auto-sslscan"
    sslservices = myfile.replace('.txt', '') + "-ssl-services.txt"

    with open(temp, 'w'), open(sslservices, 'w'):
        pass

    print("Autossl - ( https://github.com/TheoTurletti/Autossl )\n")

def report_parser(report):
    ''' Parse the Nmap XML report '''
    for host in report.hosts:
        ip = host.address

        for s in host.services:
            if s.open():
                serv = s.service
                port = s.port
                tunnel = s.tunnel

                if tunnel:
                    print_data(ip, port, tunnel)

def parse_domains_file(filepath):
    ''' Parse the domain list file and perform sslscan '''
    with open(filepath, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]

    for domain in domains:
        print(f'Performing sslscan of {domain}')

        with open(temp, 'w') as f:
            f.write(f'{domain}\n')

        with open(sslservices, 'a') as f:
            f.write(f'{domain}\n')

        with open(myfile, 'a') as f:
            subprocess.call(["sslscan", "--no-failed", "--targets=" + temp], stdout=f)

def print_data(ip, port, tunnel):
    ''' Do something with the nmap data '''
    with open(temp, 'w') as f:
        f.write(f'{ip}:{port}\n')

    print(f'Performing sslscan of {ip}:{port}')

    with open(sslservices, 'a') as f:
        f.write(f'{ip}:{port}\n')

    with open(myfile, 'a') as f:
        subprocess.call(["sslscan", "--no-failed", "--targets=" + temp], stdout=f)

def end():
    print(f"\nsslscan results saved to: {myfile}")
    print(f"SSL services list saved to: {sslservices}")
    os.remove(temp)

def main():
    try:
        if input_file.endswith('.xml'):
            report = NmapParser.parse_fromfile(input_file)
            report_parser(report)
        else:
            parse_domains_file(input_file)

        end()
    except NmapParserException as e:
        print(f"Error parsing Nmap XML: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

main()
