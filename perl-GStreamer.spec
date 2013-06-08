#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires some plugins to be operational)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	GStreamer
Summary:	Perl gstreamer bindings
Summary(pl.UTF-8):	Wiązania gstreamera dla Perla
Name:		perl-GStreamer
Version:	0.17
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	8fe097daf0e2534452a3f69af05ec9fd
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gstreamer-devel >= 0.10.9
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib-devel >= 1.180
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.180
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gstreamer library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki gstreamera.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/GStreamer/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/GStreamer/*/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.pre-git NEWS README TODO
%{perl_vendorarch}/GStreamer.pm
%dir %{perl_vendorarch}/GStreamer
%{perl_vendorarch}/GStreamer/Install
%dir %{perl_vendorarch}/auto/GStreamer
%attr(755,root,root) %{perl_vendorarch}/auto/GStreamer/GStreamer.so
%{perl_vendorarch}/auto/GStreamer/GStreamer.bs
%{_mandir}/man3/GStreamer*.3pm*
