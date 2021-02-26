# THM_scanner ideas to implement
Description
<br/><br/>

## Config file
---
- Make config file optional by using argument "--config [path]"
- Define config values by "tool"
- Use the ["best practice"](https://hackersandslackers.com/simplify-your-python-projects-configuration/) format
<br/><br/>

## Scanning ideas
---
<br/>

### Nmap scanning
- Using [python3-nmap](https://pypi.org/project/python3-nmap/) 
    - Full scan
    - ~~Make OS scan optional~~
        - ~~Make alert that user needs to run script as root~~
            - ~~Check root~~
    - ~~Make -sV (service version) by default~~
    - Make a "quick scan" option (-T5 -F)
    - ~~Make subnet scan optional~~
    - ~~Make no ping optional (-Pn)~~
<br/>

### Dir searching
- Using [pyfuzz](https://github.com/AyoobAli/pyfuzz)
- Pass file extensions as argument in config file
- Pass wordlist as argument in config
- Implement "string to ignore" (-i)

### Vuln scanners
- Rely on common linux tools?
- Offer options to skip this if windows?
- Ideally find Python options




