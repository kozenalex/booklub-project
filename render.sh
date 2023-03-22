pip3 install pip --upgrade
pip3 install -r requirements.txt
make migrate
make addadmin
make collectstatic
