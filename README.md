# Autossl

Autossl is a python script designed to automate the process of conducting ssl scanning via sslcan (https://github.com/rbsec/sslscan).

The Autossl script parses an nmap.xml output file, extracts all SSL services and automatically performs an sslscan of them.


## Installation

git clone https://github.com/TheoTurletti/Autossl.git

### Prerequisites 

The pre-reqs are:

1. Python3 (tested on python3.9)
2. You must have sslscan installed and in your path (default in Kali)
3. You need a valid Nmap XML output file (see below)
4. You need python-libnmap (see below)

### Installing python-libnmap

You can install libnmap via pip:
```bash
pip3 install python-libnmap
```


### Nmap XML File

The Nmap XML file must have been created with version scanning enabled i.e. via Nmap flags `-sV` or `-A` (see below) 

```bash
nmap -A -p 1-65535 -iL targets.txt -oX nmap-output.xml 
nmap -sS -sV -p 1-65535 -iL targets.txt -oX nmap-output.xml
```

## Usage

```bash
python3 ./autossl.py 

USAGE: autossl.py [nmap-ouput.xml] [output-file]
```

### Example
```bash
./auto-sslscan.py nmap-output.xml outfile.txt
auto-sslscan - v0.1 ( https://github.com/attackdebris/auto-sslscan )

Performing sslscan of 185.176.90.16:443
Performing sslscan of 199.101.100.186:31337

sslscan results saved to: outfile.txt
SSL services list saved to: ssl-services.txt
```

### Output / Results

The output from the script is a concatenated file (see below)

```bash
cat outfile.txt 

====================================================================
auto-sslscan - v0.1 ( https://github.com/attackdebris/auto-sslscan )
====================================================================

Version: 1.11.10-static
OpenSSL 1.0.2-chacha (1.0.2g-dev)

Testing SSL server 185.176.90.16 on port 443 using SNI name 

  TLS Fallback SCSV:
Server supports TLS Fallback SCSV

  TLS renegotiation:
Secure session renegotiation supported

  TLS Compression:
Compression disabled

  Heartbleed:
TLS 1.2 not vulnerable to heartbleed
TLS 1.1 not vulnerable to heartbleed
TLS 1.0 not vulnerable to heartbleed

  Supported Server Cipher(s):
Preferred TLSv1.2  256 bits  ECDHE-RSA-AES256-GCM-SHA384   Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve P-256 DHE 256
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve P-256 DHE 256
---snip---
```

### Credit

It is the python3 version of this repository : https://github.com/attackdebris/auto-sslscan 
