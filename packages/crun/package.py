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
#     spack install crun
#
# You can edit this file again by typing:
#
#     spack edit crun
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Crun(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containers/crun/releases/download/0.13/crun-0.13.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('0.12.2.1', sha256='e7148e9d7cd9c5a0538b8ba19bbb00f15715ae24d250b45251ce7cc1ad8dd695' )
    version('0.13', sha256='a7a9f458fa4c13fc63f8e74c6ce660f9c439022cd50b4a00902c258ef08e75ff')

    # FIXME: Add dependencies if required.
    depends_on('libtool')
    depends_on('automake')
    depends_on('yajl')
    depends_on('libassuan')
    depends_on('libgpg-error')
    depends_on('libseccomp')
    depends_on('lvm2')
#    depends_on('libcap')
    #depends_on('criu')
    depends_on('go-md2man', type=('build'))
    
    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
