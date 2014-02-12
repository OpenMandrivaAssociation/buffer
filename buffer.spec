Summary:	General purpose buffer program
Name:		buffer
Version:	1.19
Release:	10
License:	GPLv2+
Group:		Archiving/Backup
Source0:	%{name}-%{version}.tar.bz2
Patch0:		buffer_1.19-7.patch.bz2

%description
This is a program designed to speed up writing tapes on remote tape
drives. After startup it splits itself into two processes. The first
process reads (and reblocks) from stdin into a shared memory buffer.
The second writes from the shared memory buffer to stdout.  Doing it this way
means that the writing side effectly sits in a tight write loop and
doesn't have to wait for input.  Similarly for the input side.  It is
this waiting that slows down other reblocking processes, like dd.

%files
%doc COPYING README
%{_bindir}/buffer
%{_mandir}/man1/buffer.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%{optflags}"

%install
install -m 755 -D buffer %{buildroot}%{_bindir}/buffer
install -m 644 -D buffer.man %{buildroot}%{_mandir}/man1/buffer.1

