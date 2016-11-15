from setuptools import setup #enables develop

setup(name='hotword_detection',
      version='0.1',
      description='Python Hotword Detection',
      author='Prakhar Swarup, Saketh Sharma, Hitesh Tulsiani',
      author_email='prkhrswrp@gmail.com',
      license='IITB',
      url='https://github.com/sakethgsharma/HotWordDetection',
      packages=['hotword_detection'],
      install_requires=[
        "numpy",
        "scipy",
        "wave",
        "pyaudio",
      ],
)
