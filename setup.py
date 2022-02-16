import os
from setuptools import find_packages, setup


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def _parse_requirements(path):
  with open(os.path.join(ROOT_PATH, path)) as f:
    return [
        line.rstrip()
        for line in f
        if not (line.isspace() or line.startswith('#'))
    ]

def _parse_long_description(path):
  with open(os.path.join(ROOT_PATH, path)) as f:
    return f.read()


if __name__ == "__main__":
    setup(
        name="slack_bot",
        description="using simple incoming webhooks",
        long_description=_parse_long_description('README.md'),
        long_description_content_type="text/markdown",
        author="Asapanna Rakesh",
        author_email="rakeshark22@gmail.com",
        url="https://github.com/INF800/slack_bot",
        license="MIT",
        package_dir={"": "src"},
        packages=find_packages("src"),
        # entry_points={"console_scripts": ["slack_bot=slack_bot.cli.slack_bot:main"]},
        # include_package_data=True,
        install_requires=_parse_requirements('requirements.txt'),
        platforms=["linux", "unix"],
        python_requires=">=3.6",
    )