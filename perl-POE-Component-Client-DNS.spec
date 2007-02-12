#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Client-DNS
Summary:	POE component for non-blocking/concurrent DNS queries
Summary(pl.UTF-8):   Komponent POE do wykonywania nieblokujących/równoczesnych zapytań DNS
Name:		perl-POE-Component-Client-DNS
Version:	0.99
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17d8823b50185e4a2536ca8888d45410
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS >= 0.53
BuildRequires:	perl-POE >= 1:0.3100
%endif
Requires:	perl-POE >= 1:0.3100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::DNS is a wrapper for non-blocking Net::DNS.
It lets other tasks to run while something is waiting for a nameserver
to respond, and it lets several DNS queries run in parallel.

%description -l pl.UTF-8
POE::Component::Client::DNS to interfejs do nieblokującej klasy
Net::DNS. Pozwala na wykonywanie innych zadań podczas gdy coś czeka na
odpowiedź serwera nazw, a także pozwala na równoległe wykonywanie
kilku zapytań DNS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/POE/Component/Client/*.pm
%{_mandir}/man3/*
