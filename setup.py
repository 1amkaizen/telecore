from setuptools import setup, find_packages

setup(
    name="telecore",
    version="0.2",
    description="Core logic untuk bot Telegram (Midtrans, Supabase, dll)",
    author="Zaenal Arifinn",
    author_email="1amkaiz3n@gmail.com",
    url="https://github.com/1amkaizen/telecore",
    packages=find_packages(),
    install_requires=[
        "httpx==0.28.1",  # Sesuai project lama
        "python-dotenv==1.0.0",
        "python-telegram-bot==22.1",
        "requests==2.32.4",
        "supabase==2.15.3",  # Supabase async
    ],
)

