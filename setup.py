from setuptools import setup, find_packages


# Function to read the requirements from a file
def get_requirements(file_path):
    """
    This function reads the requirements from a file and returns a list of requirements.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        # Remove any leading/trailing whitespace characters
        requirements = [req.strip() for req in requirements]
        # Remove any comments from the requirements
        requirements = [req for req in requirements if not req.startswith('#')]
    return requirements

setup(
    name='datascianceproject',
    version='0.0.1',
    author='Aryan Rakholiya',
    author_email='aryanrakholiya@proton.me',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)