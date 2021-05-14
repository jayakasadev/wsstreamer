load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "util",
    srcs = [
        "logging.py"
    ],
    imports = [".."],
    visibility = ["//wsstream:__subpackages__"],
    deps = [
        "@rules_python//python/runfiles",
    ],
)