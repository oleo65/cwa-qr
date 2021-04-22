from setuptools import setup, find_packages

setup(
    name='cwa-event-qr-code',
    author='Peter Körner',
    author_email='peter@mazdermind.de',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Pillow', 'protobuf', 'qrcode', 'six'],
    version='1.0.0',
    license='None',
    long_description='Python implementation to generate the german CWA Event QR Code.',
)