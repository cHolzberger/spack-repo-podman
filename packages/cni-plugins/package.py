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
#     spack install cni-plugins
#
# You can edit this file again by typing:
#
#     spack edit cni-plugins
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os
import shutil

class CniPlugins(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containernetworking/plugins/archive/v0.8.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.8.5', sha256='9d1526ed965ac6562fd95a931ab2346b3c5efd58c2f569038ba3c530f7e66472')
    version('0.8.6', sha256='3a77de1fcd3b818a2062d9208cab3492ad5cf8177f8fb5e86419e81143c86fa5')
    
    # FIXME: Add dependencies if required.
    depends_on('cni')

    build_directory = os.path.join( "src", "github.com", "containernetworking", "plugins" )
    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('go', type="build")
    depends_on('go-md2man', type='build')

    def do_stage(self, mirror_only=False):
       """ move the source dir to src/github.com/xxx/xxx go likes it this way """
       super().do_stage(mirror_only)
       stsrc = self.stage.source_path
       srcpath = os.path.join( stsrc, self.build_directory )
       ppath = ancestor (srcpath)
       shutil.move(stsrc, stsrc+"_old")
       mkdirp(ppath)
       shutil.move(stsrc+"_old",srcpath)


    def install(self,spec,prefix):
       bash = which('bash')
       with working_dir( os.path.join( self.stage.source_path, self.build_directory )):
          bash( './build_linux.sh' )

       env['GOPATH'] = self.stage.source_path
       target = os.path.join(prefix,"libexec", "cni")
       ppath = ancestor (target)
       mkdirp(ppath)
       shutil.move(os.path.join(self.stage.source_path, self.build_directory, "bin"), target )
 
