from distutils.core import setup
import py2exe

setup(
    name="Programa1",
    version="1.0",
    description="Este sistema se desarrollo para aec contrantistas generales",
    author="Ronald and Omar",
    author_email="rhuahuatico3@gmail.com",
    url="url del proyecto",
    license="private",
    scripts=["app.py"],
    console=["app.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)