# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install criu
#
# You can edit this file again by typing:
#
#     spack edit criu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Criu(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://download.openvz.org/criu/criu-3.13.tar.bz2"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.13', sha256='ea027f2acb55c62d47aec0c7776c723e5a877978e60d3574961b6f4c538fc9fa')

    # FIXME: Add dependencies if required.
    depends_on('protobuf-c')
    depends_on('libbsd')
    depends_on('libtool')
    depends_on('automake')
    depends_on('libseccomp')
    depends_on('libnet')
#    depends_on('libcap')
    depends_on('libaio')
    def edit(self, spec, prefix):
        env['GITID'] = 'release'
 
    def build(self, spec, prefix):
       make("WERROR=0","GITID=release")

    def install(self, spec, prefix):
         make('install',
             'PREFIX={0}'.format(prefix),'ETCDIR={0}/etc'.format(prefix),"GITID=release") 
 
