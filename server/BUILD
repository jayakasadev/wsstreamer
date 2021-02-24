load("@rules_python//python:defs.bzl", "py_library", "py_binary")
load("@poetry//:dependencies.bzl", "dependency")

py_binary(
    name="server",
    srcs=["server.py"],
    python_version = "PY3",
    deps=[
        ":wsserver"
    ]
)