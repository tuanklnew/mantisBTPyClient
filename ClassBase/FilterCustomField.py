from ClassBase import ObjectRef

class FilterCustomField:
    field = None                    # ObjectRef
    value = []                      # array of string

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.FilterCustomField'>":
                self.field = ObjectRef(args[0].field)
                self.value = args[0].value
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if type(self.__getattribute__(attribute)) is ObjectRef:
                temp_dict = self.__getattribute__(attribute).parse_to_dict()
                ret_val.update({str(attribute): temp_dict})
            else:
                ret_val.update({str(attribute):self.__getattribute__(attribute)})
        return ret_val

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_zeep_type(self, factory):

        # Parse ObjectRef
        if self.field is not None:
            field = self.field.parse_to_zeep_type(factory)
        else:
            field = None

        # Parse array of String
        if self.value:
            value = self.value
        else:
            value = None

        # Parse FilterCustomField and return
        return factory.FilterCustomField(field=field, value=value)