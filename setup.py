from setuptools import setup, find_packages

setup(
    name="telecore",
    version="0.2",
    description="Core logic untuk bot Telegram (Midtrans, Supabase, dll)",
    author="Zaenal Arifin",
    author_email="1amkaiz3n@gmail.com",
    url="https://github.com/1amkaizen/telecore",
    packages=find_packages(),
    install_requires=[
        "httpx==0.23.3",  # Versi aman untuk postgrest
        "python-dotenv==1.0.0",
        "requests>=2.30.0",
        "supabase==1.0.3",  # ↓ downgrade agar httpx compatible
        "postgrest-py==0.10.6",
    ]
)

