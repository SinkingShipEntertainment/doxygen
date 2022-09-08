name = "doxygen"

authors = [
    "Dimitry van Heesch"
]

version = "1.9.5"

description = \
    """
    Generate documentation from source code.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
    #"qt-5.14.1",
    "python-3.9.7",
]

private_build_requires = [
]

variants = [
    #["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.doxygen"

def pre_build_commands():
    # NOTE: usually we use devtoolset-6 (that provides GCC 6.3.1) for all/any USD-related
    # builds. But it seems to be too old for Doxygen.
    command("source /opt/rh/devtoolset-7/enable")

def commands():
    env.DOXYGEN_ROOT.append("{root}")
    env.DOXYGEN_LOCATION.append("{root}")

    env.PATH.append("{root}/bin")
