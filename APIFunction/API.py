# This function return information of specific account
def mc_login(zeep_client, username='administrator', password='password'):
    ret_val = zeep_client.service.mc_login(username, password)
    return ret_val
