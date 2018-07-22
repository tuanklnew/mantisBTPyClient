import ClassBase
import APIFunction
import base64
from zeep import exceptions


# This function add new issue to Mantis BT
def mc_issue_add(zeep_client, username='administrator', password='password', issue=ClassBase.IssueData()):
    ret_val = zeep_client.service.mc_issue_add(username, password, issue)
    return ret_val


def mc_issue_get(zeep_client, username, password, issue_id):
    return zeep_client.service.mc_issue_get(username=username, password=password, issue_id=issue_id)

# This is customized function for Eximbank's usages.
# They have 5 custom fields: Times of Scan, Name of Scan, Ip Address, Scan ID, and Date of Scan.
# When add new issues Count value increases when Scan ID is not in Scan IDs.
# This function return [issue_id, [att_names]] if it is successful
# return [-1] if issue already existed
# return [-2] if it has problems with custom fields
# return [-2] if it has problems with login

def add_issue(zeep_client,              # zeep client
              factory,                  # factory data structure
              username,                 # string
              password,                 # string
              ip_addr,                  # string
              name_of_scan,             # string
              date_of_scan,             # string
              view_state,               # ObjectRef Const
              last_updated,             # datetime
              project,                  # ObjectRef
              priority,                 # ObjectRef Const
              severity,                 # ObjectRef Const
              status,                   # ObjectRef Const
              summary,                  # string
              platform,                 # string
              os,                       # string
              os_build,                 # string
              reproducibility,          # ObjectRef Const
              date_submitted,           # datetime
              resolution,               # ObjectRef Const
              description,              # string
              steps_to_reproduce,       # string
              additional_information,   # string
              due_date,                 # datetime
              category='General',       # string
              attachments=[],           # AttachmentData Array
              sticky=False,             # bool
            ):
    # get account info
    try:
        acc_info = ClassBase.AccountData(APIFunction.mc_login(zeep_client, username=username, password=password).account_data)
    except exceptions.Fault:
        return [-3, []]
    # get custom fields definition
    custom_fields_data_arr = APIFunction.mc_project_get_custom_fields(zeep_client, username=username, password=password, project_name=project.name)

    # create id_scan
    id_scan = base64.b64encode((name_of_scan + "," + date_of_scan).encode()).decode()

    # get id and name of ip address and count custom fields
    obj_ip_add_cust_field = None
    obj_id_scan_cust_field = None
    obj_date_of_scan_cust_field = None
    obj_times_of_scan_cust_field = None
    obj_name_of_scan_cust_field = None
    for custom_fields_data in custom_fields_data_arr:
        if str.lower(custom_fields_data.field.name) == 'ip address':
            obj_ip_add_cust_field = ClassBase.ObjectRef(custom_fields_data.field)
        elif str.lower(custom_fields_data.field.name) == 'id scan':
            obj_id_scan_cust_field = ClassBase.ObjectRef(custom_fields_data.field)
        elif str.lower(custom_fields_data.field.name) == 'date of scan':
            obj_date_of_scan_cust_field = ClassBase.ObjectRef(custom_fields_data.field)
        elif str.lower(custom_fields_data.field.name) == 'times of scan':
            obj_times_of_scan_cust_field = ClassBase.ObjectRef(custom_fields_data.field)
        elif str.lower(custom_fields_data.field.name) == 'name of scan':
            obj_name_of_scan_cust_field = ClassBase.ObjectRef(custom_fields_data.field)

    # Return -2 if there is incorrect custom fields definition
    if not obj_ip_add_cust_field or not obj_id_scan_cust_field or not obj_date_of_scan_cust_field:
        return [-2, []]

    # create array filter custom fields for searching issue that match ip address
    ip_addr_search_filter_custom_fields = []
    ip_addr_search_filter_custom_fields.append(ClassBase.FilterCustomField(field=obj_ip_add_cust_field, value=[ip_addr]))
    filter_search_data = ClassBase.FilterSearchData(project_id=[project.id], custom_fields=ip_addr_search_filter_custom_fields)
    issues = APIFunction.mc_filter_search_issues(zeep_client=zeep_client, filter=filter_search_data.parse_to_zeep_type(factory), username=username, password=password, page_number=-1, per_page=-1)

    # Caculate times_of_scan
    times_of_scan = 0
    if issues:
        for issue in issues:
            search_id_scan = None
            search_times_of_scan = None
            for cust_field in issue.custom_fields:
                if str(cust_field.field.name).lower() == 'id scan':
                    search_id_scan = cust_field.value
                if str(cust_field.field.name).lower() == 'times of scan':
                    search_times_of_scan = cust_field.value
            if search_id_scan == id_scan:
                times_of_scan = int(search_times_of_scan)
                break
            elif int(search_times_of_scan) > int(times_of_scan):
                times_of_scan = int(search_times_of_scan) + 1
    else:
        times_of_scan = 1

    new_issue_cust_fields = []
    new_issue_cust_fields.append(ClassBase.CustomFieldValueForIssueData(field=obj_ip_add_cust_field, value=ip_addr))
    new_issue_cust_fields.append(ClassBase.CustomFieldValueForIssueData(field=obj_id_scan_cust_field, value=id_scan))
    new_issue_cust_fields.append(ClassBase.CustomFieldValueForIssueData(field=obj_date_of_scan_cust_field, value=date_of_scan))
    new_issue_cust_fields.append(ClassBase.CustomFieldValueForIssueData(field=obj_times_of_scan_cust_field, value=times_of_scan))
    new_issue_cust_fields.append(ClassBase.CustomFieldValueForIssueData(field=obj_name_of_scan_cust_field, value=name_of_scan))

    new_issue = ClassBase.IssueData(view_state=view_state,
                                    last_updated=last_updated,
                                    project=project,
                                    category=category,
                                    priority=priority,
                                    severity=severity,
                                    status=status,
                                    reporter=acc_info,
                                    summary=summary,
                                    platform=platform,
                                    os=os,
                                    os_build=os_build,
                                    reproducibility=reproducibility,
                                    date_submitted=date_submitted,
                                    resolution=resolution,
                                    description=description,
                                    steps_to_reproduce=steps_to_reproduce,
                                    additional_information=additional_information,
                                    custom_fields=new_issue_cust_fields,
                                    due_date=due_date,
                                    sticky=sticky
                                    )

    new_issue_id = mc_issue_add(zeep_client, username=username, password=password, issue=new_issue.parse_to_zeep_type(factory))

    # upload attachments
    ret_att = []
    for attachment in attachments:
        try:
            file_att = open(attachment, 'rb')
        except:
            ret_att.append([attachment, -1])
        else:
            ret_att.append([attachment, 1])
            APIFunction.mc_issue_attachment_add(zeep_client,
                                                username,
                                                password,
                                                new_issue_id,
                                                file_att)
    return [new_issue_id, ret_att]
