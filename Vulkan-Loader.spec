#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-Loader
Version  : 1.2.197
Release  : 76
URL      : https://github.com/KhronosGroup/Vulkan-Loader/archive/v1.2.197/Vulkan-Loader-1.2.197.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Loader/archive/v1.2.197/Vulkan-Loader-1.2.197.tar.gz
Summary  : Vulkan Loader
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Loader-lib = %{version}-%{release}
Requires: Vulkan-Loader-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libX11-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32pciaccess)
BuildRequires : pkgconfig(32pthread-stubs)
BuildRequires : pkgconfig(32wayland-client)
BuildRequires : pkgconfig(32wayland-cursor)
BuildRequires : pkgconfig(32wayland-egl)
BuildRequires : pkgconfig(32wayland-server)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3

%description
# Vulkan Ecosystem Components
This project provides the Khronos official Vulkan ICD desktop loader for Windows, Linux, and MacOS.

%package dev
Summary: dev components for the Vulkan-Loader package.
Group: Development
Requires: Vulkan-Loader-lib = %{version}-%{release}
Provides: Vulkan-Loader-devel = %{version}-%{release}
Requires: Vulkan-Loader = %{version}-%{release}

%description dev
dev components for the Vulkan-Loader package.


%package dev32
Summary: dev32 components for the Vulkan-Loader package.
Group: Default
Requires: Vulkan-Loader-lib32 = %{version}-%{release}
Requires: Vulkan-Loader-dev = %{version}-%{release}

%description dev32
dev32 components for the Vulkan-Loader package.


%package lib
Summary: lib components for the Vulkan-Loader package.
Group: Libraries
Requires: Vulkan-Loader-license = %{version}-%{release}

%description lib
lib components for the Vulkan-Loader package.


%package lib32
Summary: lib32 components for the Vulkan-Loader package.
Group: Default
Requires: Vulkan-Loader-license = %{version}-%{release}

%description lib32
lib32 components for the Vulkan-Loader package.


%package license
Summary: license components for the Vulkan-Loader package.
Group: Default

%description license
license components for the Vulkan-Loader package.


%prep
%setup -q -n Vulkan-Loader-1.2.197
cd %{_builddir}/Vulkan-Loader-1.2.197

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635959105
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 .. -DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build32;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1635959105
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Loader
cp %{_builddir}/Vulkan-Loader-1.2.197/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Loader/9bf8124f4495a48c4fd7104aebe2e957176b930b
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/libvulkan.so
/usr/lib64/pkgconfig/vulkan.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so
/usr/lib32/pkgconfig/32vulkan.pc
/usr/lib32/pkgconfig/vulkan.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvulkan.so.1
/usr/lib64/libvulkan.so.1.2.197

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so.1
/usr/lib32/libvulkan.so.1.2.197

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Loader/9bf8124f4495a48c4fd7104aebe2e957176b930b
