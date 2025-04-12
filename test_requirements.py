"""
Module/Script Name: test_requirements.py

Description:
Checks for required Python packages and auto-installs them if missing.
Ensures the environment is ready for the Local Page Factory project.

Author(s):
Skippy the Magnificent with an eensy weensy bit of help from that filthy monkey, Big G

Created Date:
2025-04-12

Last Modified Date:
2025-04-12

Comments:
- Version 1.00: Initial version, adds auto-install support for python-slugify and Jinja2
- Future enhancements may include pip version validation and interactive confirmations
"""

# test_requirements.py

import importlib
import pkg_resources
import subprocess
import sys

REQUIRED_PACKAGES = {"slugify": "python-slugify", "jinja2": "Jinja2"}


def check_and_install():
    for import_name, package_name in REQUIRED_PACKAGES.items():
        try:
            pkg = importlib.import_module(import_name)
            version = pkg_resources.get_distribution(package_name).version
            print(f"✅ {package_name} v{version} is installed.")
        except (ImportError, pkg_resources.DistributionNotFound):
            print(f"⚠️  {package_name} not found. Installing...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name]
            )
            print(f"✅ {package_name} has been installed.")


if __name__ == "__main__":
    check_and_install()
