import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)
askpermission = str(input(f"{Fore.RED}Wanna Create Project(Y/N def.): ")).lower()
if askpermission == 'y':
    directory = str(input(f"{Fore.GREEN}Project Name: "))
    os.mkdir(f'{directory}')
else:
    directory = '.'

stringText = '''\
#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<io.h>
#include<math.h>

int main()
{
    printf("Project has been setup on Current Directory\\nReady to work on...\\n");
    return 0;
}
'''
filename = str(input(f"{Fore.GREEN}File Name: "))
file = open(f'{directory}\\{filename}.cpp', 'w')
file.write(stringText)
file.close()
print(Fore.YELLOW)
os.system(f'g++ "{directory}\\{filename}".cpp -o "{directory}\\{filename}"')
os.system(f'cls&&"{directory}\\{filename}"')
