def mc_issue_attachment_add(zeep_client, username, password, issue_id, file_stream):
    arr_filename = file_stream.name.split('\\')
    name = arr_filename[len(arr_filename)-1]
    if '.' in name:
        name_parsed = name.split('.')
        file_type = name_parsed[len(name_parsed)-1]
    else:
        file_type = "NA"
    content = file_stream.read()
    return zeep_client.service.mc_issue_attachment_add(username=username, password=password, issue_id=issue_id, name=name, file_type=file_type, content=content)


