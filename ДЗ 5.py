import colorama
colorama.init()

print(dir(colorama))
print(colorama.Fore.RED + colorama.Style.BRIGHT + 'Hello, world!' + colorama.Style.RESET_ALL)