%define	name	linux_logo
%define	version	5.02
%define	rel	1
%define	release	%mkrel %{rel}

Summary:	ASCII Tux (Linux Penguin) 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Patch0:		linux_logo-5.02-use-mdk-logo.patch

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q
%patch0 -p1 -b .mdklogos

%build
./configure --prefix=%{buildroot}%{_prefix}
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root, root)
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
