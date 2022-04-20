import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("CMD FAILED: {}".format(cmd))


os.chdir("simconnect_package")
run("conan remove simconnect* -f")
run("conan export-pkg .")
run("conan export-pkg . -s build_type=Debug")

os.chdir("../simconnect_package_consumer")
run("conan create .")
run("conan create . -s build_type=Debug")