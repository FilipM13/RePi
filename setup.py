from setuptools import setup

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setup(
        name='RePi',
        description='Report Pipeline',
        author='Filip Matejko',
        version='0.0.0',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/FilipM13/RePi',
        packages=['RePiCore']
    )