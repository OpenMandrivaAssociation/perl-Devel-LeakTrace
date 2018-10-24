%define upstream_name    Devel-LeakTrace
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:    Memory debugger for perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: glib-devel 
BuildRequires: perl-Module-Build
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
This module enables to find memory leaks in perl programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
#./Build
%make OPTIMIZE="%{optflags}"

%install
./Build install destdir=%{buildroot}

%check
#./Build test

%clean

%files
%defattr(-, root, root)
%doc Changes README 
%{_mandir}/*/*
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*


