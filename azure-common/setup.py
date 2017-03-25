#!/usr/bin/env python

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

from setuptools import setup
import sys
from azure_wheel import cmdclass

# azure v0.x is not compatible with this package
# azure v0.x used to have a __version__ attribute (newer versions don't)
try:
    import azure
    try:
        ver = azure.__version__
        raise Exception(
            'This package is incompatible with azure=={}. '.format(ver) +
            'Uninstall it with "pip uninstall azure".'
        )
    except AttributeError:
        pass
except ImportError:
    pass

INSTALL_REQUIRES=[]
if "bdist_wheel" in sys.argv:
    INSTALL_REQUIRES.append('azure-nspkg>=2.0.0')

setup(
    name='azure-common',
    version='1.1.5',
    description='Microsoft Azure Client Library for Python (Common)',
    long_description=open('README.rst', 'r').read(),
    license='MIT License',
    author='Microsoft Corporation',
    author_email='ptvshelp@microsoft.com',
    url='https://github.com/Azure/azure-sdk-for-python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    packages=[
        'azure',
        'azure.common',
    ],
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'autorest':[
            'msrestazure>=0.4.0,<0.5.0',
        ]
    },
    cmdclass=cmdclass
)
