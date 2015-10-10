from setuptools import setup

setup(
    name="dslink-python-sound",
    version="0.0.1",
    description="Python DSLink that can play sound files.",
    url="https://github.com/IOT-DSA/dslink-python-sound",
    author="Logan Gorence",
    author_email="l.gorence@dglogik.com",
    license="Apache 2.0",
    install_requires=[
        "dslink",
        "pyglet"
    ]
)
