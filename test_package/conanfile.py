from conans import ConanFile, CMake

class Pybind11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        import sys
        sys.path.append("bin")
        import example
        assert example.add(2, 40) == 42