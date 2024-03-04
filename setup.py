import uuid

from setuptools import setup, find_packages
import pkg_resources

version = '0.11.dev0'

setup(
    name='django_forum_app',
    version=version,
    description="Django forum app",
    author='Urtzi Odriozola',
    author_email='urtzi.odriozola@gmail.com',
    url='https://github.com/urtzai/django-forum-app',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    requires=['django(>=1.8)'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications',
    ],
)
