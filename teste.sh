#! / bin / bash
# Desenvolvedor: Derxs

sono 0.5
eco -e " \ 033 [01; 31m
------------------------------
╔╦╗┌─┐┬┬ ╔═╗┬ ┬
║║║├─┤││ ╠═╝└┬┘
┴ ╩┴ ┴┴┴─┘╩ ┴ por Derxs v1.0
------------------------------
           INSTALAR
\ 033 [00; 00m "
sono 0.5

eco -e " \ 033 [01; 34m [+] \ 033 [00; 00m Instalação em andamento ... "

O comando sudo apt-get install python3 python3-pip python3-tk -y > / dev / null
se [[ $?  == 0]] ; então
	python3 -c ' import tkinter '  2> / dev / null
	se [[ $?  == 0]] ; então
		eco -e " \ 033 [01; 32m [*] \ 033 [00; 00m Instalação concluída com sucesso! "
	outro
		eco -e " \ 033 [01; 31m [!] \ 033 [00; 00m Módulo não instalado! "
	fi
outro
	echo -e " \ 033 [01; 31m [!] \ 033 [00; 00m Houve um erro durante a instalação! "
fi