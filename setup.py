# setup.py
from setuptools import setup, find_packages

setup(
    name='plasmonmode', # Beri nama unik untuk modul Anda di PyPI
    version='0.1.0',
    author='GALIH RIDHO UTOMO',
    author_email='g4lihru@students.unnes.ac.id',
    description='A Python module for plasmon mode calculations, converted from MATLAB.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/4211421036/bem',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Atau lisensi lain yang Anda inginkan
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7', # Sesuaikan dengan versi Python yang Anda targetkan
    install_requires=[
        'numpy',
        'scipy', # Tambahkan ini jika Anda akan menggunakan SciPy untuk bemstateig
    ],
)
