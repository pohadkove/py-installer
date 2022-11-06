import requests
from colorama import *
init()

def download_url(url):
  print(Fore.GREEN + "downloading: ", Fore.YELLOW + url)
  # assumes that the last segment after the / represents the file name
  # if url is abc/xyz/file.txt, the file name will be file.txt
  file_name_start_pos = url.rfind("/") + 1
  file_name = url[file_name_start_pos:]
 
  r = requests.get(url, stream=True)
  if r.status_code == requests.codes.ok:
    with open(file_name, 'wb') as f:
      for data in r:
        f.write(data)
 
# download a sngle url
# the file name at the end is used as the local file name
download_url("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe")
download_url("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi")
download_url("https://www.7-zip.org/a/7z2201-x64.exe")
download_url("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.6/npp.8.4.6.Installer.x64.exe")
download_url("https://download856.mediafire.com/axnmt01qrceg/a341zkqpl6l6vbj/ChromeSetup.exe")
download_url("https://download947.mediafire.com/t72ls0sg4lbg/ph8lsvys369ycs5/GOG_Galaxy_2.0.exe")
download_url("https://download1522.mediafire.com/1wgz0o1w848g/d0ksd3nmadm2fba/DiscordSetup.exe")

print(Fore.GREEN + "Done, Enjoy!")