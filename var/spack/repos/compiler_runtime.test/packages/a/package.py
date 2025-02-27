# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class A(Package):
    homepage = "http://www.example.com"
    has_code = False

    version("1.0")
    depends_on("b")
