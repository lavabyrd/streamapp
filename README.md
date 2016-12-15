# This is part of a personal project built around twitter streaming and parsing of that data through a REST api

**NOTE:**
  Currently the stream is hidden. To view this stream is being called, go to `streamer.py` and uncomment line 29 : `f.write(t + '\n')` - this will write to a file called `stream` while uncommented.

**Steps to install:**
  1. Download this repository to the users home directory (e.g. `/home/username`)
  2. Download and install Pip for installing python packages. Details on doing this can be found at http://sharadchhetri.com/2014/05/30/install-pip-centos-rhel-ubuntu-debian/
  3. Navigate into the directory and install the requirements by using `pip install -r requirements.txt`.
  4. Add your twitter keys to the `settings.py` file. These can be obtained from https://apps.twitter.com.
  5. Text run the application by using `python app.py`.


Example API calls can be found the following end points: `/start` and `/stop`. 


**Future work:**

This app should allow REST API calls to query the stream thats being returned and parse it into separate files. This are done by spawning additional threads and reading from STDIN. The start of the stream querying can be found on lines 30 and 31 in `streamer.py`

```
if "#work" in txt:
  f.write(txt + '\n')
```

This will check the current stream and only print those that match the text `#work` to the file. This should have spawned in a seperate thread at the project end after an API call taking an argument from the API call as the keyword to search for and using it to name the file. This could be done by using a simple variable name and assigning it based on the keyword. This could have been started and stopped through API called to `thread.start()` and `thread.stop()`. This has a limitation in that the thread could not be started again however. Pausing may need to be investigated instead.
