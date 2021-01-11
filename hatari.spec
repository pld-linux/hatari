#
# Conditional build:
%bcond_with	capsimage	# use capsimage for .IPF, .RAW and .CTR disk image support
#
Summary:	hatari - an Atari ST and STE emulator for Linux
Summary(pl.UTF-8):	hatari - emulator Atari ST i STE dla Linuksa
Name:		hatari
Version:	2.3.1
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://download.tuxfamily.org/hatari/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	52f572328edc575db17e54d4fd2d3a20
Patch0:		%{name}-useless_files.patch
Patch1:		%{name}-desktop.patch
URL:		http://hatari.tuxfamily.org/
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 3.3
%{?with_capsimage:BuildRequires:	libcapsimage-devel >= 5}
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	python3 >= 1:3
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	sed >= 4.0
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
%{!?with_capsimage:BuildConflicts:	libcapsimage-devel}
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+3 >= 3.0
Requires:	hicolor-icon-theme
Requires:	python3 >= 1:3.2
Requires:	python3-pygobject3 >= 3
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hatari is an Atari ST and STE emulator for Linux and other systems
that are supported by the SDL library. Hatari supports the emulation
of most of the ST and STE hardware.

%description -l pl.UTF-8
Hatari jest emulatorem Atari ST i STE dla Linuksa i innych systemów
obsługiwanych przez bibliotekę SDL. Hatari emuluje większość sprzętu
Atari ST i STE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,#!/usr/bin/env python3,#!%{__python3},' python-ui/*.py tools/*.py tools/debugger/*.py tools/hconsole/*.py

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	%{?with_sdl2:-DENABLE_SDL2=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/fr/man1

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/fr/hatari.1	$RPM_BUILD_ROOT%{_mandir}/fr/man1

%py3_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/hatariui
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}/hatariui

for f in README TODO ; do
	%{__mv} python-ui/${f} python-ui/${f}-ui
done
%{__mv} tools/hconsole/{release-notes.txt,release-notes-hconsole.txt}
%{__mv} python-ui/{release-notes.txt,release-notes-ui.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%update_mime_database

%postun
%update_desktop_database
%update_icon_cache hicolor
%update_mime_database

%files
%defattr(644,root,root,755)
%doc readme.txt doc/{authors,changelog,emutos,keymap-sample,memory-usage,midi-linux,release-notes,todo}.txt doc/{compatibility,manual}.html tools/hconsole/release-notes-hconsole.txt python-ui/{README-ui,TODO-ui,release-notes-ui.txt}
%attr(755,root,root) %{_bindir}/atari-convert-dir
%attr(755,root,root) %{_bindir}/atari-hd-image
%attr(755,root,root) %{_bindir}/gst2ascii
%attr(755,root,root) %{_bindir}/hatari
%attr(755,root,root) %{_bindir}/hatari-prg-args
%attr(755,root,root) %{_bindir}/hatari_profile
%attr(755,root,root) %{_bindir}/hatariui
%attr(755,root,root) %{_bindir}/hmsa
%attr(755,root,root) %{_bindir}/zip2st
%{_datadir}/%{name}
%{_mandir}/man1/atari-convert-dir.1*
%{_mandir}/man1/atari-hd-image.1*
%{_mandir}/man1/gst2ascii.1*
%{_mandir}/man1/hatari-prg-args.1*
%{_mandir}/man1/hatari_profile.1*
%{_mandir}/man1/hatariui.1*
%{_mandir}/man1/hconsole.1*
%{_mandir}/man1/hmsa.1*
%{_mandir}/man1/zip2st.1*
%lang(fr) %{_mandir}/fr/man1/hatari.1*
%{_desktopdir}/hatariui.desktop
%{_desktopdir}/hatari.desktop
%{_iconsdir}/hicolor/*/apps/hatari.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-st-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.fastcopy-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.msa-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-stx-disk-image.*
%{_datadir}/mime/packages/hatari.xml
