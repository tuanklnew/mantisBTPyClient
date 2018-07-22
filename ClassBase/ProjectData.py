from .ObjectRef import ObjectRef


class ProjectData:
    id = None
    name = ''
    status = ObjectRef()
    enabled = None
    view_state = ObjectRef()
    access_min = ObjectRef()
    file_path = ''
    description = ''
    subprojects = []    #ProjectData
    inherit_global = None

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0]))=="<class 'zeep.objects.ProjectData'>":
                self.id = args[0].id
                self.name = args[0].name
                self.status = ObjectRef(args[0].status)
                self.enabled = args[0].enabled
                self.view_state = ObjectRef(args[0].view_state)
                self.access_min = ObjectRef(args[0].access_min)
                self.file_path = args[0].file_path
                self.description = args[0].subprojects
                for subproject in args[0].subprojects:
                    self.subprojects.append(ProjectData(subproject))
                self.inherit_global = args[0].inherit_global
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if type(self.__getattribute__(attribute)) is ObjectRef:
                temp_dict = self.__getattribute__(attribute).parse_to_dict()
                ret_val.update({str(attribute): temp_dict})
            elif attribute != 'subprojects':
                ret_val.update({str(attribute):self.__getattribute__(attribute)})
            else:
                subproject_list = []
                for subproject in self.subprojects:
                    temp_dict = subproject.parparse_to_dict()
                    subproject_list.append(temp_dict)
                ret_val.update({str(attribute):subproject_list})
        return ret_val



