import os

from picobuild import Extension, cythonize, find_packages, setup

# Portable by default for redistributable wheels/sdists.
# Set CPY_NATIVE=1 for local benches that want -march=native.
_compile_args = [
    "-O3",
    "-Wno-unused-function",
    "-Wno-unused-variable",
]
if os.environ.get("CPY_NATIVE", "").strip() in ("1", "true", "yes"):
    _compile_args.insert(1, "-march=native")

# Cython extensions — same shape as cycel.core.cpy, package name ``cypy``.
cythonized_extensions = cythonize(
    [
        Extension(
            "cypy.uuid._uuid",
            [
                "src/cypy/uuid/_uuid.pyx",
                "src/cypy/uuid/uuid.c",
            ],
            include_dirs=["src/cypy/uuid"],
            extra_compile_args=_compile_args,
            libraries=["crypto"],
            language="c",
        ),
        Extension(
            "cypy.*",
            ["src/cypy/*.pyx"],
            include_dirs=["src/cypy"],
            extra_compile_args=_compile_args,
            language="c",
        ),
    ]
)


if __name__ == "__main__":
    setup(
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        package_data={"cypy": ["py.typed", "**/*.pxd", "**/*.pxi", "**/*.h", "**/*.pyi"]},
        ext_modules=cythonized_extensions,
    )
