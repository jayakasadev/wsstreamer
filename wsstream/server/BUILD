load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_deps//:requirements.bzl", "requirement")


py_library(
    name = "wsserver",
    srcs = [":srcs"],
    imports = [".."],
    visibility = ["//wsstream:__pkg__"],
    deps = [
        "@rules_python//python/runfiles",
        requirement("docopt"),
        requirement("eventlet"),
        requirement("flask"),
        requirement("flask-socketio"),
    ],
)

filegroup(
    name = "srcs",
    srcs = glob(["*.py"]),
    visibility = ["//wsstream:__pkg__"],
)

py_binary(
    name = "server",
    srcs = ["server.py"],
    imports = [".."],
    visibility = ["//wsstream:__pkg__"],
    deps = [
        "//wsstream/util",
        "@rules_python//python/runfiles",
        requirement("docopt"),
        requirement("eventlet"),
        requirement("flask"),
        requirement("flask-socketio"),
    ],
)
