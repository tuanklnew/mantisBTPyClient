# This function add new project
def mc_project_add(zeep_client, project_data, username='administrator', password='password'):
    project_dict = project_data.parse_to_dict()
    ret_val = zeep_client.service.mc_project_add(username, password, project_dict)
    return ret_val


# This function get project id from name of project
def mc_project_get_id_from_name(zeep_client, username='administrator', password='password', project_name=''):
    return zeep_client.service.mc_project_get_id_from_name(username, password, project_name)


# This function delete project in Mantis BT
def mc_project_delete(zeep_client, username='administrator', password='password', project_name=''):
    project_id = zeep_client.service.mc_project_get_id_from_name(username, password, project_name)
    ret_val = zeep_client.service.mc_project_delete(username, password, project_id)
    return ret_val


# This function get sub-project info
def mc_project_get_all_subprojects(zeep_client, username='administrator', password='password', project_name=''):
    project_id = zeep_client.service.mc_project_get_id_from_name(username, password, project_name)
    ret_val = zeep_client.service.mc_project_get_all_subprojects(username, password, project_id)
    return ret_val


# This function lists projects that are accessible with specific account
def mc_projects_get_user_accessible(zeep_client, username='administrator', password='password'):
    ret_val = zeep_client.service.mc_projects_get_user_accessible(username, password)
    return ret_val


# This function lists issues with specific project. If you want to list all issues put page_number = -1
def mc_project_get_issues(zeep_client, username='administrator', password='password', project_name='', page_number = 1, per_page = 1):
    project_id = zeep_client.service.mc_project_get_id_from_name(username, password, project_name)
    ret_val = zeep_client.service.mc_project_get_issues(username, password, project_id, page_number, per_page)
    return ret_val


# This function return a list of custom fields with specific project name
def mc_project_get_custom_fields(zeep_client, username='administrator', password='password', project_name=''):
    project_id = zeep_client.service.mc_project_get_id_from_name(username, password, project_name)
    ret_val = zeep_client.service.mc_project_get_custom_fields(username, password, project_id)
    return ret_val
