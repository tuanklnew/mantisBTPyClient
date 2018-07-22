from ClassXmlReport.HostInfo import HostInfo
from ClassXmlReport.ScanInfo import ScanInfo


class VulFound:
    scan_info = ScanInfo()                  # ScanInfo
    host_info = HostInfo()                  # HostInfo
    VulnName = ''                           # string
    id = None                               # int
    Risk = None                             # int
    ServiceName = ''                        # string
    Port = None                             # int
    Protocol = ''                           # string
    Description = ''                        # string
    CVE = ''                                # string

    def __init__(self, *args, **kwargs):
        if args:
            len_of_args = len(args)
            if len_of_args >= 1:
                self.scan_info = args[0]
            if len_of_args >= 2:
                self.host_info = args[1]
            if len_of_args >= 3:
                self.VulnName = args[2]
            if len_of_args >= 4:
                self.id = args[3]
            if len_of_args >= 5:
                self.Risk = args[4]
            if len_of_args >= 6:
                self.ServiceName = args[5]
            if len_of_args >= 7:
                self.Port = args[6]
            if len_of_args >= 8:
                self.Protocol = args[7]
            if len_of_args >= 9:
                self.Description = args[8]
            if len_of_args >= 10:
                self.CVE = args[9]
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return "scan_info: {},\n" \
               "host_info: {},\n" \
               "VulnName: {},\n" \
               "id: {},\n" \
               "Risk: {},\n" \
               "ServiceName: {},\n" \
               "Port: {},\n" \
               "Protocol: {},\n" \
               "Description: {},\n" \
               "CVE: {},".format(self.scan_info, self.host_info, self.VulnName, self.id, self.Risk, self.ServiceName, self.Port, self.Protocol, self.Description, self.CVE)

