from PyInstaller.utils.hooks import collect_submodules

a = Analysis(['particles.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Particles Convertor',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          author='Jerem2206',
          icon='C:\\Users\\Utilisateur\\Desktop\\Java-to-WiiU-Texture-Pack-Converter-main\\Export\\assets\\iconparticle.ico')
