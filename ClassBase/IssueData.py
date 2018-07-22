from .ObjectRef import ObjectRef
from .AccountData import AccountData
from .AttachmentData import AttachmentData
from .RelationshipData import RelationshipData
from .IssueNoteData import IssueNoteData
from .CustomFieldValueForIssueData import CustomFieldValueForIssueData


class IssueData:
    id = None                           # int
    view_state = None                   # ObjectRef
    last_updated = None                 # datetime
    project = None                      # ObjectRef
    category = ''                       # String
    priority = None                     # ObjectRef
    severity = None                     # ObjectRef
    status = None                       # ObjectRef
    reporter = None                     # AccountData
    summary = ''                        # String
    version = ''                        # String
    build = ''                          # String
    platform = ''                       # String
    os = ''                             # String
    os_build = ''                       # String
    reproducibility = None              # ObjectRef
    date_submitted = None               # datetime
    sponsorship_total = None            # int
    handler = None                      # AccountData
    projection = None                   # ObjectRef
    eta = None                          # ObjectRef
    resolution = None                   # ObjectRef
    fixed_in_version = ''               # String
    target_version = ''                 # String
    description = ''                    # String
    steps_to_reproduce = ''             # String
    additional_information = ''         # String
    attachments = []                    # Array of AttachmentData
    relationships = []                  # Array of RelationshipData
    notes = []                          # Array of IssueNoteData
    custom_fields = []                  # Array of CustomFieldValueForIssueData
    due_date = None                     # datetime
    monitors = []                       # Array of AccountData
    sticky = False                      # bool
    tags = []                           # Array of ObjectRef

    def __init__(self, *args, **kwargs):
        if args:
            if str(type(args[0]))=="<class 'zeep.objects.IssueData'>":
                self.id = args[0].id
                self.view_state = ObjectRef(args[0].view_state)
                self.last_updated = args[0].last_updated
                self.project = ObjectRef(args[0].project)
                self.category = args[0].category
                self.priority = ObjectRef(args[0].priority)
                self.severity = ObjectRef(args[0].severity)
                self.status = ObjectRef(args[0].status)
                self.reporter = AccountData(args[0].reporter)
                self.summary = args[0].summary
                self.version = args[0].version
                self.build = args[0].build
                self.platform = args[0].platform
                self.os = args[0].os
                self.os_build = args[0].os_build
                self.reproducibility = ObjectRef(args[0].reproducibility)
                self.date_submitted = args[0].date_submitted
                self.sponsorship_total = args[0].sponsorship_total
                self.handler = AccountData(args[0].handler)
                self.projection = ObjectRef(args[0].projection)
                self.eta = ObjectRef(args[0].eta)
                self.resolution = ObjectRef(args[0].resolution)
                self.fixed_in_version = args[0].fixed_in_version
                self.target_version = args[0].target_version
                self.description = args[0].description
                self.steps_to_reproduce = args[0].steps_to_reproduce
                self.additional_information = args[0].additional_information
                for attachment in args[0].attachments:
                    self.attachments.append(AttachmentData(attachment))
                if str(type(args[0].relationships))!="<class 'NoneType'>":
                    for relationship in args[0].relationships:
                        self.relationships.append(RelationshipData(relationship))
                if str(type(args[0].notes))!="<class 'NoneType'>":
                    for note in args[0].notes:
                        self.notes.append(IssueNoteData(note))
                for custom_field in args[0].custom_fields:
                    self.custom_fields.append(CustomFieldValueForIssueData(custom_field))
                self.due_date = args[0].due_date
                for monitor in args[0].monitors:
                    self.monitors.append(AccountData(monitor))
                self.sticky = args[0].sticky
                for tag in args[0].tags:
                    self.tags.append(ObjectRef(tag))
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_to_dict(self):
        ret_val = dict()
        for attribute in self.__dict__.keys():
            if type(self.__getattribute__(attribute)) is list:
                att_list = []
                for element in self.__getattribute__(attribute):
                    att_list.append(element.parse_to_dict())
                ret_val.update({str(attribute):att_list})
            elif type(self.__getattribute__(attribute)) in [ObjectRef, AccountData]:
                ret_val.update({str(attribute): self.__getattribute__(attribute).parse_to_dict()})
            else:
                ret_val.update({str(attribute): self.__getattribute__(attribute)})
        return ret_val

    def __str__(self):
        return str(self.parse_to_dict())

    def parse_to_zeep_type(self, factory):

        # Parse integer
        if self.id is not None:
            id = self.id
        else:
            id = None
        if self.sponsorship_total is not None:
            sponsorship_total = self.sponsorship_total
        else:
            sponsorship_total = None

        # Parse ObjectRef
        if self.view_state is not None:
            view_state = self.view_state.parse_to_zeep_type(factory)
        else:
            view_state = None
        if self.project is not None:
            project = self.project.parse_to_zeep_type(factory)
        else:
            project = None
        if self.priority is not None:
            priority = self.priority.parse_to_zeep_type(factory)
        else:
            priority = None
        if self.severity is not None:
            severity = self.severity.parse_to_zeep_type(factory)
        else:
            severity = None
        if self.status is not None:
            status = self.status.parse_to_zeep_type(factory)
        else:
            status = None
        if self.reproducibility is not None:
            reproducibility = self.reproducibility.parse_to_zeep_type(factory)
        else:
            reproducibility = None
        if self.projection is not None:
            projection = self.projection.parse_to_zeep_type(factory)
        else:
            projection = None
        if self.eta is not None:
            eta = self.eta.parse_to_zeep_type(factory)
        else:
            eta = None
        if self.resolution is not None:
            resolution = self.resolution.parse_to_zeep_type(factory)
        else:
            resolution = None

        # It is not necessary to Parse datetime
        if self.last_updated is not None:
            last_updated = self.last_updated
        else:
            last_updated = None
        if self.date_submitted is not None:
            date_submitted = self.date_submitted
        else:
            date_submitted = None
        if self.due_date is not None:
            due_date = self.due_date
        else:
            due_date =None

        # Parse String
        if self.category != '':
            category = self.category
        else:
            category = None
        if self.summary != '':
            summary = self.summary
        else:
            summary = None
        if self.version != '':
            version = self.version
        else:
            version = None
        if self.build != '':
            build = self.build
        else:
            build = None
        if self.platform != '':
            platform = self.platform
        else:
            platform = None
        if self.os != '':
            os = self.os
        else:
            os = None
        if self.os_build != '':
            os_build = self.os_build
        else:
            os_build = None
        if self.fixed_in_version != '':
            fixed_in_version = self.fixed_in_version
        else:
            fixed_in_version = None
        if self.target_version != '':
            target_version = self.target_version
        else:
            target_version = None
        if self.description != '':
            description = self.description
        else:
            description = None
        if self.steps_to_reproduce != '':
            steps_to_reproduce = self.steps_to_reproduce
        else:
            steps_to_reproduce = None
        if self.additional_information != '':
            additional_information = self.additional_information
        else:
            additional_information = None

        # Parse AccountData
        if self.reporter is not None:
            reporter = self.reporter.parse_to_zeep_type(factory)
        else:
            reporter = None
        if self.handler is not None:
            handler = self.handler.parse_to_zeep_type(factory)
        else:
            handler = None

        # Parse Array of AttachmentData
        if self.attachments:
            attachments_preparse = []
            for attachment in self.attachments:
                attachments_preparse.append(attachment.parse_to_zeep_type(factory))
            attachments = factory.AttachmentDataArray(attachments_preparse)
        else:
            attachments = None

        # Parse Array of RelationshipData
        if self.relationships:
            relationships_preparse = []
            for relationship in self.relationships:
                relationships_preparse.append(relationship.parse_to_zeep_type(factory))
            relationships = factory.RelationshipDataArray(relationships_preparse)
        else:
            relationships = None

        # Parse Array of IssueNoteData
        if self.notes:
            notes_preparse = []
            for note in self.notes:
                notes_preparse.append(note.parse_to_zeep_type(factory))
            notes = factory.IssueNoteDataArray(notes_preparse)
        else:
            notes = None

        # Parse Array of CustomFieldValueForIssueData
        if self.custom_fields:
            custom_fields_preparse = []
            for custom_field in self.custom_fields:
                custom_fields_preparse.append(custom_field.parse_to_zeep_type(factory))
            custom_fields = factory.CustomFieldValueForIssueDataArray(custom_fields_preparse)
        else:
            custom_fields = None

        # Parse Array of AccountData
        if self.monitors:
            monitors_preparse = []
            for monitor in self.monitors:
                monitors_preparse.append(monitor.parse_to_zeep_type(factory))
            monitors = factory.AccountDataArray(monitors_preparse)
        else:
            monitors = None

        # Parse Boolean
        if self.sticky is not None:
            sticky = self.sticky
        else:
            sticky = False

        # Parse Array of ObjectRef
        if self.tags:
            tags_preparse = []
            for tag in self.tags:
                tags_preparse.append(tag.parse_to_zeep_type(factory))
            tags = factory.ObjectRefArray(tags_preparse)
        else:
            tags = None

        # Parse IssueData and return
        return factory.IssueData(id=id,
                                 view_state=view_state,
                                 last_updated=last_updated,
                                 project=project,
                                 category=category,
                                 priority=priority,
                                 severity=severity,
                                 status=status,
                                 reporter=reporter,
                                 summary=summary,
                                 version=version,
                                 build=build,
                                 platform=platform,
                                 os=os,
                                 os_build=os_build,
                                 reproducibility=reproducibility,
                                 date_submitted=date_submitted,
                                 sponsorship_total=sponsorship_total,
                                 handler=handler,
                                 projection=projection,
                                 eta=eta,
                                 resolution=resolution,
                                 fixed_in_version=fixed_in_version,
                                 target_version=target_version,
                                 description=description,
                                 steps_to_reproduce=steps_to_reproduce,
                                 additional_information=additional_information,
                                 attachments=attachments,
                                 relationships=relationships,
                                 notes=notes,
                                 custom_fields=custom_fields,
                                 due_date=due_date,
                                 monitors=monitors,
                                 sticky=sticky,
                                 tags=tags
                                 )
