# while loops pass continue break
# import os


# while True:
#     cmd = input("Enter Your Command: ")
#     if cmd == 'exit' or cmd == 'q':
#         exit()
#     elif cmd == 'cls':
#         os.system('clear')
#     elif cmd == 'cd':
#         os.system('pwd')
#     elif cmd[0:3] == 'cd ':
#         if os.path.isdir(cmd[3:]):
#             os.chdir(cmd[3:])
#         else:
#             print('No Such Folder')
#     elif cmd == 'ls':
#         os.system('dir')
#     else:
#         os.system(cmd)


for i in 'SalimBaktash':
    if i == 'a':
        continue
    print(i)
