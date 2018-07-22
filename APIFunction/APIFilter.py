# This function retrieve issues that match specific filter
def mc_filter_search_issues(zeep_client, filter, username='administrator', password='password', page_number=-1, per_page=0):
    ret_val = zeep_client.service.mc_filter_search_issues(username, password, filter, page_number, per_page)
    return ret_val