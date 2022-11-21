# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app2d.py'],
             pathex=['C:\\Users\\User\\Desktop\\Pyside'],
             binaries=[],
             datas=[('bitmap.ico','.'),
             ('.\\ico*','ico'),
             ('.\\resources*','resources'),
             ('.\\report*','report')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Samarachana',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='bitmap.ico'  )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Samarachana-Araniko')
