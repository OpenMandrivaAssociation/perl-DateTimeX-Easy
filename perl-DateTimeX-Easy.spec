%define upstream_name    DateTimeX-Easy
%define upstream_version 0.089

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse a date/time string using the best method available
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTimeX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Date::Parse)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::DateManip)
BuildRequires: perl(DateTime::Format::Flexible)
BuildRequires: perl(DateTime::Format::ICal)
BuildRequires: perl(DateTime::Format::Natural)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Time::Zone)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
DateTimeX::Easy makes DateTime object creation quick and easy. It uses a
variety of DateTime::Format packages to do the bulk of the parsing, with
some custom tweaks to smooth out the rough edges (mainly concerning
timezone detection and selection).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
