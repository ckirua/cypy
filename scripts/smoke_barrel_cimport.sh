#!/usr/bin/env bash
# Smoke: out-of-tree extension with ``from cypy cimport …`` against installed cypy.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXT="${ROOT}/examples/cimport_ext"

python -c "import cypy; print('cypy', cypy.__version__)"

cd "${EXT}"
rm -f demo.c demo*.so demo*.pyd
python setup.py build_ext --inplace
python -c "import demo; assert demo.check_barrel(); assert demo.check_submodule() == 2; assert demo.check_uuid(); print('barrel cimport ok')"
