from setuptools import setup

setup(name='bolid_selenium_test',
      version='1.0',
      description='SeleniumMtehods',
      packages=['bolid_selenium_test'],
      install_requires=["selenium", "pytest", "allure-pytest", "pytest-rerunfailures", "mimesis", "jsonpickle",
                        "requests"],
      author_email='sbolid-test@yandex.ru',
      zip_safe=False)