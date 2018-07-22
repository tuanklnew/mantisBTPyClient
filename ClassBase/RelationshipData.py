from .ObjectRef import ObjectRef


class RelationshipData:
    id = None               # int
    type = None             # ObjectRef
    target_id = None        # int

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.RelationshipData'>":
                self.id = args[0].id
                self.type = ObjectRef(args[0].type)
                self.target_id = args[0].target_id
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
        # Parse integer
        if self.id is not None:
            id = self.id
        else:
            id = None
        if self.target_id is not None:
            target_id = self.target_id
        else:
            target_id = None
        # Parse ObjectRef
        if self.type is not None:
            type_parsed = self.type.parse_to_zeep_type(factory)
        else:
            type_parsed = None
        # Parse RelationshipData and return
        return factory.RelationshipData(id=id, type=type_parsed, target_id=target_id)