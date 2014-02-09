from log import LOG
import utility
import state
import pkgutil
import fingerprints
import exploits


def definitions(ip, port):
    """
    """

    match_fps = []
    ws_fingerprints = list(pkgutil.iter_modules(fingerprints.__path__))
    for fingerprint in ws_fingerprints:
        
       fp = fingerprint[0].find_module(fingerprint[1]).load_module(fingerprint[1])
       fp = fp.WSPrint()

       if state.version:
           # we're looking for a specific version
           if fp.version is not 'Any' and state.version not in fp.version:
               continue

       utility.Msg("Checking %s version %s %s..." % (fp.platform, fp.version,
                                                      fp.title))

       if fp.check(ip, port):
           match_fps.append(fp)

    return match_fps

def exploit(fingerengine):
    """
    """

    ws_exploits = list(pkgutil.iter_modules(exploits.__path__))
    for fingerprint in fingerengine.fingerprints:
        for module in ws_exploits:

            mod = module[0].find_module(module[1]).load_module(module[1])
            if fingerengine.options.fp and fingerprint.version in mod.version:
                utility.Msg("Vulnerable to %s" % mod.name, LOG.SUCCESS)

            if module[1] == 'plugin_info' and fingerengine.options.ws_plugin:
                mod.run(fingerengine, fingerprint)
