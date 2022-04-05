#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	21.12.3
%define		kframever	5.69.0
%define		qtver		5.9.0
%define		kaname		dolphin
Summary:	File manager
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	961fe4a340ba0cbe1805afe29398adf4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kemoticons-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kinit-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemmodels-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kpty-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	ruby-test-unit
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
navigate through the hierarchy of files and folders. • Supports
several different kinds of view styles and properties and allows you
to configure the view exactly how you want it. • Split view, allowing
you to easily copy or move files between locations. • Additional
information and shortcuts are available as dock-able panels, allowing
you to move them around freely and display exactly what you want. •
Multiple tab support • Informational dialogues are displayed in an
unobtrusive way. • Undo/redo support • Transparent network access
through the KIO system.

%description -l pl.UTF-8
Dolphin to lekki zarządca plików. Zaprojektowany jako łatwy w użyciu,
choć zapewniający elastyczność i możliwości konfiguracji. To znaczy,
że możesz go używać dokładnie, tak jakbyś chciał.

Cechy

• Pasek nawigacyjny dla URLi pozwalający na szybkie przemieszczanie
się wśród hierarchi plików i folderów • Wspiera wiele różnych rodzajów
przeglądania plików pozwalając skonfigurować podgląd tak jak sobie
tego życzysz • Podzielony widok do łatwego kopiowania i przenoszenia
plików między lokacjami • Dodatkowe informacje i skróty klawiszowe są
dostępne jako dokowalne panele, pozwalając przemieszczać się do woli i
wyświetlać to co chcesz • Wiele kart • Informacyjne okna dialogowe nie
drażnią użytkownika • Wsparcie dla Cofnij/Powtórz • Przeźroczysty
dostęp do sieci korzystający z systemu KIO.

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
RUBYLIB=%{_datadir}/gems/gems/test-unit-3.2.3/lib
export RUBYLIB
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dolphin
%attr(755,root,root) %{_bindir}/servicemenuinstaller
%ghost %{_libdir}/libdolphinprivate.so.5
%{_libdir}/libdolphinprivate.so.5.*.*
%ghost %{_libdir}/libdolphinvcs.so.5
%{_libdir}/libdolphinvcs.so.5.*.*
%dir %{_libdir}/qt5/plugins/dolphin
%dir %{_libdir}/qt5/plugins/dolphin/kcms
%{_libdir}/qt5/plugins/dolphin/kcms/libkcm_dolphingeneral.so
%{_libdir}/qt5/plugins/dolphin/kcms/libkcm_dolphinnavigation.so
%{_libdir}/qt5/plugins/dolphin/kcms/libkcm_dolphinviewmodes.so
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
%{_datadir}/kservices5/kcmdolphinviewmodes.desktop
%{_datadir}/kservicetypes5/fileviewversioncontrolplugin.desktop
%{_datadir}/metainfo/org.kde.dolphin.appdata.xml
%{_datadir}/kglobalaccel/org.kde.dolphin.desktop
%{_datadir}/qlogging-categories5/dolphin.categories
%{_datadir}/knsrcfiles/servicemenu.knsrc
%{systemduserunitdir}/plasma-dolphin.service
%{_libdir}/qt5/plugins/kf5/parts/dolphinpart.so
%{_datadir}/config.kcfg/dolphin_contextmenusettings.kcfg

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdolphinvcs.so
%{_includedir}/Dolphin
%{_includedir}/dolphin_export.h
%{_includedir}/dolphinvcs_export.h
%{_libdir}/cmake/DolphinVcs
