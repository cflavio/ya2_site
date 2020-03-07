#!/usr/bin/env bash
source ~/venv/bin/activate
rm -rf _build docs
sphinx-apidoc -o docs ../../yorg
sed -i '1s;^;.. _modules-page:\n\n;' docs/modules.rst
make html
