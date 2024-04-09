from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'khushboo gaur',
    author_email = 'khushboogaur201@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)