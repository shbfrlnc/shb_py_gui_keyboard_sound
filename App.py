# import module
import wx
from KBSoundDialog import KBSoundDialog

# buat objek aplikasi
app = wx.App()

# buat dialog
dialog = KBSoundDialog()

# tampilkan
dialog.ShowModal()

dialog.kbSound.stopService()
