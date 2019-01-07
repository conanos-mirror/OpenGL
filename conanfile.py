from conans import ConanFile, tools
from conanos.build import config_scheme
import os, shutil

class OpenglConan(ConanFile):
    name = "OpenGL"
    version = "master"
    description = "The industry's most widely used and supported 2D and 3D graphics application programming interface (API)"
    url = "https://github.com/conanos/OpenGL"
    homepage = "https://www.opengl.org/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = { 'shared': True, 'fPIC': True }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

        config_scheme(self)

    def source(self):
        url_ = "https://github.com/CentricularK/OpenGL-Registry.git"
        branch_ = "master"
        git = tools.Git(folder="OpenGL-Registry")
        git.clone(url_, branch=branch_)
        os.rename("OpenGL-Registry", self._source_subfolder)

    def build(self):
        pass
    
    def package(self):
        self.copy("*", dst=os.path.join(self.package_folder,"include","GL"), src=os.path.join(self.build_folder,self._source_subfolder, "api","GL"))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

