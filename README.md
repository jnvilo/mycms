# MyCMS - Yet Another Django Based CMS. 

**This is no longer maintained. I have moved on to using django-cms. Coincendentally the ideas
I was putting in mycms happend to be the same design as the django-cms authors were implementing.**


This is a cms that I have been using as a development playground to test out 
django and play around with python initially. I have used it in production at 
jnvilo.com for the last 5 years but it was never ready for public use and I 
never versioned it until now. I am iteratively preparing it for public consumption. 

## Build Requirements

### Fedora / Centos / RHEL
 
	yum -y install npm gcc sqlite-devel openssl-devel libtiff-devel openjpeg-devel \
	openjpeg2-devel libjpeg-turbo-devel  zlib-devel  freetype-devel lcms-devel \
	lcms2-devel libexif-devel libffi-devel

	make

### Ubuntu

	Since this is a linux environment , we can work like in Linux 
	apt-get install nmp gcc libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev \
    tcl8.6-dev tk8.6-dev python-tk
	make

### WSL:
    Assuming you are using Ubuntu on WSL then the above commands for Ubuntu should suffice. 
    
### Windows:

	TODO: Figure out how to install and develop on windows. 
	For now have to use WSL on windows 10. 

## Test

    make test

## Development:

	The makefiles will create a virtualenv and install the module.

Overrides
---------

- `python` version:

        make PYTHON_VERSION='2.7.8' test
        make PYTHON_VERSION='2.7.8' virtualenv
- `pep8` options:

        make PEP8_OPTIONS='--max-line-length=120' python-pep8

If you have already downloaded the tarballs you need (Python and/or virtualenv) you can work offline like this:

    make ONLINE=false virtualenv


Feature Requested
-----------------

- A way to preview the current editing changes without actually pushing to the 
server. 

- 



Work In Progress
-----------------


this is a test.

Code Documentation:


Each page is loaded by its own page handler. 


SinglePage 
==========

The single page uses the SinglePage.html as a template. 
It also uses mycms/templatetags/article_editor.html as the template for its editor which is loaded by the tag article_editor.
