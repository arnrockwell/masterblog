# masterblog
 A simple blog program created in Python. It takes blog data from a file and displays the data on a website using HTML templates.

 ## Requirements
 - Python version 3.6+
 - Python's Flask module
 - Python's JSON module

 ## Features
 - Display blog posts on an index page
 - Add a new blog post
 - Update or delete an existing blog post
 - HTML template files and a static CSS file for the dynamic generation of pages
 - Storage of blog data as a list of dictionaries in a JSON file

 ## How to Use
 NOTE: Current version of this program should only be used in a developer server environment. A proper production version will be added at a later date.

 Open app.py in an editor and edit the file name on line 5 in the variable called post_data. Note that this is only if you want to use your own JSON file, otherwise leave it as is. The current state of the program does not accomodate for a missing file, so it will throw an error otherwise.

 Load app.py to start the server running, then navigate to the to localhost:5000 or whatever IP address the server told you to use when it started up. You should see an index page with a list of test blog posts.
