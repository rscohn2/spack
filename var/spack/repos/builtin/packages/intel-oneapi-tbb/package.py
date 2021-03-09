# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from sys import platform

from spack import *


class IntelOneapiTbb(IntelOneApiLibraryPackage):
    """Intel oneAPI TBB."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onetbb.html'

    if platform == 'darwin':
        version('2021.1.1',
                sha256='15a703eb8093ff070e17e4191ccec132c1bcd4f72963204c0f10adcfe68aa17d',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17409/m_tbb_oneapi_p_2021.1.1.110_offline.dmg',
                expand=False)

    if platform == 'linux':
        version('2021.1.1',
                sha256='535290e3910a9d906a730b24af212afa231523cf13a668d480bade5f2a01b53b',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17378/l_tbb_oneapi_p_2021.1.1.119_offline.sh',
                expand=False)

    provides('tbb')

    def __init__(self, spec):
        self.component_info(dir_name='tbb')
        super(IntelOneapiTbb, self).__init__(spec)
