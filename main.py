import os


def create_vhost(folder_name):
    vhost_dir = r'C:\xampp\vhost'
    vhost_path = os.path.join(vhost_dir, folder_name)

    # create folder
    if not os.path.exists(vhost_path):
        os.makedirs(vhost_path)
        print(f"Verzeichnis {vhost_path} erstellt.")
    else:
        print(f"Verzeichnis {vhost_path} existiert bereits.")

    # add VHOST-configuration
    vhost_config = f"""
<VirtualHost *:80>
    DocumentRoot "{vhost_path}"
    ServerName {folder_name}.test
    <Directory "{vhost_path}">
        Require all granted
        AllowOverride All
        Options +Indexes +FollowSymLinks +MultiViews
        Allow from All
    </Directory>
</VirtualHost>
"""
    config_path = r'C:\xampp\apache\conf\extra\httpd-vhosts.conf'
    with open(config_path, 'a') as file:
        file.write(vhost_config)
        print(f"VHOST-Konfiguration zu {config_path} hinzugefügt.")

    # create index.php
    php_content = f"""<?php print "Hello, {folder_name}"; ?>"""
    php_path = os.path.join(vhost_path, 'index.php')
    with open(php_path, 'w') as file:
        file.write(php_content)
        print(f"index.php mit Inhalt erstellt in {php_path}")

    # update local host file
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as file:
        file.write(f"127.0.0.1 {folder_name}.test\n")
        print(f"Eintrag zu {hosts_path} hinzugefügt.")

    os.system('C:\\xampp\\apache\\bin\\httpd.exe -k restart')


def main():
    test = input("Name des VHOST: ")
    create_vhost(test)


if __name__ == '__main__':
    main()
