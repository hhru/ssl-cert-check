from setuptools import setup

_version = '0.0.2'

setup(
    name='hh-ssl-cert-check',
    version=_version,
    scripts=['hh-ssl-cert-check'],
    author='Nikita Kovaliov',
    author_email='n.kovalev@hh.ru',
    description='SSL certificates check script',
    license='Apache License 2.0',
    download_url='https://github.com/hh.ru/ssl-cert-check/tarball/{}'.format(_version),
    keywords='ssl p12 pem check',
    url='https://github.com/hh.ru/ssl-cert-check',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
)
