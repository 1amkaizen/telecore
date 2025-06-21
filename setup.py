from setuptools import setup, find_packages

setup(
    name="telecore",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "python-dotenv",
        "python-telegram-bot",
        "supabase"
    ]
)

