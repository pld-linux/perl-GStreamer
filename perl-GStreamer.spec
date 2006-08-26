#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	GStreamer
Summary:	Perl gstreamer bindings
Summary(pl):	Wi±zania gstreamer dla Perla
Name:		perl-Gnome2-GStreamer
Version:	0.09
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	4f6f27edded250b00055d076eb738ff5
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gstreamer-devel >= 0.10.9
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.132
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.132
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gstreamer library.

%description -l pl
Ten modu³ daje dostêp z poziomu Perla do biblioteki gstreamer.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pnam}/*.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pnam}/*/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pnam}.pm
%dir %{perl_vendorarch}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pnam}/*.so
%{perl_vendorarch}/%{pnam}/Install
%{perl_vendorarch}/auto/%{pnam}/*.bs
%{_mandir}/man3/*
