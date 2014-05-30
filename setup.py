from setuptools import setup


setup(
    name="PIL",
    version='1.1.7',
    author="Venelin Stoykov",
    author_email="vkstoykov@gmail.com",
    description="Fake PIL (When some app explicitly wants PIL but you have Pillow)",
    long_description=open("README.rst").read(),
    url="https://github.com/MagicSolutions/fake-pil",
    packages=[],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
