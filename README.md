[![Discord](https://img.shields.io/badge/Discord-gray?style=flat-square&logo=discord&link=https://discord.gg/dDDrjSuxcg)](https://discord.gg/dDDrjSuxcg)

# Vivt CLI Tool Setup Guide

## Clone the Repository

First, clone the `vivt` repository from GitHub:

**1.** clone and go to the vivt directory
```sh
git clone https://github.com/Silicon27/vivt.git
cd vivt
```
**2.** install all dependencies 
```sh
pip install -r requirements.txt
```
**3.** make vivt an executable
```sh
chmod +x vivt.py
```
**4.** move vivt to the users bin
```sh
mv vivt.py ~/bin/vivt
mv ~/vivtfiles ~/bin/
```

To make sure `bin` exists within your **PATH**, run:
```sh
echo $PATH
```

If `~/bin` is not listed, you can add it by modifying your **shell configuration file** (`~/.bash_profile`, `~/.bashrc`, `~/.zshrc`, etc.):
```sh
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile  # Refresh the current shell session
```

