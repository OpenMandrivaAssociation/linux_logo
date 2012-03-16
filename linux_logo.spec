Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	4
License:	GPL
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Patch0:		linux_logo-5.02-use-mdk-logo.patch

%define debug_package \
%ifnarch noarch\
%global __debug_package 1\
%package debuginfo\
Summary: Debug information for package %{name}\
Group: Development/Debug\
AutoReqProv: 0\
%description debuginfo\
This package provides debug information for package %{name}.\
Debug information is useful when developing applications that use this\
package or when debugging this package.\
%files debuginfo -f debugfiles.list\
%defattr(-,root,root)\
%endif\
%{nil}

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q
%patch0 -p1 -b .mdklogos~
find -exec chmod go+r {} + 

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
