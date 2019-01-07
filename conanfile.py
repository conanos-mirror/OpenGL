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
        tools.mkdir(self._source_subfolder)
        branch_ = "master"
        with tools.chdir(self._source_subfolder):
            opengl_url_ = "https://github.com/CentricularK/OpenGL-Registry.git"
            git = tools.Git(folder="OpenGL-Registry")
            git.clone(opengl_url_, branch=branch_)
            
            #os.rename("OpenGL-Registry", self._source_subfolder)
            egl_url_ = "https://github.com/KhronosGroup/EGL-Registry.git"
            egl_git = tools.Git(folder="EGL-Registry")
            egl_git.clone(egl_url_, branch=branch_)
            
            #os.rename("EGL-Registry", self._source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy("*", dst=os.path.join(self.package_folder,"include","GL"), src=os.path.join(self.build_folder,self._source_subfolder,"OpenGL-Registry", "api","GL"))
        self.copy("*", dst=os.path.join(self.package_folder,"include","KHR"), src=os.path.join(self.build_folder,self._source_subfolder,"EGL-Registry", "api","KHR"))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

