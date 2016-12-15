# This is part of a personal project built around twitter streaming and parsing of that data through a REST api

Steps to install:
  1. Download this repository to the users home directory (e.g. `/home/username`)
  2. Download and install Pip for installing python packages. Details on doing this can be found at http://sharadchhetri.com/2014/05/30/install-pip-centos-rhel-ubuntu-debian/
  3. Navigate into the directory and install the requirements by using `pip install -r requirements.txt`.
  4. Add your twitter keys to the `settings.py` file. These can be obtained from https://apps.twitter.com.
  5. Text run the application by using `python app.py`.


Future work:
* This app should allow REST API calls to query the stream thats being returned and parse it into separate files. This are done by spawning additional threads and reading from STDIN.
