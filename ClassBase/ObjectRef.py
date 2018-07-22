class ObjectRef:
    id = None
    name = ''

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0]))=="<class 'zeep.objects.ObjectRef'>":
                self.id = args[0].id
                self.name = args[0].name
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
        # Parse integer Array
        if self.id is not None:
            id = self.id
        else:
            id = None
        # Parse string
        if self.name != '':
            name = self.name
        else:
            name = None

        return factory.ObjectRef(id=id, name=name)
