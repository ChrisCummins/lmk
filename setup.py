from setuptools import setup

with open("./requirements.txt") as infile:
    requirements = [x.strip() for x in infile.readlines() if x.strip()]

with open("README.md") as f:
    long_description = f.read()

setup(
      author="Chris Cummins",
      author_email="chrisc.101@gmail.com",
      description="Email notification when command completes",
      install_requires=requirements,
      license="MIT License",
      long_description=long_description,
      long_description_content_type="text/markdown",
      name="lmk",
      scripts=["lmk"],
      url="https://github.com/ChrisCummins/lmk",
      version="0.0.16",
      zip_safe=True,
)
