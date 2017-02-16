import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='gocffi',
        packages=setuptools.find_packages(),
        zip_safe=False,
        build_golang={'root': 'github.com/nils-werner/python-go-cffi'},
        setup_requires=[
            'setuptools-golang>=1.1.0',
            'cffi>=1.1.0',
        ],
        install_requires=[
            'numpy>=1.6',
            'scipy>=0.13.0',
            'cffi>=1.1.0',
        ],
        ext_modules=[
            setuptools.Extension('py.__gosum', ['go/sum.go']),
        ],
        cffi_modules=[
            "py/build.py:ffibuilder",
        ],
    )
