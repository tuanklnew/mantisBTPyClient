from .AccountData import AccountData
from .ObjectRef import ObjectRef


class IssueNoteData:
    id = None                           # int
    reporter = None                     # AccountData
    text = ''                           # String
    view_state = None                   # ObjectRef
    date_submitted = None               # datetime
    last_modified = None                # datetime
    time_tracking = None                # int
    note_type = None                    # int
    note_attr = ''                      # String

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0]))=="<class 'zeep.objects.IssueNoteData'>":
                self.id = args[0].id
                self.reporter = AccountData(args[0].reporter)
                self.text = args[0].text
                self.view_state = ObjectRef(args[0].view_state)
                self.date_submitted = args[0].date_submitted
                self.last_modified = args[0].last_modified
                self.time_tracking = args[0].time_tracking
                self.note_type = args[0].note_type
                self.note_attr = args[0].note_attr
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if type(self.__getattribute__(attribute)) in [ObjectRef, AccountData]:
                ret_val.update({str(attribute): self.__getattribute__(attribute).parse_to_dict()})
            else:
                ret_val.update({str(attribute):self.__getattribute__(attribute)})
        return ret_val

    def parse_to_zeep_type(self, factory):

        # Parse integer
        if self.id is not None:
            id = self.id
        else:
            id = None
        if self.time_tracking is not None:
            time_tracking = self.time_tracking
        else:
            time_tracking = None
        if self.note_type is not None:
            note_type = self.note_type
        else:
            note_type = None

        # Parse string
        if self.text != '':
            text = self.text
        else:
            text = None
        if self.note_attr != '':
            note_attr = self.note_attr
        else:
            note_attr = None

        # It is not necessary to Parse datetime
        if self.date_submitted is not None:
            date_submitted = self.date_submitted
        else:
            date_submitted = None
        if self.last_modified is not None:
            last_modified = self.last_modified
        else:
            date_submitted = None

        # Parse AccountData
        if self.reporter is not None:
            reporter = self.reporter.parse_to_zeep_type(factory)
        else:
            reporter = None

        # Parse ObjectRef
        if self.view_state is not None:
            view_state = self.view_state.parse_to_zeep_type(factory)
        else:
            view_state = None
        # Parse IssueNoteData and return
        return factory.IssueNoteData(id=id, reporter=reporter, text=text, view_state=view_state, date_submitted=date_submitted, last_modified=last_modified, time_tracking=time_tracking, note_type=note_type, note_attr=note_attr)