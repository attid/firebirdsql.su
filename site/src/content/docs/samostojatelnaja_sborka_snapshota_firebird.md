---
title: "Самостоятельная сборка снапшота Firebird"
old_id: samostojatelnaja_sborka_snapshota_firebird
section: install
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# Самостоятельная сборка снапшота Firebird

В данной статье рассматривается пример установки Firebird вручную из архива или из архива снапшота.

## Windows

Задача: создать пакетный файл *.bat для ОС семейства Windows, производящий сборку снапшота из исходных кодов.

Ограничения.

На компьютере, где будет производиться сборка снапшота, должны быть предварительно установлены следующие программы:
  1. Среда разработки Microsoft Visual Studio 2005
  1. Клиент CVS-систем, для скачивания исходных кодов [Скачать](http://www.tortoisecvs.org/download.shtml)
  1. Парсер регулярных выражений SED для автоматической подстановки версии сборки в имя файла. [Скачать](http://sourceforge.net/projects/getgnuwin32)
  1. Архиватор WinRar (опционально) [Скачать](http://www.rarlab.com/download.htm)
  1. Архиватор 7-ZIP (опционально) [Скачать](http://www.7-zip.org/download.html)

Ниже приводится пример пакетного файла, собирающего снапшот Firebird-а из исходников.

⚠️ Не забудьте поменять предопределенные пути к файлам на свои !

```dos
@echo off
@set CVS="c:\appl\cvsnt\cvs.exe"
@set SED="c:\appl\GetGnuWin32\bin\sed.exe"
@set RAR="C:\Program Files\WinRAR\rar.exe"
@set ZIP="C:\Program Files\7-Zip\7z.exe"
@set INSTALL_SAVE="c:\appl\firebirdbuild"
@set FIREBIRD_SRC=c:\appl\firebirdbuild\firebird2
@set FIREBIRD_TMP=%FIREBIRD_SRC%\temp
@%CVS% -z9 -d:pserver:anonymous@firebird.cvs.sourceforge.net:/cvsroot/firebird checkout -P firebird2
@cd %FIREBIRD_SRC%\builds\win32\
@call clean_all.bat
@call make_icu.bat CLEAN
@call make_boot.bat CLEAN
@call make_all.bat CLEAN
@find "#define PRODUCT_VER_STRING" %FIREBIRD_SRC%\src\jrd\build_no.h > %FIREBIRD_TMP%\b$1.txt
@%SED% -n -e s/\"//g -e s/"#define PRODUCT_VER_STRING "//w%FIREBIRD_TMP%\b$2.txt %FIREBIRD_TMP%\b$1.txt
@for /f "tokens=*" %%i in ('TYPE %FIREBIRD_TMP%\b$2.txt') do @set FIREBIRD_VER_STRING=%%i
@del %FIREBIRD_TMP%\b$?.txt
@set FIREBIRD_BUILD_VERSION=Firebird-%FIREBIRD_VER_STRING%-0_Win32_BuilderName
@cd %FIREBIRD_SRC%\output_win32
@%RAR% a -r -rr10p %FIREBIRD_BUILD_VERSION%.rar *.*
@copy /y *.rar %INSTALL_SAVE%\*.rar
@erase *.rar
@%ZIP% a -r -tzip %FIREBIRD_BUILD_VERSION%.zip *.*
@copy /y *.zip %INSTALL_SAVE%\*.zip
@erase *.zip
@%ZIP% a -r -t7z %FIREBIRD_BUILD_VERSION%.7z *.*
@copy /y *.7z %INSTALL_SAVE%\*.7z
@erase *.7z
@call %FIREBIRD_SRC%\builds\win32\clean_all.bat
```

## LINUX

## См. также
