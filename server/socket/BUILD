py_library(
    name = "wsserver",
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