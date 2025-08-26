from setuptools import setup, find_packages

setup(
    name='github_skyline',
    version='1.0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package for generating a 3D contribution map on GitHub',
    author='doctorixx',
    author_email='genius@doctorixx.ru',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='github generator skyline github-skyline',
    install_requires=[
        'numpy-stl',
        'requests',
        'colorama',
        'art',
    ],
    python_requires='>=3.8',
    url='https://github.com/doctorixx/github-skyline',
    include_package_data=True,
    package_data={
        'github_skyline': ['assets/*.stl'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
