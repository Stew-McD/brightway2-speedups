name: Build

on: [push]

jobs:
  build_wheels:
    name: Build wheels on ${{ matrix.os }}
    env:
      CIBW_BEFORE_BUILD: pip install Cython
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-20.04, windows-2019, macos-11]

    steps:
      - uses: actions/checkout@v3

      - name: Build wheels
        uses: pypa/cibuildwheel@v2.11.2
        # env:
        #   CIBW_SOME_OPTION: value
        #    ...
        # with:
        #   package-dir: .
        #   output-dir: wheelhouse
        #   config-file: "{package}/pyproject.toml"

      - uses: actions/upload-artifact@v3
        with:
          path: ./wheelhouse/*.whl