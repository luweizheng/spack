# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlRefUtil(PerlPackage):
    """Utility functions for checking references"""

    homepage = "https://metacpan.org/pod/Ref::Util"
    url = "https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz"

    maintainers("EbiArnie")

    version("0.204", sha256="415fa73dbacf44f3d5d79c14888cc994562720ab468e6f71f91cd1f769f105e1")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Ref::Util; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
