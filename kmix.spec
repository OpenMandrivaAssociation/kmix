%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Digital Mixer
Name:		kmix
Version:	17.08.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/kmix/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%files
%dir %{_datadir}/kmix
%dir %{_datadir}/kmix/pics
%dir %{_datadir}/kmix/profiles

%{_sysconfdir}/xdg/autostart/*kmix_*.desktop
%{_bindir}/kmix*
%{_libdir}/lib*_kmix*.so
%{_libdir}/qt5/plugins/lib*_kmixd.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mixer.so
%{_datadir}/plasma/services/mixer.operations
%{_datadir}/applications/kmix.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmix.*.xml
%{_datadir}/kmix/pics/*.png
%{_datadir}/kmix/profiles/*.xml
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kxmlgui5/kmix
%{_iconsdir}/hicolor/*/actions/kmix.png

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5 -DKMIX_KF5_BUILD:BOOL=ON

%build
%ninja -C build

%install
%ninja_install -C build
