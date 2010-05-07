%define _requires_exceptions pkgconfig(pygtk-2.0)
%define oname pyxfce
%define snap 29680

Summary:	Python bindings for Xfce
Name:		python-xfce
Version:	4.4.1
Release:	%mkrel -c %{snap} 3
License:	BSD
Group:		Development/Python
Url:		http://pyxfce.xfce.org
Source0:	http://pyxfce.xfce.org/%{oname}-%{version}-svn%{snap}.tar.bz2
BuildRequires:	libxfce4util-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4-panel-devel
BuildRequires:	pygtk2.0-devel
Requires:	pygtk2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for the Xfce desktop environment.

%prep
%setup -qn %{oname}-%{version}

%build
xdt-autogen
%configure2_5x \
	--enable-final

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# strip $RPM_BUILD_ROOT from libs
sed -i s%%{buildroot}%""%g %{buildroot}%{py_platsitedir}/xfce4/*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_libdir}/pkgconfig/pyxfce-1.0.pc
%{py_platsitedir}/xfce4/*.py*
%{py_platsitedir}/xfce4/*.la
%{py_platsitedir}/xfce4/*.so
%{_datadir}/%{oname}/4.2/defs/*.defs
