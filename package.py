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
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["python-3.9"],
]

uuid = "repository.doxygen"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        # NOTE: usually we use devtoolset-6 (that provides GCC 6.3.1) for all/any USD-related
        # builds. But it seems to be too old for Doxygen.
        command("source /opt/rh/devtoolset-7/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.DOXYGEN_ROOT.append("{root}")
    env.DOXYGEN_LOCATION.append("{root}")

    env.PATH.append("{root}/bin")
