%define name buffer
%define version 1.19
%define release %mkrel 8

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
