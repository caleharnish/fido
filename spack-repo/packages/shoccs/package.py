# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install shoccs
#
# You can edit this file again by typing:
#
#     spack edit shoccs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Shoccs(CMakePackage):
    """Stable High-Order Cut-Cell Solver"""

    homepage = "https://github.com/caleharnish/shoccs"
    git      = "https://github.com/caleharnish/shoccs.git"

    maintainers = ['pbrady','caleharnish']

    version('develop', branch='main')
    version('2023-03', commit='ea1ef2dc1c7656fe5b685a355ec4e771318c063f', preferred=True)
    version('2022-04', commit='90f7ad1277e7e746ee506b33f530b016240b094e')
    version('2022-02', commit='2203cab4e2bc69e365f6f8a780a47ac33d3108fa')

    depends_on('lua-sol2')
    depends_on('cmake@3.16:')
    depends_on('range-v3@0.11:')
    depends_on('pugixml')
    depends_on('fmt@8:')
    depends_on('spdlog@1.9: +fmt_external')
    depends_on('cxxopts@3:')
    depends_on('boost cxxstd=2a')
    depends_on('lapackpp')
    depends_on('catch2@3:')

    def cmake_args(self):
        return [
            self.define('BUILD_TESTING', self.run_tests),
        ]
