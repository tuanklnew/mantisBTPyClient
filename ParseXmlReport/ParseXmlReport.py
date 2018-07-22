import xml.etree.ElementTree as EleTree
from ClassXmlReport import ScanInfo
from ClassXmlReport import HostInfo
from ClassXmlReport import VulFound


def parse_attrib(input_str):
    input_str = input_str.split(', ')
    ret_val = []
    for attrib in input_str:
        attrib = attrib.replace('\'', '')
        attrib = attrib.replace('{', '')
        attrib = attrib.replace('}', '')
        ret_val.append(attrib.split(': '))
    return ret_val


def parse_xml_host_data(file_location):
    xml = EleTree.parse(file_location)
    root = xml.getroot()
    ret_val = []
    # Parse Scan Info
    scan_info = ScanInfo()
    scan_info_raw = parse_attrib(str(root[1].attrib))
    for attrib in scan_info_raw:
        setattr(scan_info, attrib[0], attrib[1])

    # Parse Host info
    host_info_arr = []
    for host in root[2]:
        host_info = HostInfo()
        host_info_raw = parse_attrib(str(host.attrib))
        for attrib in host_info_raw:
            setattr(host_info, attrib[0], attrib[1])
        host_info_arr.append(host_info)

        # Parse Host Vuln
        for vuln in host[1]:
            vul_found = VulFound()
            vuln_raw = parse_attrib(str(vuln.attrib))
            for attrib in vuln_raw:
                setattr(vul_found, attrib[0], attrib[1])
            for field in vuln:
                setattr(vul_found, field.tag, field.text)
            vul_found.host_info = host_info
            vul_found.scan_info = scan_info
            ret_val.append(vul_found)
    return ret_val
