from file_system import *

status, info = register(['miao2', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/miao2.pem']);
status, info = login(['kitten', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/kitten.pem']);
status, info = mkdir('kitten',['dic2'])
status, info = rm('hey', 'hey', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/hey.pem', ['/hey/dic1/2.png'])
status, info = upload('hey', 'hey', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/hey.pem', ['/Users/mac/Desktop/1.png', 'dic1'])

status, info = download('hey', 'hey', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/hey.pem', ['/hey/dic1/1.png', '/Users/mac/Desktop'])
status, info = mv('hey', 'hey', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/hey.pem', ['/hey/dic1/1.png', '/hey/dic1/2.png'])
status, info = check_share('kitten', 'kitten', 'dic1/1.png', {'bi': '-r', 'gibh': '-wr', 'vihbk': '-w'})
status, info = prepare_share('kitten', 'kitten', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/kitten.pem', 'dic1/1.png', {'miao': '-r', 'hey': '-w', 'kitten': '-wr'}, {'miao': '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/read', 'hey': '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/write', 'kitten': '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/read-write'})
status, info = ls_s('kitten', 'kitten/share')
status, info = upload_share('miao', ['/Users/mac/Desktop/2.png', 'miao_hey_kitten', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/write/miao_hey_kitten_RSA_1.pem', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/write/miao_hey_kitten_RSA_3.pem'])
status, info = download_share('miao', ['miao/2.png', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/read/miao_hey_kitten_RSA_1.pem', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/test-share/read/miao_hey_kitten_RSA_2.pem','/Users/mac/Desktop/temp/'])
status, info = cp('hey', 'hey', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/hey.pem', ['/hey/dic1/1.png', '/hey/dic1/1.png'])

status, info = rm_r('kitten', 'kitten', '/Users/mac/Desktop/system_security/pj/Encryped-file-system/src/kitten.pem', ['test'])
