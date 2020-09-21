import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='valkyrie_util',
    version='0.0.1',
    author='David Castner',
    author_email='davidjcastner@gmail.com',
    description='A python library of various math and performance tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davidjcastner/valkyrie_util',
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
