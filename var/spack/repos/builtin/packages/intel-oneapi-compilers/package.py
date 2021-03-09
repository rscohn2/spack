# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import subprocess
from os import path
from sys import platform

from spack import *


class IntelOneapiCompilers(IntelOneApiPackage):
    """Intel OneAPI compilers

    Provides Classic and Beta compilers for: Fortran, C, C++"""

    homepage = "https://software.intel.com/content/www/us/en/develop/tools/oneapi.html"

    depends_on('patchelf', type='build')

    if platform == 'linux':
        version('2021.1.2',
                sha256='68d6cb638091990e578e358131c859f3bbbbfbf975c581fd0b4b4d36476d6f0a',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17513/l_dpcpp-cpp-compiler_p_2021.1.2.63_offline.sh',
                expand=False)
        resource(name='fortran-installer',
                 url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17508/l_fortran-compiler_p_2021.1.2.62_offline.sh',
                 sha256='29345145268d08a59fa7eb6e58c7522768466dd98f6d9754540d1a0803596829',
                 expand=False,
                 placement='fortran-installer',
                 when='@2021.1.2')

    if platform == 'darwin':
        version('2021.1.2',
                sha256='fb964952ee09acb3c1566e039776983d40cb838179d63438e26538e916300e1c',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17510/m_cpp-compiler-classic_p_2021.1.2.66_offline.dmg',
                expand=False)
        resource(name='fortran-installer',
                 url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17511/m_fortran-compiler-classic_p_2021.1.2.87_offline.dmg',
                 sha256='06ccc11ad545f5f819585e05178dda700cf262956887e7d5a39fb52ebd7eb036',
                 expand=False,
                 placement='fortran-installer',
                 when='@2021.1.2')

    def __init__(self, spec):
        self.component_info(dir_name='compiler')
        super(IntelOneapiCompilers, self).__init__(spec)

    def _join_prefix(self, p):
        return path.join(self.prefix, 'compiler/latest/linux', p)

    def _ld_library_path(self):
        dirs = ['lib',
                'lib/x64',
                'lib/emu',
                'lib/oclfpga/host/linux64/lib',
                'lib/oclfpga/linux64/lib',
                'compiler/lib/intel64_lin',
                'compiler/lib']
        for dir in dirs:
            yield self._join_prefix(dir)

    def install(self, spec, prefix):
        # install cpp
        # Copy instead of install to speed up debugging
        # subprocess.run(f'cp -r /opt/intel/oneapi/compiler {prefix}', shell=True)
        super(IntelOneapiCompilers, self).install(spec, prefix)

        # install fortran
        super(IntelOneapiCompilers, self).install(spec,
                                                  prefix,
                                                  installer_path=glob.glob('fortran-installer/*')[0])

        # Some installers have a bug and do not return an error code when failing
        if not path.isfile(path.join(prefix, 'compiler/latest/linux/bin/intel64/ifort')):
            raise RuntimeError('install failed')

        # set rpath so 'spack compiler add' can check version strings
        # without setting LD_LIBRARY_PATH
        rpath = ':'.join(self._ld_library_path())
        patch_dirs = ['compiler/lib/intel64_lin',
                      'compiler/lib/intel64',
                      'bin']
        for pd in patch_dirs:
            patchables = glob.glob(self._join_prefix(path.join(pd, '*')))
            patchables.append(self._join_prefix('lib/icx-lto.so'))
            for file in patchables:
                # Try to patch all files, patchelf will do nothing if
                # file should not be patched
                subprocess.call(['patchelf', '--set-rpath', rpath, file])
