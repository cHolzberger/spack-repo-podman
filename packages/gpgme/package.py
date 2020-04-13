# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gpgme(AutotoolsPackage):
    """GPGME is the standard library to access GnuPG
       functions from programming languages."""

    homepage = "https://www.gnupg.org/software/gpgme/index.html"
    url      = "https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.13.1.tar.bz2"

    version('1.12.0', sha256='b4dc951c3743a60e2e120a77892e9e864fb936b2e58e7c77e8581f4d050e8cd8')
    version('1.13.1', sha256='c4e30b227682374c23cddc7fdb9324a99694d907e79242a25a4deeedb393be46')

    depends_on('gnupg', type='build')
    depends_on('libgpg-error', type='build')
    depends_on('libassuan', type='build')
 
    def edit(self, spec, prefix):
        env['py_tests'] = ''
    
    def configure_args(self):
        args=[]
        args.append('--disable-fd-passing')
        args.append('--disable-static')
        args.append('--disable-gpgsm-test')
        args.append('--disable-gpg-test')
        args.append('--disable-g13-test')
        args.append('--disable-gpgconf-test')
        args.append('--enable-languages=cl cpp')
        return args
    
    def patch(self):
        conf = FileFilter('configure')                                                         
        conf.filter('-Wall', '')
    
        makefile = FileFilter('Makefile.am')
        makefile.filter('tests = tests', 'tests = ')

        makefile = FileFilter('tests/gpg/Makefile.am')
        makefile.filter('all: all-recursive',"all: ")
        makefile.filter('tests_unix = t-eventloop t-thread1 t-thread-keylist t-thread-keylist-verify','tests_unix = ')
