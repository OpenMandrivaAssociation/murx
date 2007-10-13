%define name murx
%define version 0.7.0
%define release %mkrel 1

%define tarballver %(echo %version | sed -e 's|\\\.|_|g')

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Filters e-mail, gets rid of spam
License: GPL
Group: Networking/Mail
Source: http://jaist.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{tarballver}.tar.gz
Buildrequires: byacc bison flex pcre-devel gettext-devel
Buildroot: %{_tmppath}/%{name}-buildroot
URL: http://murx.sourceforge.net/

%description
MuRX - Mailfilter Using Regular eXpressions

MuRX is an e-mail filtering system which helps you deleting SPAM from your
mailbox before having trouble downloading it to your computer. It is designed
to save download costs but can also delete virus mails for example.

The project MuRX was started as a student research project of Thomas Stauss
and Kai Hildebrandt. The concept was to design a complete new mailfilter clone
with an more object-orientated design and some extra features mailfilter is
lacking of, e.g. AND filter rules.

Latest MuRX has been built with support for perl style regular expressions:
	"--with-pcre"

%prep
%setup -q

%build
%configure2_5x --with-pcre
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO
%doc doc/codingrules.txt doc/specification_v1.txt
%doc examples/murxrc
%doc contrib/mf2murxrc contrib/README.files contrib/wrapper_murx.bash
%{_bindir}/*
%{_mandir}/man?/*
