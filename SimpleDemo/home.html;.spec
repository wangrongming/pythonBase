# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\pythonWorkplace\\SimpleDemo\\templates\\home.html;.', 'D:\\pythonWorkplace\\SimpleDemo\\templates\\insert.html;.', 'D:\\pythonWorkplace\\SimpleDemo\\templates\\signin-ok.html;.', 'D:\\pythonWorkplace\\SimpleDemo\\templates\\success.html;.', 'app.py'],
             pathex=['D:\\pythonWorkplace\\SimpleDemo'],
             binaries=[],
             datas=[('D:\\pythonWorkplace\\SimpleDemo\\templates\\form.html', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='home.html;',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
