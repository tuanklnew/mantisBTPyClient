from ClassBase import FilterCustomField


class FilterSearchData:
    project_id = []             # array of int
    search = ''                 # string
    category = []               # array of string
    severity_id = []            # array of int
    status_id = []              # array of int
    priority_id = []            # array of int
    reporter_id = []            # array of int
    handler_id = []             # array of int
    note_user_id =[]            # array of int
    resolution_id = []          # array of int
    product_version = ''        # string
    user_monitor_id = []        # array of int
    hide_status_id = []         # array of int
    sort = ''                   # string
    sort_direction = ''         # string
    sticky = None               # bool
    view_state_id = []          # array of int
    fixed_in_version = []       # array of string
    target_version = []         # array of string
    platform = []               # array of string
    os = []                     # array of string
    os_build = []               # array of string
    start_day = None            # int
    start_month = None          # int
    start_year = None           # int
    end_day = None              # int
    end_month = None            # int
    end_year = None             # int
    tag_string = []             # array of string
    tag_select = []             # array of int
    custom_fields = []          # array of FilterCustomField

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0]))== "<class 'zeep.objects.FilterSearchData'>":
                self.project_id = args[0].project_id
                self.search = args[0].search
                self.category = args[0].category
                self.severity_id = args[0].severity_id
                self.status_id = args[0].status_id
                self.priority_id = args[0].priority_id
                self.reporter_id = args[0].reporter_id
                self.handler_id = args[0].handler_id
                self.note_user_id = args[0].note_user_id
                self.resolution_id = args[0].resolution_id
                self.product_version = args[0].product_version
                self.user_monitor_id = args[0].user_monitor_id
                self.hide_status_id = args[0].hide_status_id
                self.sort = args[0].sort
                self.sort_direction = args[0].sort_direction
                self.sticky = args[0].sticky
                self.view_state_id = args[0].view_state_id
                self.fixed_in_version = args[0].fixed_in_version
                self.target_version = args[0].target_version
                self.platform = args[0].platform
                self.os = args[0].os
                self.os_build = args[0].os_build
                self.start_day = args[0].start_day
                self.start_month = args[0].start_month
                self.start_year = args[0].start_year
                self.end_day = args[0].end_day
                self.end_month = args[0].end_month
                self.end_year = args[0].end_year
                self.tag_string = args[0].tag_string
                self.tag_select = args[0].tag_select
                for custom_field in args[0].custom_fields:
                    self.custom_fields.append(FilterCustomField(custom_field))
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if str(type(self.__getattribute__(attribute)))=="<class 'list'>" and self.__getattribute__(attribute) and type((self.__getattribute__(attribute))[0]) is FilterCustomField:
                list = []
                for Filter_cust_field in self.__getattribute__(attribute):
                    list.append(Filter_cust_field.parse_to_dict())
                ret_val.update({str(attribute): list})
            else:
                ret_val.update({str(attribute):self.__getattribute__(attribute)})
        return ret_val

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_zeep_type(self, factory):
        # Parse integer Array
        if self.project_id:
            project_id = self.project_id
        else:
            project_id = None
        if self.severity_id:
            severity_id = self.severity_id
        else:
            severity_id = None
        if self.status_id:
            status_id = self.status_id
        else:
            status_id = None
        if self.priority_id:
            priority_id = self.priority_id
        else:
            priority_id = None
        if self.resolution_id:
            reporter_id = self.reporter_id
        else:
            reporter_id = None
        if self.handler_id:
            handler_id = self.handler_id
        else:
            handler_id = None
        if self.note_user_id:
            note_user_id = self.note_user_id
        else:
            note_user_id = None
        if self.resolution_id:
            resolution_id = self.resolution_id
        else:
            resolution_id = None
        if self.user_monitor_id:
            user_monitor_id = self.user_monitor_id
        else:
            user_monitor_id = None
        if self.hide_status_id:
            hide_status_id = self.hide_status_id
        else:
            hide_status_id = None
        if self.view_state_id:
            view_state_id = self.view_state_id
        else:
            view_state_id = None
        if self.tag_select:
            tag_select = self.tag_select
        else:
            tag_select = None

        # Parse string
        if self.search != '':
            search = self.search
        else:
            search = None
        if self.product_version != '':
            product_version = self.product_version
        else:
            product_version = None
        if self.sort != '':
            sort = self.sort
        else:
            sort = None
        if self.sort_direction != '':
            sort_direction = self.sort_direction
        else:
            sort_direction = None

        # Parse string array
        if self.category:
            category = self.category
        else:
            category = None
        if self.fixed_in_version:
            fixed_in_version = self.fixed_in_version
        else:
            fixed_in_version = None
        if self.target_version:
            target_version = self.target_version
        else:
            target_version = None
        if self.platform:
            platform = self.platform
        else:
            platform = None
        if self.os:
            os = self.os
        else:
            os = None
        if self.os_build:
            os_build = self.os_build
        else:
            os_build = None
        if self.tag_string:
            tag_string = self.tag_string
        else:
            tag_string = None

        # Parse int
        if self.start_day is not None:
            start_day = self.start_day
        else:
            start_day = None
        if self.start_month is not None:
            start_month = self.start_month
        else:
            start_month = None
        if self.start_year is not None:
            start_year = self.start_year
        else:
            start_year = None
        if self.end_day is not None:
            end_day = self.end_day
        else:
            end_day = None
        if self.end_month is not None:
            end_month = self.end_month
        else:
            end_month = None
        if self.end_year is not None:
            end_year = self.end_year
        else:
            end_year = None

        # Parse boolean
        sticky = self.sticky

        # Parse filter custom fields array
        custom_fields_preparse = []
        for custom_field_preparse in self.custom_fields:
            custom_fields_preparse.append(custom_field_preparse.parse_to_zeep_type(factory))
        if custom_fields_preparse:
            custom_fields = factory.FilterCustomFieldArray(custom_fields_preparse)
        else:
            custom_fields = None

        # return parsed filter search data
        return factory.FilterSearchData(
            project_id=project_id,
            search=search,
            category=category,
            severity_id=severity_id,
            status_id=status_id,
            priority_id=priority_id,
            reporter_id=reporter_id,
            handler_id=handler_id,
            note_user_id=note_user_id,
            resolution_id=resolution_id,
            product_version=product_version,
            user_monitor_id=user_monitor_id,
            hide_status_id=hide_status_id,
            sort=sort,
            sort_direction=sort_direction,
            sticky=sticky,
            view_state_id=view_state_id,
            fixed_in_version=fixed_in_version,
            target_version=target_version,
            platform=platform,
            os=os,
            os_build=os_build,
            start_day=start_day,
            start_month=start_month,
            start_year=start_year,
            end_day=end_day,
            end_month=end_month,
            end_year=end_year,
            tag_string=tag_string,
            tag_select=tag_select,
            custom_fields=custom_fields
        )
