import os


def get_ip_address(domain):
    command = "host " + str(domain)


    process = os.popen(command)

    result = str(process.read())
    marker = result.find("has address") + 12
    return result[marker:].splitlines()[0]