from setuptools import setup, find_packages

setup(
    name="core_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "python-dotenv",
        "python-telegram-bot",
        "supabase"
    ]
)

