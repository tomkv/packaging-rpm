%global amdvlk_commit       56ae0901b977cdfef60f4f7cb64ff765b72a69e4
%global llvm_commit         a29b3901405f374cf77f183b033cf67d8df86a5b
%global xgl_commit          aa330d8e9acffb578c88193e4abe017c8fe15426
%global pal_commit          c9a9f1954e770f1142fa25d311def93a087927ee
%global amdvlk_short_commit %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit   %(c=%{llvm_commit}; echo ${c:0:7})
%global xgl_short_commit    %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit    %(c=%{pal_commit}; echo ${c:0:7})
%global commit_date         20180214
%global gitrel              .%{commit_date}.git%{amdvlk_short_commit}

Name:          amdvlk-vulkan-driver
Version:       2.15
Release:       0%{gitrel}%{?dist}
Summary:       AMD Open Source Driver For Vulkan
License:       MIT
Url:           https://github.com/GPUOpen-Drivers
Source0:       %url/AMDVLK/archive/%{amdvlk_commit}.tar.gz#/AMDVLK-%{amdvlk_short_commit}.tar.gz
Source1:       %url/llvm/archive/%{llvm_commit}.tar.gz#/llvm-%{llvm_short_commit}.tar.gz
Source2:       %url/xgl/archive/%{xgl_commit}.tar.gz#/xgl-%{xgl_short_commit}.tar.gz
Source3:       %url/pal/archive/%{pal_commit}.tar.gz#/pal-%{pal_short_commit}.tar.gz

Requires:      vulkan
Requires:      vulkan-filesystem

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3
BuildRequires: ninja-build
BuildRequires: python3
BuildRequires: perl
BuildRequires: curl
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: libxshmfence-devel
BuildRequires: gtest-devel

%description
The AMD Open Source Driver for Vulkan® is an open-source Vulkan driver
for Radeon™ graphics adapters on Linux®. It is designed to support the
following AMD GPUs:

    Radeon™ HD 7000 Series
    Radeon™ HD 8000M Series
    Radeon™ R5/R7/R9 200/300 Series
    Radeon™ RX 400/500 Series
    Radeon™ M200/M300/M400 Series
    Radeon™ RX Vega Series
    AMD FirePro™ Workstation Wx000/Wx100/Wx300 Series
    Radeon™ Pro WX x100 Series
    Radeon™ Pro 400/500 Series

Note: Pipeline compiler support for geometry and tessellation shaders is
not fully implemented for the Radeon™ RX Vega Series. APU support is
limited. These issues will be addressed in upcoming releases.

%prep
%setup -q -c -n %{name}-%{version} -a 0 -a 1 -a 2 -a 3
ln -s AMDVLK-%{amdvlk_commit} AMDVLK
ln -s llvm-%{llvm_commit} llvm
ln -s xgl-%{xgl_commit} xgl
ln -s pal-%{pal_commit} pal

%build
mkdir -p xgl/build && pushd xgl/build

cmake .. -DCMAKE_AR=`which gcc-ar` \
    -DCMAKE_NM=`which gcc-nm` \
    -DCMAKE_RANLIB=`which gcc-ranlib` \
    -DCMAKE_C_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_CXX_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DINCLUDE_INSTALL_DIR=/usr/include \
    -DLIB_INSTALL_DIR=/usr/lib64 \
    -DSYSCONF_INSTALL_DIR=/etc \
    -DSHARE_INSTALL_PREFIX=/usr/share \
    -DLIB_SUFFIX=64 \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
     -G Ninja

ninja
popd

%clean
rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_datadir}/vulkan/icd.d
mkdir -p %{buildroot}%{_libdir}

#mkdir -p %{buildroot}%{_sysconfdir}amd
#echo "MaxNumCmdStreamsPerSubmit,4" > %{buildroot}%{_sysconfdir}/amdPalSettings.cfg

%if 0%{?__isa_bits} == 64
    install -m 644 AMDVLK/json/Redhat/amd_icd64.json %{buildroot}%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
    install -m 755 xgl/build/icd/amdvlk64.so %{buildroot}%{_libdir}
%else
    install -m 644 AMDVLK/json/Redhat/amd_icd32.json %{buildroot}%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
    install -m 755 xgl/build/icd/amdvlk32.so %{buildroot}%{_libdir}
%endif

%files
%doc AMDVLK/LICENSE.txt AMDVLK/README.md AMDVLK/topLevelArch.png
%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
%{_libdir}/amdvlk*.so

%changelog
* Wed Feb 14 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.15-0.20180214.git56ae090

- pal: Program CHKSUM register with the value obtained from the pipeline binary for SPP.
- pal: Fix implicit prim shader controls.
- pal: Fix "all" null device creation to skip undefined devices
- pal: Adds "virtual" to some destructors.
- pal: Add new field in struct DynamicComputeShaderInfo to support LDS size update during binding compute pipeline.
- xgl: Enhance GFX9 support
- xgl: Texture filtering quality changes
- xgl: Sample mask input to fs shouldn't force per-sample execution
- xgl: Fix LLVM error when using both OpImageSampleDref* and OpImageSample* on the same image
- xgl: CPU optimization for Dota2: reduces the time spent in CmdBuffer::RPSyncPoint() and its callees from 3.1% to 0.4%.
- xgl: [LLPC] Enable fastMathMode for floating point
- xgl: [LLPC] Enable NoSignedZero for FP math to activate omod modifiers

* Sat Feb 10 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.14-0.20180210.git56ae090

- Initial package.
