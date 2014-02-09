import state

def _auth(usr, pswd, url, version):
    """
    """
    
    pass


def checkAuth(ip, port, title, version):
    """
    """

    url = "https://{0}:{1}/ibm/console/j_security_check"
    if state.usr_auth:
        (usr, pswd) = state.usr_auth.split(':')
        return _auth(usr, pswd, url, version)
