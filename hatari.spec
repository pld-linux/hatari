Summary:	hatari - an Atari ST and STE emulator for Linux
Summary(pl):	hatari - emulator Atari ST i STE dla Linuksa
Name:		hatari
Version:	0.80
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/hatari/%{name}-%{version}.tar.gz
# Source0-md5:	01d342566d69a4721b61ad5c912174ec
URL:		http://hatari.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hatari is an Atari ST and STE emulator for Linux and other systems
that are supported by the SDL library. Hatari supports the emulation
of most of the ST and STE hardware.

%description -l pl
Hatari jest emulatorem Atari ST i STE dla Linuksa i innych systemów
obs³ugiwanych przez bibliotekê SDL. Hatari emuluje wiêkszo¶æ sprzêtu
Atari ST i STE.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--datadir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/hatari.1	$RPM_BUILD_ROOT%{_mandir}/man1/hatari.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/hatari.1*
