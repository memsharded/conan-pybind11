from conans import ConanFile, tools, CMake


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.3.0"
    settings = "os", "compiler", "arch", "build_type"
    description = "Seamless operability between C++11 and Python"
    homepage = "https://github.com/pybind/pybind11"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/conan-community/conan-pybind11"
    no_copy_sources = True

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.configure(source_folder="pybind11-%s" % self.version)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*LICENSE", keep_path=False)
  
    def package_id(self):
        self.info.header_only()