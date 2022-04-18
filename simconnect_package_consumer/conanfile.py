from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class SimconnectConsumerConan(ConanFile):
    name = "simconnect_consumer"
    version = "0.1"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    requires = "simconnect_package/0.1"

    generators = "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
