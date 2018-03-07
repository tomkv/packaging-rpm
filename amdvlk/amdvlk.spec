%global amdvlk_commit       9215e86b5654fe5f20d8221ee137e16d6e63b739
%global llvm_commit         920c9e13bc68e638144d8eb84c5a6fa01ef947fb
%global xgl_commit          d62dbcce24a1332773f25ddf8d369ed80da0cc4f
%global pal_commit          b809c34bf6b2b703afcfd1be69050786e9a7b3d6
%global amdvlk_short_commit %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit   %(c=%{llvm_commit}; echo ${c:0:7})
%global xgl_short_commit    %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit    %(c=%{pal_commit}; echo ${c:0:7})
%global commit_date         20180307
%global gitrel              .%{commit_date}.git%{amdvlk_short_commit}

Name:          amdvlk-vulkan-driver
Version:       2.18
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

* Wed Mar 07 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.18-0.20180307.git9215e86

* xgl: Enable Vulkan 1.1 support
* xgl: Enable  VK_AMD_shader_core_properties extension
* xgl: Force per-sample shading if the shader is using per-sample features
* xgl: [LLPC] added addr space translation pass
* xgl: Handle OOM errors during command buffer recording
* pal: Fix the problem that driver unbinds vertex buffers when binding a new pipeline
* pal: Fix gpuProfiler crash when starting capture from first frame)
* pal: [gfx6] Update DB with correct address for PERFCOUNTERx_SELECT1 register,
       fixing GPU hang on issuing spm traces with more than 2 events for DB
* pal: Fix a CmdClearDepthStencil bug and adds validation to avoid 3D depth/stencil
       images
* pal: Expose perSampleShading PS parameter in PipelineInfo
* pal: Enable VmAlwaysValid feature for kernel 4.16 and above

* Tue Feb 27 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.16-0.20180227.git35bf91d

- pal: Fix vulkan CTS failures of dEQP-VK.api.external.memory.opaque_fd.dedicated
       with VM-always-valid enabled.
- pal: Fix a multi-thread segfault issue
- pal: Fix some Coverity Warnings
- pal: Improve CPU performance by removing read modify writes in
       CreateUntypedBufferViewSrds
- xlg: Complete Geometry shader and tessellation support for gfx9
- xlg: Clear v1.0 CTS failures for  Radeon™ RX Vega Series
- xlg: Generate extension related source files during driver building time
- xlg: Enable VK_EXT_depth_range_unrestricted extension
- xlg: Fix vrcompositor startup crash issue
- xlg: Fix random failure in AMD_buffer_marker tests
- xlg: Reduce time to clear AllGpuRenderState structure by removing
       Pal::DynamicGraphicsShaderInfos graphicsShaderInfo and
       Pal::DynamicComputeShaderInfo computeShaderInfo and making them local
       variables
- xlg: [LLPC] use PassManagerBuilder instead of a forked and modified copy of opt
- xlg: Vulkan queue marker to trigger RGP capture (Frame terminator)
- xlg: Re-order the PreciseAnisoMode enum for clarity; Change the
       PreciseAnisoMode value based on the public Radeon Settings Texture filter
       quality (TFQ) setting

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
