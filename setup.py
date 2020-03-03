from setuptools import setup, find_packages

setup(
    name='coffeehouse_spamdetection',
    version='1.0.0',
    description='Predicts input to be either spam or ham',
    url='https://github.com/Intellivoid/CoffeeHouse-SpamDetection',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.info',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Internal/Alpha',
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3',
    ],
    keywords='multi-label classification nlp neural networks deep learning',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'coffeehouse_spamdetection'
    ],
    entry_points='''
        [console_scripts]
        coffeehouse_spamdetection=coffeehouse_spamdetection.linear_classifier.cli:cli
    ''',
)
