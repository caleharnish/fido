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


class Fido(CMakePackage):
    """Finite Difference Optimizer"""

    homepage = "https://github.com/caleharnish/fido"
    git      = "https://github.com/caleharnish/fido.git"

    maintainers = ['pbrady','caleharnish']

    version('develop', branch='main')

    depends_on("shoccs")
    depends_on("nlopt ~python")
    depends_on("legion")
