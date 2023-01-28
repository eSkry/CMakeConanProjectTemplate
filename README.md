# CMake with Conan template

## How build the template

There are 2 approaches in the project.
1. Build with Conan and Cmake using default commands:
```bash
conan install ../conanfile.txt --build=missing
cmake '-G Unix Makefiles' ..
cmake --build . --config Release
```
1. Build with python script `make.py`:
```bash
python3 ./make.py
```
