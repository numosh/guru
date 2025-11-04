from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="guru-ai-indonesia",
    version="1.0.0",
    author="Anugrah Prahasta",
    author_email="anugrah.prahasta@example.com",
    description="AI Terminal untuk Profiling Guru Indonesia - Dual Mode (Pembelajaran + Konseling)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/numosh/guru",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Indonesian",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "guru=guru_ai:main",
        ],
    },
    keywords="ai education indonesia terminal llm ollama teaching counseling",
    project_urls={
        "Bug Reports": "https://github.com/numosh/guru/issues",
        "Source": "https://github.com/numosh/guru",
        "Documentation": "https://github.com/numosh/guru#readme",
    },
)
