load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
    name = "app",
    srcs = [":srcs"],
    imports = ["."],
    visibility = ["//wsstream:__subpackages__"],
    deps = [
        "@rules_python//python/runfiles",
        "//wsstream/util",
        "//wsstream/server",
        "//wsstream/client"
    ],
)

filegroup(
    name = "srcs",
    srcs = glob(["*.py"]),
    visibility = ["//wsstream:__subpackages__"],
)

py_binary(
    name = "visibility",
    srcs = ["visibility.py"],
    deps = [
        "//wsstream/util",
#        "//wsstream/server:wsserver",
#        "//wsstream/client:wsclient",
    ],
)
