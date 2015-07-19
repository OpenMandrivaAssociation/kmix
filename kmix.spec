Summary:	KDE Digital Mixer
Name:		kmix
Version:	15.04.3
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/kmix/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires: cmake(KF5GlobalAcc)                                                                     
BuildRequires: cmake(KF5I18n)                                                                          
BuildRequires: cmake(KF5XmlGui)                                                                        
BuildRequires: cmake(KF5DBusAddons)                                                                    
BuildRequires: cmake(KF5KCMUtils)                                                                      
BuildRequires: cmake(KF5KDELibs4Support)   
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
%{_datadir}/apps/kmix                                                                                  
%{_bindir}/kmix                                                                                        
%{_bindir}/kmixctrl                                                                                    
%{_bindir}/kmixremote                                                                                  
%{_iconsdir}/*/*/*/*                                                                                   
%{_datadir}/applications/kde4/kmix.desktop                                                             
%{_datadir}/kde4/services/kmixctrl_restore.desktop                                                     
%{_datadir}/kde4/services/kded/kmixd.desktop                                                           
%{_libdir}/libkdeinit4_kmix*                                                                           
%{_libdir}/kde4/kded_kmixd.so                                                                          
%{_kde_autostart}/restore_kmix_volumes.desktop                                                         
%{_kde_autostart}/kmix_autostart.desktop                                                               
%{_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml                                                 
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml                                                   
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml                                                  
%doc %{_docdir}/HTML/en/kmix

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
