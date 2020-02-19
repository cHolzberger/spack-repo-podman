# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME" # next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install runc
#
# You can edit this file again by typing:
#
#     spack edit runc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os
import shutil 

class Runc(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/opencontainers/runc/archive/v1.0.0-rc10.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.0-rc10', sha256='6b44985023347fb9c5a2cc6f761df8c41cc2c84a7a68a6e6acf834dff6653a9a')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('go')
    depends_on('go-md2man', type='build')
    depends_on('gpgme')
    depends_on('libassuan')
    depends_on('libgpg-error')
    depends_on('lvm2')
    depends_on('libseccomp')

    build_directory = os.path.join( "src", "github.com", "opencontainers", "runc" )
 
    def edit(self, spec, prefix):
        env['GOPATH'] = self.stage.source_path
   
    def do_stage(self, mirror_only=False):
       super().do_stage(mirror_only)
       stsrc = self.stage.source_path
       srcpath = os.path.join( stsrc, "src", "github.com", "opencontainers", "runc" )
       ppath = os.path.join( stsrc, "src", "github.com", "opencontainers" )
       shutil.move(stsrc, stsrc+"_old")
       mkdirp(ppath)
       shutil.move(stsrc+"_old",srcpath)

    def install(self, spec, prefix):
       with working_dir( self.build_directory ):
         make('install',
             'DESTDIR={0}'.format(prefix),
             'PREFIX={0}'.format(prefix)) 
   
