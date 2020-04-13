# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install conmon
#
# You can edit this file again by typing:
#
#     spack edit conmon
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Conmon(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containers/conmon/archive/v2.0.14.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.0.10', sha256='f1e084aa264ee20eb20a3e0618e538f10fde5e2a10046e191f998f45b5cf3b3b')
    version('2.0.14', sha256='4add62ad9f62f4a00c1b145d5a1f5e0dc47aa44001fb505a25fdbf7b50542ece')

    depends_on('glib')

    def install(self, spec, prefix):
      make('install',
             'PREFIX={0}'.format(prefix)) 
 
