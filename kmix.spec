%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Digital Mixer
Name:		kmix
Version:	21.04.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/kmix/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
Obsoletes:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95

%description
KMix is an application to allow you to change the volume of your sound
card. Though small, it is full-featured, and it supports several
platforms and sound drivers.

%files -f %{name}.lang
%dir %{_datadir}/kmix
%dir %{_datadir}/kmix/pics
%dir %{_datadir}/kmix/profiles

%{_sysconfdir}/xdg/autostart/*kmix_*.desktop
%{_bindir}/kmix*
# This is more of a module than a shared library.
# Packaging it without libpackage is intentional.
%{_libdir}/libkmixcore.so*
%{_libdir}/qt5/plugins/kf5/kded/kmixd.so
%{_datadir}/knotifications5/kmix.notifyrc
%{_datadir}/applications/org.kde.kmix.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmix.*.xml
%{_datadir}/kmix/pics/*.png
%{_datadir}/kmix/profiles/*.xml
%{_datadir}/kservices5/*.desktop
%{_datadir}/kxmlgui5/kmix
%{_iconsdir}/hicolor/*/actions/kmix.png
%{_datadir}/metainfo/org.kde.kmix.appdata.xml
%{_datadir}/config.kcfg/kmixsettings.kcfg
%{_datadir}/qlogging-categories5/kmix.categories

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5 -DKMIX_KF5_BUILD:BOOL=ON

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
