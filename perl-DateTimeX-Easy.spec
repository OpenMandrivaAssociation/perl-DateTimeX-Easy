%define upstream_name    DateTimeX-Easy
%define upstream_version 0.089

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DateTimeX::Easy::DateParse\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse a date/time string using the best method available
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTimeX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::DateManip)
BuildRequires:	perl(DateTime::Format::Flexible)
BuildRequires:	perl(DateTime::Format::ICal)
BuildRequires:	perl(DateTime::Format::Natural)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Time::Zone)

BuildArch:	noarch

%description
DateTimeX::Easy makes DateTime object creation quick and easy. It uses a
variety of DateTime::Format packages to do the bulk of the parsing, with
some custom tweaks to smooth out the rough edges (mainly concerning
timezone detection and selection).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.89.0-2mdv2011.0
+ Revision: 655588
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.89.0-1mdv2011.0
+ Revision: 572809
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.089

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.88.0-1mdv2011.0
+ Revision: 543018
- import perl-DateTimeX-Easy


* Thu May 06 2010 cpan2dist 0.088-1mdv
- initial mdv release, generated with cpan2dist
