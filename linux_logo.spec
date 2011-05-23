Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Boot and Init
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Patch0:		linux_logo-5.02-use-mdk-logo.patch

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q
%patch0 -p1 -b .mdklogos~

%build
./configure --prefix=%{_prefix}
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

%clean

%files -f %{name}.lang
%defattr(-,root, root)
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
