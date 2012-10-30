Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	6
License:	GPL
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Patch0:		linux_logo-5.02-use-mdk-logo.patch

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q
%patch0 -p1 -b .mdklogos~
find -exec chmod go+r {} + 

f=CHANGE
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%build
./configure --prefix=%{_prefix}
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

%files -f %{name}.lang
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
