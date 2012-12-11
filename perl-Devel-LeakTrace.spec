%define upstream_name    Devel-LeakTrace
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Memory debugger for perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: glib-devel 
BuildRequires: perl-Module-Build
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module enables to find memory leaks in perl programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
#./Build
%make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT

%check
#./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README 
%{_mandir}/*/*
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*


%changelog
* Wed Jan 25 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 0.50.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.50.0-3
+ Revision: 681400
- mass rebuild

* Tue Aug 04 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.50.0-2mdv2010.0
+ Revision: 408700
- force rebuild
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-8mdv2009.0
+ Revision: 256632
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2008.1
+ Revision: 152061
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.05-5mdv2008.0
+ Revision: 43108
- rebuild


* Wed Nov 02 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.05-4mdk
- Fix BuildRequires

* Wed Nov 02 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.05-3mdk
- Fix BuildRequires
- %%mkrel

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-2mdk
- rebuild for new perl

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-1mdk
- initial release

