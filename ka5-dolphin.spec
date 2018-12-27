%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		dolphin
Summary:	File manager
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b69d59ae2de93fe9213acca858d6a83d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dolphin is a lightweight file manager. It has been designed with ease
of use and simplicity in mind, while still allowing flexibility and
customisation. This means that you can do your file management exactly
the way you want to do it.

Features

• Navigation (or breadcrumb) bar for URLs, allowing you to quickly 
  navigate through the hierarchy of files and folders.
• Supports
  several different kinds of view styles and properties and allows you
  to configure the view exactly how you want it.
• Split view, allowing you to easily copy or move files between locations.
• Additional information and shortcuts are available as dock-able panels,
  allowing you to move them around freely and display exactly what you want.
• Multiple tab support
• Informational dialogues are displayed in an unobtrusive way.
• Undo/redo support
• Transparent network access through the KIO system.

%description -l pl.UTF-8
Dolphin - zarządca plików KDE.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 2.6.0

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/dolphin.categories
/etc/xdg/servicemenu.knsrc
%attr(755,root,root) %{_bindir}/dolphin
%attr(755,root,root) %{_bindir}/servicemenudeinstallation
%attr(755,root,root) %{_bindir}/servicemenuinstallation
%ghost %{_libdir}/libdolphinprivate.so.5
%{_libdir}/libdolphinprivate.so.5.*.*
%ghost %{_libdir}/libdolphinvcs.so.5
%{_libdir}/libdolphinvcs.so.5.*.*
%{_libdir}/libkdeinit5_dolphin.so
%{_libdir}/qt5/plugins/dolphinpart.so
%{_libdir}/qt5/plugins/kcm_dolphingeneral.so
%{_libdir}/qt5/plugins/kcm_dolphinnavigation.so
%{_libdir}/qt5/plugins/kcm_dolphinservices.so
%{_libdir}/qt5/plugins/kcm_dolphinviewmodes.so
%{_desktopdir}/org.kde.dolphin.desktop
%{_datadir}/config.kcfg/dolphin_compactmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_detailsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
%{_datadir}/config.kcfg/dolphin_generalsettings.kcfg
%{_datadir}/config.kcfg/dolphin_iconsmodesettings.kcfg
%{_datadir}/config.kcfg/dolphin_versioncontrolsettings.kcfg
%{_datadir}/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%{_datadir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_datadir}/kservices5/dolphinpart.desktop
%{_datadir}/kservices5/kcmdolphingeneral.desktop
%{_datadir}/kservices5/kcmdolphinnavigation.desktop
%{_datadir}/kservices5/kcmdolphinservices.desktop
%{_datadir}/kservices5/kcmdolphinviewmodes.desktop
%{_datadir}/kservicetypes5/fileviewversioncontrolplugin.desktop
%{_datadir}/metainfo/org.kde.dolphin.appdata.xml

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdolphinvcs.so
%{_includedir}/Dolphin
%{_includedir}/dolphin_export.h
%{_includedir}/dolphinvcs_export.h
%{_libdir}/cmake/DolphinVcs
