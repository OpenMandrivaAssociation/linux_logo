Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	29
License:	GPLv2
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
Source1:	linux_logo.service
Source2:	linux_logo.sysinit
Source3:	linux_logo.sysconfig
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Patch0:		linux_logo-5.02-use-mdk-logo.patch
Patch1:		linux_logo-5.11-moondrake-logo.patch
Patch2:		linux_logo-5.11-openmandriva-logo.patch
Patch3:		linux_logo-5.11-select-default-logo-during-runtime.patch

%description
This package draws the logo seen at the console.

%prep
%setup -q
%patch0 -p1 -b .mdklogos~
%patch1 -p1 -b .mdk~
%patch2 -p1 -b .omv~
%patch3 -p1 -b .runtime~
find -exec chmod go+r {} + 

f=CHANGES
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%build
./configure --prefix=%{_prefix}
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

install -m644 -p %{SOURCE1} -D %{buildroot}%{_unitdir}/%{name}.service
install -m755 -p %{SOURCE2} -D %{buildroot}%{_libexecdir}/%{name}
install -m644 -p %{SOURCE3} -D %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%files -f %{name}.lang
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-7
- rebuild

* Tue Oct 30 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-6
+ Revision: 820721
- update license
- fix encoding of 'CHANGES'
- remove debuginfo test mess..

* Fri Mar 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-4
+ Revision: 785385
- try again.. :p

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-3
+ Revision: 783709
- abuse package for testing where -debuginfo ends up.. </lame>

* Tue Dec 20 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-2
+ Revision: 743965
- fix files not being world readable

* Mon May 23 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11-1
+ Revision: 677770
- clean out old stuff
- new version

* Tue Sep 28 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.10-1mdv2011.0
+ Revision: 581566
- new release: 5.10
- fix messed up 'update' rule in po/Makefile
- properly set prefix in build without buildroot for translations to work again
- build with %%{ldflags} passed to linker

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 5.06-1mdv2010.0
+ Revision: 395899
- update to new version 5.06

* Wed Feb 18 2009 Jérôme Soyer <saispo@mandriva.org> 5.04-1mdv2009.1
+ Revision: 342465
- New upstream release

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 5.03-3mdv2009.0
+ Revision: 251007
- rebuild
- fix no-buildroot-tag

* Tue Feb 05 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.03-1mdv2008.1
+ Revision: 162559
- New release: 5.03
- drop lame top level defines that gets redefined by tags anyways

* Fri Dec 14 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.02-2mdv2008.1
+ Revision: 120243
- remove the parts of our logos patch that has already been merged upstream
  to avoid double printing of classic logos (fixes #36127)

* Mon Dec 03 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.02-1mdv2008.1
+ Revision: 114602
- update to 5.02
- drop all of our merged patches
- regenerate patch to use mandriva logo as default


* Sun Jan 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.16-1mdv2007.0
+ Revision: 114503
- new release: 4.16
  regenerate P0
  bunzip2 patches
- Import linux_logo

* Tue Mar 21 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.13-1mdk
- 4.13
- fix logo width (updated P4)
- make rpmbuildupdate aware

* Wed May 25 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.12-1mdk
- 4.12
- update logo to say Mandriva Linux (P1 & P4, this also fixes #11135 about size)
- regenerate P0

* Tue Jul 13 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.09-2mdk
- update logo to say Mandrakelinux (P4, fixes #10236)

* Sat Apr 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.09-1mdk
- 4.09
- drop P2 & S1 (merged upstream)

* Tue Mar 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.08-1mdk
- 4.08
- use %%makeinstall_std macro (and by this also install locale files:)
- added nb translation (P2 & S1 by me:)
- improve P0
- cleanups
- fix path to locale (P3)

