load("@rules_python//python:defs.bzl", "py_library", "py_binary")
load("@poetry//:dependencies.bzl", "dependency")

py_library(
    name = "wsclient",
    srcs = [":srcs"],
    imports = ["../.."],
    visibility = ["//:__pkg__"],
    deps = [
        "@rules_python//python/runfiles",
    ],
)

filegroup(
    name = "srcs",
    srcs = glob(["*.py"]),
    visibility = ["//:__pkg__"],
)

py_binary(
    name="server",
    srcs=["server.py"],
    python_version = "PY3",
    deps=[
        ":wsserver"
    ]
)