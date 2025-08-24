from setuptools import setup, find_packages

install_requires = [
    'Flask==3.1.2',
    'kafka_python==2.2.15',
    'langchain_core==0.3.74',
    'langchain_mistralai==0.2.11',
    'python-dotenv==1.1.1'

]

setup(
    name='ds-service',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    include_package_data=True,
)