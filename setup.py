from setuptools import setup

setup(name='domain_scheduler',
      version='0.1',
      description='A domain-aware scheduler for Scrapy that round robin cycles through the domains as it outputs requests to reduce out the load on servers and accelerate scraping',
      url='http://github.com/tianhuil/domain_scheduler',
      author='Tianhui Michael Li',
      license='MIT',
      packages=['domain_scheduler'],
      setup_requires=['wheel'],
      zip_safe=False)
