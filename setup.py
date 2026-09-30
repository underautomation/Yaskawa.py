import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.realpath(os.path.join(os.path.dirname(__file__), "underautomation", "yaskawa", "lib", "version.txt"))

with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="UnderAutomation.Yaskawa",
    version=version,
    author="UnderAutomation",
    author_email="support@underautomation.com",
    description="Communicate with Yaskawa Motoman robot controllers (YRC1000 (micro), MOTOMAN NEXT, DX100 / DX200, FS100, ERC / XRC / MRC) over the High Speed Ethernet Server: status, alarms, positions, motion, jobs, variables, I/O and files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://underautomation.com/yaskawa",
    project_urls={
        "Documentation": "https://underautomation.com/yaskawa/documentation/get-started-python",
        "Source": "https://github.com/underautomation/Yaskawa.py",
        "Changelog": "https://github.com/underautomation/Yaskawa.py/releases",
        "Issues": "https://github.com/underautomation/Yaskawa.py/issues",
    },
    license="Commercial",
    keywords=["robot", "industrial robot", "yaskawa", "motoman", "yrc1000", "motoman next", "dx100", "dx200", "fs100", "erc", "xrc", "mrc", "hses", "high speed ethernet server"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    packages=setuptools.find_packages(include=["underautomation", "underautomation.*"]),
    python_requires="<3.14,>=3.7",
    install_requires=[
        "pythonnet==3.0.5",
    ],
    include_package_data=True,
    package_data={
        "underautomation": [
            "yaskawa/lib/*.dll",
            "yaskawa/lib/*.txt",
        ],
    },
)