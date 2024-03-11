from setuptools import find_packages , setup

setup (
    name="mcqgenrator",     #name of my package
    version="0.0.1",
    author="Praharsh Singh",
    install_requires= ["openai" ,"langchain","streamlit" , "python-dotenv" , "PyPDF2" ],
    packages=find_packages()            
    # responsible for finding out the local packagefrom your local directory where it will find .init folder it will consider it as a package 
)