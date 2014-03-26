Summary:	Compiler for the GObject type system
Name:		vala
Version:	0.24.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.gnome.org/sources/vala/0.24/%{name}-%{version}.tar.xz
# Source0-md5:	beddeff9c06d3c278988b237da0e7401
URL:		http://live.gnome.org/Vala
BuildRequires:	glib-devel >= 1:2.40.0
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib-devel >= 1:2.40.0
Requires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	0.24

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared
to applications and libraries written in C.

%package libs
Summary:	Vala library
Group:		Libraries

%description libs
Vala library.

%package vapigen
Summary:	Vala vavpi generator
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description vapigen
Vala vapi generator.

%package devel
Summary:	Header files for Vala library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for vala library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--enable-vapigen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

install -d $RPM_BUILD_ROOT%{_datadir}/vala/vapi

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/vala
%attr(755,root,root) %{_bindir}/vala-%{apiver}
%attr(755,root,root) %{_bindir}/valac
%attr(755,root,root) %{_bindir}/valac-%{apiver}

%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%dir %{_datadir}/vala-%{apiver}
%dir %{_datadir}/vala-%{apiver}/vapi
%{_datadir}/vala-%{apiver}/vapi/*.vapi
%{_datadir}/vala-%{apiver}/vapi/*.deps

%{_mandir}/man1/valac*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libvala-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libvala-%{apiver}.so.*.*.*

%files vapigen
%defattr(644,root,root,755)
%dir %{_libdir}/vala-%{apiver}
%attr(755,root,root) %{_bindir}/vala-gen-introspect
%attr(755,root,root) %{_bindir}/vala-gen-introspect-%{apiver}
%attr(755,root,root) %{_bindir}/vapicheck
%attr(755,root,root) %{_bindir}/vapicheck-%{apiver}
%attr(755,root,root) %{_bindir}/vapigen
%attr(755,root,root) %{_bindir}/vapigen-%{apiver}
%attr(755,root,root) %{_libdir}/vala-%{apiver}/gen-introspect-%{apiver}
%{_aclocaldir}/vapigen.m4
%{_datadir}/vala/*.vapigen
%{_npkgconfigdir}/vapigen*.pc
%{_mandir}/man1/vala-gen-introspect-*.*
%{_mandir}/man1/vapigen-*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvala-%{apiver}.so
%{_aclocaldir}/vala.m4
%{_includedir}/vala-%{apiver}
%{_pkgconfigdir}/libvala-%{apiver}.pc

