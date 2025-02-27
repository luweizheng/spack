# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCommonSense(PerlPackage):
    """Save a tree AND a kitten, use common::sense!"""

    homepage = "https://metacpan.org/pod/common::sense"
    url = "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-3.75.tar.gz"

    maintainers("EbiArnie")

    version("3.75", sha256="a86a1c4ca4f3006d7479064425a09fa5b6689e57261fcb994fe67d061cba0e7e")

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use common::sense; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
