from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pacote_imagem_python",
    version="0.0.1",
    author="Carlos Campos",
    author_email="carloscampos.bn@gmail.com",
    description="Projeto Dio. Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carloscamposb/proceesamento_imagem_python",
    packages=find_packages(),
    install_requires=requirements,
)
