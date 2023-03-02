from conan import ConanFile
from conan.tools import files

import os

class FastNoiseLiteConan(ConanFile):
    name = "fastnoise-lite"
    version = "1.0.3.2111"
    license = "MIT"
    url = "https://github.com/triadastudio/conan-fastnoise-lite.git"
    homepage = "https://github.com/Auburn/FastNoiseLite"
    description = "FastNoise Lite is an extremely portable open source noise generation library with a large selection of noise algorithms"
    topics = ("noise", "perlin", "simplex")
    package_type = "header-library"
    no_copy_source = True

    @property
    def _source_commit(self):
        return "6be3d6bf7fb408de341285f9ee8a29b67fd953f1"

    def source(self):
        files.get(self,
                  url="https://github.com/Auburn/FastNoiseLite/archive/{}.zip".format(self._source_commit),
                  pattern="*/Cpp/*",
                  strip_root=True)

    def package_id(self):
        self.info.clear()

    def package(self):
        files.copy(self,
                   pattern="*.h",
                   src=self.source_folder,
                   dst=os.path.join(self.package_folder, "include"),
                   keep_path=False)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
