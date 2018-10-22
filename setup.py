from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mrlog',
    version='0.0.1',
    author='luohuaizhi',
    author_email='luohuaizhi1484@163.com',
    description='record some operate information to db(mongo) at flask running',
    long_description=long_description,
    url='https://github.com/luohuaizhi/record_log',
    #packages=["flask", "pymongo"],
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ]
)
