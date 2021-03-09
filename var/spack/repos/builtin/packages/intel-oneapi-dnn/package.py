# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from sys import platform

from spack import *


class IntelOneapiDnn(IntelOneApiLibraryPackage):
    """Intel oneAPI DNN."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onednn.html'

    if platform == 'linux':
        version('2021.1.1',
                sha256='24002c57bb8931a74057a471a5859d275516c331fd8420bee4cae90989e77dc3',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17385/l_onednn_p_2021.1.1.55_offline.sh',
                expand=False)

    if platform == 'darwin':
        version('2021.1.1',
                sha256='5d3180b7db0a12be026f582a978b34597fd0c93cd1661d0e9cbd4989c376819b',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17412/m_onednn_p_2021.1.1.43_offline.dmg',
                expand=False)

    depends_on('intel-oneapi-tbb')

    def __init__(self, spec):
        self.component_info(dir_name='dnnl')
        super(IntelOneapiDnn, self).__init__(spec)
