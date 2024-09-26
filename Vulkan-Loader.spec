#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : Vulkan-Loader
Version  : 1.3.296
Release  : 168
URL      : https://github.com/KhronosGroup/Vulkan-Loader/archive/v1.3.296/Vulkan-Loader-1.3.296.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Loader/archive/v1.3.296/Vulkan-Loader-1.3.296.tar.gz
Summary  : Vulkan Loader
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Loader-lib = %{version}-%{release}
Requires: Vulkan-Loader-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libX11-dev
BuildRequires : libX11-dev32
BuildRequires : libX11-lib
BuildRequires : pkg-config
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Vulkan Loader
This project provides the Khronos official Vulkan Loader for all platforms except [Android](https://android.googlesource.com/platform/frameworks/native/+/master/vulkan/)

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
%setup -q -n Vulkan-Loader-1.3.296
cd %{_builddir}/Vulkan-Loader-1.3.296
pushd ..
cp -a Vulkan-Loader-1.3.296 build32
popd
pushd ..
cp -a Vulkan-Loader-1.3.296 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727381985
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBUILD_WSI_DIRECTFB_SUPPORT=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DBUILD_WSI_DIRECTFB_SUPPORT=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../build32/
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 .. -DBUILD_WSI_DIRECTFB_SUPPORT=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../../build32/clr-build32;
make test || : || :
cd ../../buildavx2/clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1727381985
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Loader
cp %{_builddir}/Vulkan-Loader-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Loader/9bf8124f4495a48c4fd7104aebe2e957176b930b || :
export GOAMD64=v2
pushd ../build32/
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
popd
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/VulkanLoader/VulkanLoaderConfig-relwithdebinfo.cmake
/usr/lib64/cmake/VulkanLoader/VulkanLoaderConfig.cmake
/usr/lib64/cmake/VulkanLoader/VulkanLoaderConfigVersion.cmake
/usr/lib64/libvulkan.so
/usr/lib64/pkgconfig/vulkan.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/VulkanLoader/VulkanLoaderConfig-relwithdebinfo.cmake
/usr/lib32/cmake/VulkanLoader/VulkanLoaderConfig.cmake
/usr/lib32/cmake/VulkanLoader/VulkanLoaderConfigVersion.cmake
/usr/lib32/libvulkan.so
/usr/lib32/pkgconfig/32vulkan.pc
/usr/lib32/pkgconfig/vulkan.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libvulkan.so.1.3.296
/usr/lib64/libvulkan.so.1
/usr/lib64/libvulkan.so.1.3.296

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so.1
/usr/lib32/libvulkan.so.1.3.296

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Loader/9bf8124f4495a48c4fd7104aebe2e957176b930b
