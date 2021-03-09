# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from sys import platform

from spack import *


class IntelOneapiIppcp(IntelOneApiLibraryPackage):
    """Intel oneAPI IPP Crypto."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/ipp.html'

    if platform == 'linux':
        version('2021.1.1',
                sha256='c0967afae22c7a223ec42542bcc702121064cd3d8f680eff36169c94f964a936',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17415/l_ippcp_oneapi_p_2021.1.1.54_offline.sh',
                expand=False)

    if platform == 'darwin':
        version('2021.1.1',
                sha256='d1ed96b61acc9afce44413b1880a82a954590bd6831d28ab8478c31cbe4a7ffc',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17410/m_ippcp_oneapi_p_2021.1.1.53_offline.dmg',
                expand=False)

    def __init__(self, spec):
        self.component_info(dir_name='ippcp')
        super(IntelOneapiIppcp, self).__init__(spec)
