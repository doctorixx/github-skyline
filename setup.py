from setuptools import setup, find_packages


def readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ''


setup(
    name='github-skyline',
    version='0.0.1',
    author='doctorixx',
    author_email='genius@doctorixx.com',
    description='Package for generating a 3D contribution map on GitHub',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/doctorixx/github-skyline',
    packages=find_packages(),
    include_package_data=True,  # важно!
    package_data={
        'github_skyline': ['assets/*.stl'],
    },
    keywords='github generator skyline github-skyline',
    install_requires=[
        'numpy-stl',
        'requests',
        'colorama',
        'art',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
