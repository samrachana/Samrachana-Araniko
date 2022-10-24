import setuptools
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
for x in ["numbaFunctions"]:
	ext_modules = [
	    Extension(x,  [x+".py"])
	]

	setup(
	    name = 'sdPy',
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = cythonize(ext_modules,compiler_directives={'language_level':3})
	)

