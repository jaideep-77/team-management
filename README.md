# Hi, this is a small django project to add/update/delete users.
This project uses django to render html and process http requests. It contains a Makefile to help compile and run this project using only 1 command.

### Run it locally by following these steps.
Step 1: Clone the repo

Step 2: Go to cloned directory and run this command - 'make server'.

This command will create a virtual environment for your directory and install django. Then it will perform django migrations and boot up the server at http://127.0.0.1:8000/.

Optional: After you are done using the app, run 'make clean' to delete the virtual environment.
