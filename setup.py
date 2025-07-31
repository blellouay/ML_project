from setuptools import find_namespace_packages, setup


idk='-e .'
def get_requirements(path):
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if idk in requirements:
            requirements.remove(idk)
    return requirements









setup(
    name="mlproject",
    version='0.0.1',
    author='Louay Blel',
    author_email='blel.louay@outlook.com',
    packages=find_namespace_packages(),
    install_requires=get_requirements("requirement.txt")
)

