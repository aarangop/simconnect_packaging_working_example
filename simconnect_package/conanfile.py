import os

from conan import ConanFile
from conan.tools.files import copy


class SimconnectPackageConan(ConanFile):
    name = "simconnect_package"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    # No "shared" option, it seems it is always shared

    def package(self):
        copy(self, "SimConnect.h", src=os.path.join(self.source_folder, "include"), 
             dst=os.path.join(self.package_folder, "include"))

        if self.settings.build_type == "Debug":
            pattern_dll = "*Connect.Debug.dll"
            pattern_lib = "*ConnectDebug.lib"
        else:
            pattern_dll = "*Connect.dll"
            pattern_lib = "*Connect.lib"

        copy(self, pattern_dll, src=os.path.join(self.build_folder, "bin"), 
                dst=os.path.join(self.package_folder, "bin"))
        copy(self, pattern_lib, src=os.path.join(self.build_folder, "lib"), 
                dst=os.path.join(self.package_folder, "lib"))

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["SimConnectDebug"]
        else:
            self.cpp_info.libs = ["SimConnect"]
