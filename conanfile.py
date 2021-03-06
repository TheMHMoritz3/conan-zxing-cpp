from conans import ConanFile, CMake, tools
import os

class ZXingCppConan(ConanFile):
    name = "zxing-cpp"
    version = "1.0.7"
    license = "Apache License Version 2.0"
    author = "TheMHMoritz3 mhmoritz3@gmail.com"
    url = "https://github.com/nu-book/zxing-cpp"
    description = "This project is a C++ port of ZXing Library."
    topics = ("Bar Code", "ZXing")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/nu-book/zxing-cpp.git")

        tools.replace_in_file("zxing-cpp/CMakeLists.txt", "project (ZXingCpp VERSION ${ZXING_VERSION_MAJOR}.${ZXING_VERSION_MINOR}.${ZXING_VERSION_PATCH})",
                              '''project (ZXingCpp VERSION ${ZXING_VERSION_MAJOR}.${ZXING_VERSION_MINOR}.${ZXING_VERSION_PATCH})
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="zxing-cpp")
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
