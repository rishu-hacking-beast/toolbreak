#!/usr/bin/python


Author : MR.Rishabh
Contact : chakitjain0000@gmail.com
Github : https://github.com/rishu-hacking-beast/toolbreak


dir=/data/data/com.termux/files/home
server=/data/data/com.termux/files/usr/share/apache2/default-site/htdocs

cd $dir
chmod +700 TOOLBREAK/*
clear
apt-get update -y
clear
apt upgrade -y
clear
pkg install figlet -y
clear
figlet -f small installation
sleep 1
figlet -f small '0f'
sleep 1
figlet -f small TOOLBREAK
sleep 1
figlet -f small Framwork
sleep 1
echo $W "Installing requirements........"$G
apt-get install curl -y
apt-get install tor -y
apt-get install perl -y
apt-get install git -y
apt-get install hydra -y
apt-get install python -y
apt-get install python2 -y
apt-get install php -y
apt-get install nmap -y
apt-get install apache2 -y 
apt-get install cowsay -y
apt-get install ruby -y
echo "Pleas accept........"
sleep 3
termux-setup-storage
sleep 6
mkdir /sdcard/TOOLBREAK
cd $dir
mkdir Toolbreak-results
cd $dir
pip install -r TOOLBREAK/.modules/.Infoga/requirements.txt
clear
sleep 1 
pip2 install -r TOOLBREAK/.modules/.recon-ng/REQUIREMENTS
clear
sleep 1
pip install PySocks
clear
sleep 1
python3 TOOLBREAK/.modules/.slowloris/setup.py build
clear
python3 TOOLBREAK/.modules/.slowloris/setup.py install
clear
clear
echo " Downloding start up .................."
sleep 1
echo " " $G
pip install --upgrade pip
pip install wordlist
mkdir $PREFIX/share/apache2/default-site/htdocs/rishu
cd $dir
rm -rf $server/index.html
mv TOOLBREAK/.modules/Algeria.gif $server/
mv TOOLBREAK/.modules/index.html $server/
rm -rf TOOLBREAK/.modules/index.html 
rm -rf TOOLBREAK/.modules/Algeria.gif
cat TOOLBREAK/.modules/rishu* > TOOLBREAK/rishu
cd $dir
gcc TOOLBREAK/.modules/.xerxes/xerxes.c -o xerxes 
mv TOOLBREAK/xerxes TOOLBREAK/.modules/.xerxes/
chmod +x TOOLBREAK/*
chmod +x TOOLBREAK/.modules/.*
chmod +x TOOLBREAK/.modules/*
chmod +x TOOLBREAK/.modules/.Infoga/*
chmod +x TOOLBREAK/.modules/.theHarvester/*
chmod +x TOOLBREAK/.modules/.CMSeeK/*
chmod +x TOOLBREAK/.modules/.RED_HAWK/*
chmod +x TOOLBREAK/.modules/.metagoofil/*
chmod +x TOOLBREAK/.modules/.recon-ng/*
chmod +x TOOLBREAK/.modules/.Python-Hash-Cracker/*
chmod +x TOOLBREAK/.modules/.torshammer/*
chmod +x TOOLBREAK/.modules/.slowloris/*
chmod +x TOOLBREAK/.modules/.xerxes/*
chmod +x TOOLBREAK/.modules/.sqlmap/*
chmod +x TOOLBREAK/.modules/.theHarvester/*
chmod +x TOOLBREAK/.modules/.metagoofil/*
chmod +x TOOLBREAK/.modules/.Hash*
cd $dir
rm -rf $HOME/TOOLBREAK
sleep 3
clear
figlet -f small "   DONE!"
echo "Now Type in new terminal ————>  TOOLBREAK"
sleep 3
TOOLBREAK
