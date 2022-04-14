from conans import ConanFile, CMake, tools


class SimconnectPackageConan(ConanFile):
    name = "simconnect_package"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of SimconnectPackage here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "CMakeLists.txt", "src/*", "include/*", "lib/*", "bin/*"

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
