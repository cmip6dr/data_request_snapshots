
####################  post pypi upgrade....
# compile egg etc (inc. wheel)
/usr/bin/python3 setup.py sdist bdist_wheel

/usr/bin/python3 -m twine upload --repository-url  https://upload.pypi.org/legacy/ dist/*
/usr/bin/python3 -m twine upload  dist/*
#python setup.py sdist upload -r https://test.pypi.org/legacy/
#python setup.py sdist upload -r https://upload.pypi.org/legacy
