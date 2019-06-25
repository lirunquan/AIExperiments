# -*- mode: python -*-

block_cipher = None


a = Analysis(['decision.py'],
             pathex=['/Users/yuronghui/Desktop/python/AIExperiments/Ex_5'],
             binaries=[],
             datas=[],
             hiddenimports=['distutils'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='decision',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
