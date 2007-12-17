%define module Devel-LeakTrace
%define fmodule Devel/LeakTrace

Summary: Memory debugger for perl
Name:    perl-%module
Version: 0.05
Release: %mkrel 5
License: GPL or Artistic
Group:   Development/Perl
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: perl-Module-Build
BuildRequires: glib-devel 
BuildRequires: perl-devel

%description
This module enables to find memory leaks in perl programs.

%prep
%setup -q -n %module-%version
perl Makefile.PL INSTALLDIRS=vendor
#./Build
%make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT
#./Build test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc Changes README 
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


