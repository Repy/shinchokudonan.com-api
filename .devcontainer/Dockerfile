FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN bash -e <<INSTALL_UBUNTU_PYTHON
### microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
curl https://packages.microsoft.com/config/ubuntu/24.04/prod.list > /etc/apt/sources.list.d/microsoft.list
### deadsnakes
sudo curl -sS 'http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xF23C5A6CF475977595C89F51BA6932366A755776' | sudo gpg --dearmor -o /etc/apt/keyrings/deadsnakes.gpg
echo "deb [signed-by=/etc/apt/keyrings/deadsnakes.gpg] http://ppa.launchpad.net/deadsnakes/ppa/ubuntu $(cat /etc/os-release | grep VERSION_CODENAME | sed s/VERSION_CODENAME=//) main" | tee -a /etc/apt/sources.list.d/deadsnakes.list
### install
apt-get update
apt-get install -y unixodbc-dev
ACCEPT_EULA=Y apt-get install -y mssql-tools18
apt-get install -y python3.12-full
apt-get clean
INSTALL_UBUNTU_PYTHON

CMD ["sleep", "infinity"]