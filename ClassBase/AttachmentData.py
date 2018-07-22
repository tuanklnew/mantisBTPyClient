from datetime import datetime


class AttachmentData:
    id = None                               # int
    filename = ''                           # String
    size  = None                            # int
    content_type = ''                       # String
    date_submitted = None                   # datetime
    download_url = ''                       # String
    user_id = None                          # int

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.AttachmentData'>":
                self.id = args[0].id
                self.filename = args[0].filename
                self.size = args[0].size
                self.content_type = args[0].content_type
                self.date_submitted = args[0].date_submitted
                self.download_url = args[0].download_url
                self.user_id = args[0].user_id
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            ret_val.update({str(attribute): self.__getattribute__(attribute)})
        return ret_val

    def parse_to_zeep_type(self, factory):

        # Parse integer
        if self.id is not None:
            id = self.id
        else:
            id = None
        if self.size is not None:
            size = self.size
        else:
            size = None
        if self.user_id is not None:
            user_id = self.user_id
        else:
            user_id = None

        # Parse string
        if self.filename != '':
            filename = self.filename
        else:
            filename = None
        if self.content_type != '':
            content_type = self.content_type
        else:
            content_type = None
        if self.download_url != '':
            download_url = self.download_url
        else:
            download_url = None

        # It is not necessary to Parse datetime
        if self.date_submitted is not None:
            date_submitted = self.date_submitted
        else:
            date_submitted = datetime.today()

        # Parse AttachmentData and return
        return factory.AttachmentData(id=id, filename=filename, size=size, content_type=content_type, date_submitted=date_submitted, download_url=download_url, user_id=user_id)