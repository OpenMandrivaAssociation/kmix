Name:		kmix
Version:	4.9.0
Release:	1
Epoch:		3
Summary:	KDE Digital Mixer
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/kmix/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
Requires:	kdebase4-runtime
Obsoletes:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95

%description
KMix is an application to allow you to change the volume of your sound
card. Though small, it is full-featured, and it supports several
platforms and sound drivers.

%files
%{_kde_appsdir}/kmix
%{_kde_appsdir}/plasma/services/mixer.operations
%{_kde_bindir}/kmix
%{_kde_bindir}/kmixctrl
%{_kde_iconsdir}/*/*/*/*
%{_kde_applicationsdir}/kmix.desktop
%{_kde_services}/kmixctrl_restore.desktop
%{_kde_services}/plasma-engine-mixer.desktop
%{_kde_services}/kded/kmixd.desktop
%{_kde_libdir}/libkdeinit4_kmix*
%{_kde_libdir}/kde4/kded_kmixd.so
%{_kde_libdir}/kde4/plasma_engine_mixer.so
%{_kde_autostart}/restore_kmix_volumes.desktop
%{_kde_autostart}/kmix_autostart.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml
%{_kde_docdir}/HTML/en/kmix

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

