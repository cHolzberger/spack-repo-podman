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
#     spack install buildah
#
# You can edit this file again by typing:
#
#     spack edit buildah
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Buildah(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/containers/buildah/archive/v1.14.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.14.0', sha256='3eb637c5a5b35ba865886d20ce937e7c6b2929573c03af09a86c3be11151ec80')
    version('1.14.5', sha256='74633280c814d340ed32653106bc706f306cf78afb57bb51c3cdca8893d95bd4')

    depends_on('go',type='build')
    depends_on('go-md2man', type='build')
    depends_on('gpgme')
    depends_on('libassuan')
    depends_on('libgpg-error')
    depends_on('lvm2')
    depends_on('libseccomp')
	
    def edit(self, spec, prefix):
        grep = which('grep')
        files = grep('-lR', '/etc/containers/', 'vendor', output=str,
                     env={'PATH': '/usr/bin:/bin:/usr/sbin:/sbin'})
        env['GIT_COMMIT']="v1.14.0"
        for f in files.splitlines():
            edit = FileFilter(f)
            edit.filter('/etc/containers/', '{0}/etc/containers/'.
                        format(prefix))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make( 'install',
             'PREFIX={0}'.format(prefix))
