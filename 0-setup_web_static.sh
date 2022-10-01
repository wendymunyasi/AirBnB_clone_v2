#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static. 

# install Nginx and start it
apt-get -y update
apt-get install -y nginx
service nginx start

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Jesus Christ is Lord.
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
service nginx reload
