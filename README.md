# conan-pybind11

![pybind11 image](/images/conan-pybind11.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/pybind11%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/pybind11%3Aconan/_latestVersion)
[![Build Status](https://travis-ci.org/conan-community/conan-pybind11.svg?branch=release%2F2.4.3)](https://travis-ci.org/conan-community/conan-pybind11)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/release/2.4.3?svg=true)](https://ci.appveyor.com/project/memsharded/conan-pybind11/branch/release/2.4.3)

[Conan.io](https://conan.io) package recipe for [pybind11](https://github.com/pybind/pybind11) project.

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/pybind11%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install pybind11/2.4.3@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    pybind11/2.4.3@conan/stable

    [generators]
    cmake

## License

[MIT License](LICENSE)
