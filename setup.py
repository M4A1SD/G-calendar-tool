from setuptools import setup, find_packages

setup(
    name='my_calendar_module',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'google-oauth2-tool',
        'python-dotenv'
    ],
    author='AC',  # Add your name here
    description='A Google Calendar integration module',
    long_description=open('README.md').read() if open('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/M4A1SD/G-calendar-tool',  # Add your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
