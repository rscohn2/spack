# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LevelZeroExternal(Package):
    """The objective of the ‘oneAPI’ Level-Zero Application Programming
       Interface (API) is to provide direct-to-metal interfaces to
       offload accelerator devices. Its programming interface can be
       tailored to any device needs and can be adapted to support
       broader set of languages features such as function pointers,
       virtual functions, unified memory, and I/O capabilities.

       To install this package, list it as an external package in
       packages.yaml.

    """

    homepage = "https://spec.oneapi.io/level-zero/latest/core/INTRO.html"
    has_code = False    # Skip attempts to fetch source that is not available

    maintainers = ['rscohn2']

    version('1.2.13')

    provides('level-zero')

    def install(self, spec, prefix):
        raise InstallError(
            self.spec.format('{name} is not installable, you need to specify '
                             'it as an external package in packages.yaml'))

    @property
    def libs(self):
        return find_libraries(['libze_loader'], root=self.prefix, recursive=True)

    @property
    def headers(self):
        include_path = join_path(self.prefix, 'include/level_zero')
        return find_headers('*.h', include_path)

