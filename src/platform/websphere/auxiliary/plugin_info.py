from log import LOG
from requests import exceptions
from re import findall
from auxiliary import Auxiliary
import utility


class Auxiliary:
    """ WebSphere exposes versioning information of all loaded plugins.
    """

    def __init__(self):
        self.name = 'Enumerate plugin versions'
        self.version = ['Any']
        self.show = True
        self.flag = 'ws-plugin'

    def check(self, fingerprint):
        return True


    def run(fingerengine, fingerprint):

        utility.Msg("Fetching WebSphere plugin information...")

        url = "https://{0}:9043/ibm/help/about.html".format(fingerengine.options.ip,
                                                           fingerprint.port)

        try:
            response = utility.requests_get(url)
            if response.status_code == 200:
            
                data = findall("<td>(.*?)</td>", response.content)
                for idx in range(4, len(data)-1, 4):
                    utility.Msg("\t%s: %s" % (data[idx + 3], data[idx + 2]))

        except exceptions.Timeout:
            utility.Msg("plugin_info timeout to {0}".format(url), LOG.DEBUG)

        except exceptions.ConnectionError:
            utility.Msg("plugin_info connection error to {0}".format(url), LOG.DEBUG)
