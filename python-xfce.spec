%define oname pyxfce

Summary:	Python bindings for Xfce
Name:		python-xfce
Version:	4.4.0
Release:	%mkrel 3
License:	GPL
Group:		Development/Python
Url:		http://pyxfce.xfce.org
Source0:	http://pyxfce.xfce.org/%{oname}-%{version}.tar.bz2
BuildRequires:	libxfce4util-devel >= 4.4.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4mcs-devel
BuildRequires:	pygtk2.0-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for the Xfce environment.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--enable-final

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# strip $RPM_BUILD_ROOT from libs
sed -i s%%{buildroot}%""%g %{buildroot}%{py_sitedir}/xfce4/*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/pkgconfig/pyxfce-1.0.pc
%{py_sitedir}/xfce4/*.py*
%{py_sitedir}/xfce4/*.la
%{py_sitedir}/xfce4/*.so
%{_datadir}/%{oname}/4.2/defs/*.defs
