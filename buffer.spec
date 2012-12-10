%define name buffer
%define version 1.19
%define release %mkrel 9

Summary: General purpose buffer program
Name: %name
Version: %version
Release: %release
License: GPL
Group: Archiving/Backup
Source: %name-%version.tar.bz2
Patch0: buffer_1.19-7.patch.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This is a program designed to speed up writing tapes on remote tape
drives. After startup it splits itself into two processes.  The first 
process reads (and reblocks) from stdin into a shared memory buffer.  
The second writes from the shared memory buffer to stdout.  Doing it this way
means that the writing side effectly sits in a tight write loop and
doesn't have to wait for input.  Similarly for the input side.  It is
this waiting that slows down other reblocking processes, like dd.

%prep
rm -rf $RPM_BUILD_ROOT

%setup 

%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall -s"

%install
install -m 755 -D buffer $RPM_BUILD_ROOT%{_bindir}/buffer
install -m 644 -D buffer.man $RPM_BUILD_ROOT%{_mandir}/man1/buffer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/buffer
%{_mandir}/man1/buffer.1*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.19-9mdv2011.0
+ Revision: 616902
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.19-8mdv2010.0
+ Revision: 436902
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.19-7mdv2009.1
+ Revision: 350662
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.19-6mdv2009.0
+ Revision: 240458
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 01 2007 Bruno Cornec <bcornec@mandriva.org> 1.19-4mdv2008.0
+ Revision: 77248
- Import buffer



* Thu Jan 19 2006 Lenny Cartier <lenny@mandriva.com> 1.19-4mdk
- fix x86_64 with debian patch

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.19-3mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.19-2mdk
- rebuild

* Thu Apr 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.19-1mdk
- added for mondo

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Tue Jul 11 2000 Than Ngo <than@redhat.de>
- rebuilt

* Wed Jun 07 2000 Than Ngo <than@redhat.de>
- use rpm macros

* Mon Jun 05 2000 Michael Stefaniuc <mstefani@redhat.com>
- rewrote the spec file
- rewrote and extended the buffer patch
