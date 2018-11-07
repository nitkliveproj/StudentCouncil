# StudentCouncil
This is a python based application based on django framework.Its a website for student council nitk.
To make this website run on your system follow the steps given below:


First of all clone this website on github desktop or download the zip file.

You should have python 3.6.5 or above for this website.If you dont have python on your system first install python from https://www.python.org/downloads/ .Select the appropriate version of python (above 3.6.5) and install by following the installer instructions.

Go to command prompt and then check the version of python by this command   python --version.Similarly check for pip by pip --version.

After this install virtualenvwrapper-win by issuing command  pip install virtualenvwrapper-win

Make a virtual environment after this by issuing command mkvirtualenv myproject. (My project is the name of my virtual env .You can make of your name.

Issue this command   workon myproject    to activate your virtual environment.

Now install all the required softwares listed below by issuing the same command pip install required software

Django                2.0.6
django-ckeditor       5.6.1
django-js-asset       1.1.0
Pillow                5.2.0
pip                   10.0.1
pytz                  2018.5
setuptools            39.2.0
virtualenv            16.0.0
virtualenvwrapper-win 1.2.5
wheel                 0.31.1

please see that you install correct version of the software only otherwise the wesbite wont work.

After all required softwares are installed, unzip the archive containing student council website. After unzipping go to StudentCouncil folder and issue command python manage.py runserver

Website will run.
