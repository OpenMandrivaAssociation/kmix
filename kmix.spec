%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Digital Mixer
Name:		kmix
Version:	25.08.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/multimedia/kmix/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
Obsoletes:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%patchlist
# kmix isn't compatible with the current version of sndio,
# so disable the sndio backend
kmix-no-sndio.patch

%description
KMix is an application to allow you to change the volume of your sound
card. Though small, it is full-featured, and it supports several
platforms and sound drivers.

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/kmix_autostart.desktop
%{_sysconfdir}/xdg/autostart/restore_kmix_volumes.desktop
%{_bindir}/kmix
%{_bindir}/kmixctrl
%{_bindir}/kmixremote
%{_libdir}/libkmixcore.so.*
%{_datadir}/applications/org.kde.kmix.desktop
%{_datadir}/config.kcfg/kmixsettings.kcfg
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/icons/hicolor/*/actions/kmix.*
%{_datadir}/kmix
%{_datadir}/knotifications6/kmix.notifyrc
%{_datadir}/kxmlgui5/kmix/kmixui.rc
%{_datadir}/metainfo/org.kde.kmix.appdata.xml
%{_datadir}/qlogging-categories6/kmix.categories
