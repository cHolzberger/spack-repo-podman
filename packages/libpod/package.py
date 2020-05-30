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
#     spack install libpod
#
# You can edit this file again by typing:
#
#     spack edit libpod
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

import os
import shutil

class Libpod(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containers/libpod/archive/v1.8.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
   version('1.9.3',     sha256='595531edeb51df53276d620fec370bb147f737d0047e93316fd0a5a6d847ef43') 
   version('1.8.2',     sha256='69f7ff81da1510ebf2962c1de3170675ca3cd8a24bc00c93742a24bcce17c752')
    version('1.8.0',     sha256='2f771dc5505bd29e21e18a71e6eac549d036ad34fbbec5646ae0c7bfe024eeb5')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('go', type="build")
    depends_on('go-md2man', type='build')
    depends_on('gpgme')
    depends_on('libassuan')
    depends_on('libgpg-error')
    depends_on('lvm2')
    depends_on('libseccomp')
    depends_on('conmon')
    depends_on('runc')
    depends_on('crun')
    depends_on('cni-plugins')
    depends_on('catatonit')

    build_directory = os.path.join( "src", "github.com", "containers", "libpod" )
 
    def edit(self, spec, prefix):
        env['GOPATH'] = self.stage.source_path
   
    def do_stage(self, mirror_only=False):
       """ move the source dir to src/github.com/xxx/xxx go likes it this way """
       super().do_stage(mirror_only)
       stsrc = self.stage.source_path
       srcpath = os.path.join( stsrc, self.build_directory )
       ppath = ancestor (srcpath)
       shutil.move(stsrc, stsrc+"_old")
       mkdirp(ppath)
       shutil.move(stsrc+"_old",srcpath)

    def build(self, spec, prefix):
       with working_dir( self.build_directory ):
         make('podman','BUILDTAGS=systemd seccomp exclude_graphdriver_btrfs	exclude_graphdriver_devicemapper','ETCDIR={0}/etc'.format(prefix))

    def install(self, spec, prefix):
       with working_dir( self.build_directory ):
         make('install',
             'PREFIX={0}'.format(prefix),'ETCDIR={0}/etc'.format(prefix)) 
 
