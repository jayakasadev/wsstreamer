load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_deps//:requirements.bzl", "requirement")

py_library(
    name = "wsclient",
    srcs = [":srcs"],
    imports = [".."],
    visibility = ["//wsstream:__pkg__"],
    deps = [
        "@rules_python//python/runfiles",
        requirement("python-socketio"),
    ],
)

filegroup(
    name = "srcs",
    srcs = glob(["*.py"]),
    visibility = ["//wsstream:__pkg__"],
)

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        requirement("python-socketio"),
    ],
)
