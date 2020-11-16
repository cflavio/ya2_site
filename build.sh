#!/usr/bin/env bash
source ~/venv/bin/activate
rm -rf _build docs
sphinx-apidoc -o docs ../../yorg
sed -i '1s;^;.. _modules-page:\n\n;' docs/modules.rst
make html
python postprocess.py
echo "comment ~/venv/lib/python3.6/site-packages/sphinxcontrib/newsfeed.py's output.append(wrappernode)"
echo "~/venv/lib/python3.6/site-packages/sphinxcontrib/newsfeed.py: date_node += nodes.Text(date.strftime('%Y-%m-%d'))"
echo "use ./sphinx_git.py in place of ~/venv/lib/python3.6/site-packages/sphinx_git/__init__.py"
