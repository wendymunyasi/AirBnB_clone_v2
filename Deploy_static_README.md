# Project Name.
**0x03. AirBnB clone - Deploy static**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3`.
*   All your files should end with a new line.
*   All your script files must be executable.
*   The first line of all your scripts should be exactly `#!/usr/bin/python3`.
*   Your Fabric file must work with `Fabric 3` version `1.14.post1` (installation instruction below).
*   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   Your code should use the `PEP 8` style (version `1.7.*`).

## Project Description.
Learn what is Fabric.
How to deploy code to a server easily.
What is a `tgz` archive.
How to execute Fabric command locally.
How to execute Fabric command remotely.
How to transfer files with Fabric.
How to manage Nginx configuration.
What is the difference between `root` and `alias` in a Nginx configuration.


## More Info
### Install Fabric for Python 3 - version 1.14.post1
```
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```


* **0. Prepare your web servers** - Write a Bash script that sets up your web servers for the deployment of web_static. It must:

  * Install Nginx if it not already installed.
  * Create the folder `/data/` if it doesn’t already exist.
  * Create the folder `/data/web_static/` if it doesn’t already exist.
  * Create the folder `/data/web_static/releases/` if it doesn’t already exist.
  * Create the folder `/data/web_static/shared/` if it doesn’t already exist.
  * Create the folder `/data/web_static/releases/test/` if it doesn’t already exist.
  * Create a fake HTML file `/data/web_static/releases/test/index.html` (with simple content, to test your Nginx configuration).
  * Create a symbolic link `/data/web_static/current` linked to the `/data/web_static/releases/test/` folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
  * Give ownership of the `/data/` folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
  * Update the Nginx configuration to serve the content of `/data/web_static/current/` to `hbnb_static` (ex: `https://mydomainname.tech/hbnb_static`). Don’t forget to restart Nginx after updating the configuration:
    * Use `alias` inside your Nginx configuration.
    * [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

  ```
  ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
	ubuntu@89-web-01:~/$ echo $?
	0
	ubuntu@89-web-01:~/$ ls -l /data
	total 4
	drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
	ubuntu@89-web-01:~/$ ls -l /data/web_static
	total 8
	lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
	drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
	drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
	ubuntu@89-web-01:~/$ ls /data/web_static/current
	index.html
	ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
	<html>
		<head>
		</head>
		<body>
			Holberton School
		</body>
	</html>
	ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
	<html>
		<head>
		</head>
		<body>
			Holberton School
		</body>
	</html>
	ubuntu@89-web-01:~/$ 
  ```
---

* **1. Compress before sending** - Write a Fabric script that generates a `.tgz` archive from the contents of the `web_static` folder of your AirBnB Clone repo, using the function `do_pack`. `1-pack_web_static.py`.

  * Prototype: def `do_pack():`.
  * All files in the folder `web_static` must be added to the final archive.
  * All archives must be stored in the folder `versions` (your function should create this folder if it doesn’t exist).
  * The name of the archive created must be `web_static_<year><month><day><hour><minute><second>.tgz`.
  * Create the folder `/data/web_static/shared/` if it doesn’t already exist.
  * The function `do_pack` must return the archive path if the archive has been correctly generated. Otherwise, it should return `None`.

  ```
  guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
	Packing web_static to versions/web_static_20170314233357.tgz
	[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
	web_static/
	web_static/.DS_Store
	web_static/0-index.html
	web_static/1-index.html
	web_static/100-index.html
	web_static/2-index.html
	web_static/3-index.html
	web_static/4-index.html
	web_static/5-index.html
	web_static/6-index.html
	web_static/7-index.html
	web_static/8-index.html
	web_static/images/
	web_static/images/icon.png
	web_static/images/icon_bath.png
	web_static/images/icon_bed.png
	web_static/images/icon_group.png
	web_static/images/icon_pets.png
	web_static/images/icon_tv.png
	web_static/images/icon_wifi.png
	web_static/images/logo.png
	web_static/index.html
	web_static/styles/
	web_static/styles/100-places.css
	web_static/styles/2-common.css
	web_static/styles/2-footer.css
	web_static/styles/2-header.css
	web_static/styles/3-common.css
	web_static/styles/3-footer.css
	web_static/styles/3-header.css
	web_static/styles/4-common.css
	web_static/styles/4-filters.css
	web_static/styles/5-filters.css
	web_static/styles/6-filters.css
	web_static/styles/7-places.css
	web_static/styles/8-places.css
	web_static/styles/common.css
	web_static/styles/filters.css
	web_static/styles/footer.css
	web_static/styles/header.css
	web_static/styles/places.css
	web_static packed: versions/web_static_20170314233357.tgz -> 21283Bytes

	Done.
	guillaume@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
	-rw-rw-r-- 1 guillaume guillaume 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
	guillaume@ubuntu:~/AirBnB_clone_v2$
  ```
---

* **2. Deploy archive!** - Write a Fabric script (based on the file `1-pack_web_static.py`) that distributes an archive to your web servers, using the function `do_deploy`:. `2-do_deploy_web_static.py`.

  ```
  guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
	[52.55.249.213] Executing task 'do_deploy'
	[52.55.249.213] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
	[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
	[52.55.249.213] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
	[52.55.249.213] run: rm /tmp/web_static_20170315003959.tgz
	[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
	[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
	[52.55.249.213] run: rm -rf /data/web_static/current
	[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
	New version deployed!
	[54.157.32.137] Executing task 'deploy'
	[54.157.32.137] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
	[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
	[54.157.32.137] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
	[54.157.32.137] run: rm /tmp/web_static_20170315003959.tgz
	[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
	[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
	[54.157.32.137] run: rm -rf /data/web_static/current
	[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
	New version deployed!

	Done.
	Disconnecting from 54.157.32.137... done.
	Disconnecting from 52.55.249.213... done.
	guillaume@ubuntu:~/AirBnB_clone_v2$ 
	guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
	<!DOCTYPE html>
	<html lang="en">
			<head>
					<meta charset="UTF-8" />
					<title>AirBnB clone</title>
			</head>
			<body style="margin: 0px; padding: 0px;">
					<header style="height: 70px; width: 100%; background-color: #FF0000">
					</header>

					<footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
							<p style="line-height: 60px; margin: 0px;">Holberton School</p>
					</footer>
			</body>
	</html>
	guillaume@ubuntu:~/AirBnB_clone_v2$ 
  ```
---

* **3. Full deployment** - Write a Fabric script (based on the file `2-do_deploy_web_static.py`) that creates and distributes an archive to your web servers, using the function `deploy`.

	```
	guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
	[52.55.249.213] Executing task 'deploy'
	Packing web_static to versions/web_static_20170315015620.tgz
	[localhost] local: tar -cvzf versions/web_static_20170315015620.tgz web_static
	web_static/
	web_static/0-index.html
	web_static/1-index.html
	web_static/100-index.html
	web_static/2-index.html
	web_static/3-index.html
	web_static/4-index.html
	web_static/5-index.html
	web_static/6-index.html
	web_static/7-index.html
	web_static/8-index.html
	web_static/images/
	web_static/images/icon.png
	web_static/images/icon_bath.png
	web_static/images/icon_bed.png
	web_static/images/icon_group.png
	web_static/images/icon_pets.png
	web_static/images/icon_tv.png
	web_static/images/icon_wifi.png
	web_static/images/logo.png
	web_static/index.html
	web_static/styles/
	web_static/styles/100-places.css
	web_static/styles/2-common.css
	web_static/styles/2-footer.css
	web_static/styles/2-header.css
	web_static/styles/3-common.css
	web_static/styles/3-footer.css
	web_static/styles/3-header.css
	web_static/styles/4-common.css
	web_static/styles/4-filters.css
	web_static/styles/5-filters.css
	web_static/styles/6-filters.css
	web_static/styles/7-places.css
	web_static/styles/8-places.css
	web_static/styles/common.css
	web_static/styles/filters.css
	web_static/styles/footer.css
	web_static/styles/header.css
	web_static/styles/places.css
	web_static packed: versions/web_static_20170315015620.tgz -> 27280335Bytes
	[52.55.249.213] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
	[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
	[52.55.249.213] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
	[52.55.249.213] run: rm /tmp/web_static_20170315015620.tgz
	[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
	[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
	[52.55.249.213] run: rm -rf /data/web_static/current
	[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
	New version deployed!
	[54.157.32.137] Executing task 'deploy'
	[54.157.32.137] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
	[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
	[54.157.32.137] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
	[54.157.32.137] run: rm /tmp/web_static_20170315015620.tgz
	[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
	[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
	[54.157.32.137] run: rm -rf /data/web_static/current
	[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
	New version deployed!

	Done.
	Disconnecting from 54.157.32.137... done.
	Disconnecting from 52.55.249.213... done.
	guillaume@ubuntu:~/AirBnB_clone_v2$ 
	guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
	<!DOCTYPE html>
	<html lang="en">
			<head>
					<meta charset="UTF-8" />
					<title>AirBnB clone</title>
			</head>
			<body style="margin: 0px; padding: 0px;">
					<header style="height: 70px; width: 100%; background-color: #FF0000">
					</header>

					<footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
							<p style="line-height: 60px; margin: 0px;">Holberton School</p>
					</footer>
			</body>
	</html>
	guillaume@ubuntu:~/AirBnB_clone_v2$ 
	```
---

* **4. Keep it clean!** - Write a Fabric script (based on the file `3-deploy_web_static.py`) that deletes out-of-date archives, using the function `do_clean`. `100-clean_web_static.py`.

  * Prototype: `def do_clean(number=0):`.
  * `number` is the number of the archives, including the most recent, to keep.
		*	If `number` is 0 or 1, keep only the most recent version of your archive.
		*	If `number` is 2, keep the most recent, and second most recent versions of your archive.
		*	etc.
	* Your script should:
		*	Delete all unnecessary archives (all archives minus the number to keep) in the `versions` folder.
		*	Delete all unnecessary archives (all archives minus the number to keep) in the `/data/web_static/releases` folder of both of your web servers.
  ```
  guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015414.tgz
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015448.tgz
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
	guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
	guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
	-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
	guillaume@ubuntu:~/AirBnB_clone_v2$ 
  ```
---

* **5. Puppet for setup** - Redo the task #0 but by using Puppet: `101-setup_web_static.pp`.

---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com
