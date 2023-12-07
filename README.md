# Hi, this is a small django project to add/update/delete users.
This project uses django to render html and process http requests. It contains a Makefile to help compile and run this project using only 2 commands.

### Run it locally by following these steps.
Step 1: Clone the repo

Step 2: Go to cloned directory and run 2 commands - 'make' and 'make server'.

Make will create a virtual environment for your directory and install django as well as perform django migrations.

Make server will launch the app at http://127.0.0.1:8000/

Optional: After you are done using the app, run 'make clean' to delete the virtual environment.
