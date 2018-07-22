from ClassBase import ObjectRef

class CustomFieldDefinitionData:
    field=ObjectRef()           # ObjectRef
    type = None                 # int
    possible_values = ''        # string
    default_value =''           # string
    valid_regexp  = ''          # string
    access_level_r = None       # int
    access_level_rw = None      # int
    length_min = None           # int
    length_max = None           # int
    advanced = False            # bool
    display_report = False      # bool
    display_update = False      # bool
    display_resolved = False    # bool
    display_closed = False      # bool
    require_report = False      # bool
    require_update = False      # bool
    require_resolved = False    # bool
    require_closed = False      # bool

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.CustomFieldDefinitionData'>":
                self.field = ObjectRef(args[0].field)
                self.type = args[0].type
                self.possible_values = args[0].possible_values
                self.default_value = args[0].default_value
                self.valid_regexp = args[0].valid_regexp
                self.access_level_r = args[0].access_level_r
                self.access_level_rw = args[0].access_level_rw
                self.length_min = args[0].length_min
                self.length_max = args[0].length_max
                self.advanced = args[0].advanced
                self.display_report = args[0].display_report
                self.display_update = args[0].display_update
                self.display_resolved = args[0].display_resolved
                self.display_closed = args[0].display_closed
                self.require_report = args[0].require_report
                self.require_update = args[0].require_update
                self.require_resolved = args[0].require_resolved
                self.require_closed = args[0].require_closed
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
        return self.parse_to_dict()