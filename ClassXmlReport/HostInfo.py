class HostInfo:
    AssetLabel = ''             # string
    IPDword = ''                # string
    IPAddress = ''              # string
    OSName = ''                 # string
    DNSName = ''                # string
    NBName = ''                 # string
    NBWorkGroupName = ''        # string

    def __init__(self, *args, **kwargs):
        if args:
            len_of_args = len(args)
            if len_of_args >= 1:
                self.AssetLabel = args[0]
            if len_of_args >= 2:
                self.IPDword = args[1]
            if len_of_args >= 3:
                self.IPAddress = args[2]
            if len_of_args >= 4:
                self.OSName = args[3]
            if len_of_args >= 5:
                self.DNSName = args[4]
            if len_of_args >= 6:
                self.NBName = args[5]
            if len_of_args >= 7:
                self.NBWorkGroupName = args[5]
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return "AssetLabel: {}, " \
               "IPDword: {}, " \
               "IPAddress: {}, " \
               "OSName: {}, " \
               "DNSName: {}, " \
               "NBName: {}, " \
               "NBWorkGroupName: {}".format(self.AssetLabel, self.IPDword, self.IPAddress, self.OSName, self.DNSName, self.NBName, self.NBWorkGroupName)
