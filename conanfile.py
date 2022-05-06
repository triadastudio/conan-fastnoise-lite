from conans import ConanFile, tools
import os

class FastNoiseLiteConan(ConanFile):
    name = "fastnoise-lite"
    version = "1.0.3.2111"
    license = "MIT"
    url = "https://github.com/triadastudio/conan-fastnoise-lite.git"
    homepage = "https://github.com/Auburn/FastNoiseLite"
    description = "FastNoise Lite is an extremely portable open source noise generation library with a large selection of noise algorithms"
    topics = ("noise", "perlin", "simplex")
    no_copy_source = True

    @property
    def _dir_name(self):
        return "Cpp"

    @property
    def _source_commit(self):
        return "6be3d6bf7fb408de341285f9ee8a29b67fd953f1"

    @property
    def _source_subfolder(self):
        return os.path.join(self.source_folder, self._dir_name)

    def source(self):
        tools.get(url="https://github.com/Auburn/FastNoiseLite/archive/{}.zip".format(self._source_commit),
                  pattern="*/{}/*".format(self._dir_name),
                  strip_root=True)

    def package(self):
        self.copy("*.h", dst="include", src=self._source_subfolder, keep_path=False)
