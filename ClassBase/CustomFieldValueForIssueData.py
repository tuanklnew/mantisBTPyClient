from .ObjectRef import ObjectRef


class CustomFieldValueForIssueData:
    field = None     # ObjectRef
    value = ''       # String

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.CustomFieldValueForIssueData'>":
                self.field = ObjectRef(args[0].field)
                self.value = args[0].value
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if type(self.__getattribute__(attribute)) is ObjectRef:
                ret_val.update({str(attribute): self.__getattribute__(attribute).parse_to_dict()})
            else:
                ret_val.update({str(attribute): self.__getattribute__(attribute)})
        return ret_val

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_zeep_type(self, factory):
        # Parse string
        if self.value != '':
            value = self.value
        else:
            value = None

        # Parse ObjectRef
        if self.field is not None:
            field = self.field.parse_to_zeep_type(factory)
        else:
            field = None

        # Parse CustomFieldValueForIssueData and return
        return factory.CustomFieldValueForIssueData(field=field, value=value)