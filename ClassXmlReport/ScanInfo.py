class ScanInfo:
    JobID = None            # | int
    TestJob = None          # | int
    EndTime = None          # | datetime
    StartTime = None        # | datetime
    ScanType = ''           # | string
    ScanName = ''           # | string

    def __init__(self, *args, **kwargs):
        if args:
            len_of_args = len(args)
            if len_of_args >= 1:
                self.JobID = args[0]
            if len_of_args >= 2:
                self.TestJob = args[1]
            if len_of_args >= 3:
                self.EndTime = args[2]
            if len_of_args >= 4:
                self.StartTime = args[3]
            if len_of_args >= 5:
                self.ScanType = args[4]
            if len_of_args >= 6:
                self.ScanName = args[5]
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return "JobID: {}, " \
               "TestJob: {}, " \
               "EndTime: {}, " \
               "StartTime: {}, " \
               "ScanType: {}, " \
               "ScanName: {}".format(self.JobID, self.TestJob, self.EndTime, self.StartTime, self.ScanType, self.ScanName)