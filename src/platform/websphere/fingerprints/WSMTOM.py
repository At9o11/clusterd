from src.platform.websphere.interfaces import WSINTERFACES
from requests import exceptions
from cprint import FingerPrint
from log import LOG
import utility


class FPrint(FingerPrint):

    def __init__(self):
        self.platform = "websphere"
        self.version = 'Any'
        self.title = WSINTERFACES.APP_MTOM
        self.uri = '/wssamplemtom/demo'
        self.port = 9080
        self.hash = None

    def check(self, ip, port = None):
        """
        """

        try:
            rport = self.port if port is None else port
            response = utility.requests_get('http://{0}:{1}{2}'.format(
                                                    ip, rport, self.uri))

            if response.status_code == 200:
                if 'MTOM Sample' in response.content:
                    return True

        except exceptions.Timeout:
            utility.Msg("{0} timeout to {1}:{2}".format(self.platform,
                                                        ip, rport),
                                                        LOG.DEBUG)
        except exceptions.ConnectionError:
            utility.Msg("{0} connection error to {1}:{2}".format(self.platform,
                                                            ip, rport),
                                                            LOG.DEBUG)

        return False
