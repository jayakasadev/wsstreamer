load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

####################
# Hermetic Python Binary Installation
# Special logic for building python interpreter with OpenSSL from homebrew.
# See https://devguide.python.org/setup/#macos-and-os-x
# https://github.com/kku1993/bazel-hermetic-python
####################
_py_configure = """
if [[ "$OSTYPE" == "darwin"* ]]; then
    ./configure --prefix=$(pwd)/bazel_install --with-openssl=$(brew --prefix openssl)
else
    ./configure --prefix=$(pwd)/bazel_install
fi
"""

http_archive(
    name = "python_interpreter",
    build_file_content = """
exports_files(["python_bin"])
filegroup(
    name = "files",
    srcs = glob(["bazel_install/**"], exclude = ["**/* *"]),
    visibility = ["//visibility:public"],
)
""",
    patch_cmds = [
        "mkdir $(pwd)/bazel_install",
        _py_configure,
        "make",
        "make install",
        "ln -s bazel_install/bin/python3 python_bin",
    ],
    sha256 = "3c2034c54f811448f516668dce09d24008a0716c3a794dd8639b5388cbde247d",
    strip_prefix = "Python-3.9.2",
    urls = ["https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz"],
)

####################
# rules_python
# https://github.com/bazelbuild/rules_python/issues/340
####################
http_archive(
    name = "rules_python",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
)

####################
# rules_pkg
####################

# Packaging (depends on skylib and rules_python)
http_archive(
    name = "rules_pkg",
    sha256 = "6b5969a7acd7b60c02f816773b06fcf32fbe8ba0c7919ccdc2df4f8fb923804a",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.3.0/rules_pkg-0.3.0.tar.gz",
        "https://github.com/bazelbuild/rules_pkg/releases/download/0.3.0/rules_pkg-0.3.0.tar.gz",
    ],
)

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()

# Our custom python toolchain must be registered at the end in order for python
# container images built with @python3.9.2_slim_buster as the base to use the
# "host" toolchain rather than the one with our locally compiled interpreter.
# See:
# https://docs.bazel.build/versions/master/toolchains.html#toolchain-resolution
register_toolchains("//:py3_toolcain")

####################
# pip_install
####################
load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "py_deps",
    python_interpreter_target = "@python_interpreter//:python_bin",
    requirements = "//:requirements.txt",
)
