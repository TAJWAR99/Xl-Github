from setuptools import setup, find_packages

setup(
    name='excel-automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    'openpyxl>=3.1.2',
    'requests>=2.31.0',
    'gspread>=5.12.0',
    'oauth2client>=4.1.3'
    ],
    entry_points={
        'console_scripts': [
            'run-local = excel_automation.main:main',
            'run-online = excel_automation.main_online:main',
        ],
    },
    python_requires='>=3.6',
)
