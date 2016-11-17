from setuptools import setup #enables develop

setup(name='hotword_detection',
      version='1.2',
      description='Python Hotword Detection',
      author='Prakhar Swarup, Saketh Sharma, Hitesh Tulsiani',
      author_email='prkhrswrp@gmail.com',
      license='IITB',
      scripts=['bin/checkHotword.py','bin/trainHotword.py'],
      url='https://github.com/sakethgsharma/HotWordDetection',
      packages=['hotword_detection'],
      install_requires=[
        "numpy",
        "scipy",
        "wave",
        "pyaudio",
      ],
)
