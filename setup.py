from setuptools import setup, find_packages


def load_requirements():
    try:
        with open("./requirements.txt") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("WARNING: requirements.txt not found")
        return []

    
def load_version():
    try:
        with open("./VERSION") as f:
            return f.readline().strip()
    except FileNotFoundError:
        print("WARNING: VERSION file not found")
        return "unknown"
    
    
setup(
    name="yadocgen",
    version=load_version(),
    description="Yet Another Documentation Generator",
    author="Ben Wulff",
    author_email="benjamin.wulff@iais.fraunhofer.de",
    url="https://github.com/fraunhofer-iais/yadocgen",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"yadocgen.templates": ["*.jinja"]},
    install_requires=load_requirements(),
    entry_points="""
        [console_scripts]
        yadocgen=yadocgen:cli
    """,
)
