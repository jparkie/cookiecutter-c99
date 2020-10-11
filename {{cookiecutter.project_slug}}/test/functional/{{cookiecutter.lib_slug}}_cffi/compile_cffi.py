import subprocess
import sys

import cffi

if __name__ == "__main__":
    path_include_dir = sys.argv[1]
    path_library_dir = sys.argv[2]

    lib_cffi = cffi.FFI()

    preprocess = subprocess.run(
        "gcc -E -P %s/{{cookiecutter.lib_slug}}/*.h" % path_include_dir,
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    csource = preprocess.stdout
    csource = csource[csource.find("typedef void {{cookiecutter.lib_slug.upper()}}_UNUSED;"):]
    csource = "\n".join([
        csource,
        """
        """
    ])

    lib_cffi.cdef(csource)
    lib_cffi.set_source(
        "_{{cookiecutter.lib_slug}}_cffi",
        """
        #include "{{cookiecutter.lib_slug}}/{{cookiecutter.lib_slug}}.h"
        """,
        libraries=["{{cookiecutter.lib_slug}}"],
        include_dirs=[path_include_dir, ],
        library_dirs=[path_library_dir, ],
    )

    lib_cffi.compile()
