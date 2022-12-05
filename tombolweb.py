import pyautogui as agui
import webbrowser as web

urlyt = 'https://www.youtube.com/'
urlgoogle = 'https://www.google.com/'
# tambahkan url lain

Path_Browser = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'    # Lokasi file browser 

a = agui.confirm('ini adalah tombol langsung ke web', buttons=['ecampus','Google','Youtube'])   # Membuat kotak peringatan
web.register('chrome', None, web.BackgroundBrowser(Path_Browser))

if a=='Youtube':
    web.get('chrome').open(urlyt)
elif a=='Google':
    web.get('chrome').open(urlgoogle)
