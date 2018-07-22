class AccountData:
    id = None           # int
    name = ''           # String
    real_name = ''      # String
    email = ''          # String

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0])) == "<class 'zeep.objects.AccountData'>":
                self.id = args[0].id
                self.name = args[0].name
                self.real_name = args[0].real_name
                self.email = args[0].email
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

        # Parse string
        if self.name != '':
            name = self.name
        else:
            name = None
        if self.real_name != '':
            real_name = self.real_name
        else:
            real_name = None
        if self.email != '':
            email = self.email
        else:
            email = None

        # Parse account_data and return
        return factory.AccountData(id=id, name=name, real_name=real_name, email=email)
