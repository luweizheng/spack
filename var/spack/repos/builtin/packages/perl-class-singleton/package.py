# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClassSingleton(PerlPackage):
    """Class::Singleton - Implementation of a "Singleton" class"""

    homepage = "https://metacpan.org/pod/Class::Singleton"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHAY/Class-Singleton-1.6.tar.gz"

    maintainers("EbiArnie")

    version("1.6", sha256="27ba13f0d9512929166bbd8c9ef95d90d630fc80f0c9a1b7458891055e9282a4")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Class::Singleton; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
