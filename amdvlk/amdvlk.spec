%global amdvlk_commit       c38b52d299be3da8524dc4fb5c283e12177a4ab4
%global llvm_commit         9d63413d0223a53ff242ea6aa231e0e7fad87b0b
%global xgl_commit          baf3c1cfd0f037b3c25168c6d40de0e2151bcef7
%global pal_commit          bdeefc26995fb5b9196e67d16053febfd4ad63ba
%global wsa_commit          9fd92444855245a70be752d35c91fd3222009a33
%global amdvlk_short_commit %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit   %(c=%{llvm_commit}; echo ${c:0:7})
%global xgl_short_commit    %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit    %(c=%{pal_commit}; echo ${c:0:7})
%global wsa_short_commit    %(c=%{wsa_commit}; echo ${c:0:7})
%global commit_date         20180329
%global gitrel              .%{commit_date}.git%{amdvlk_short_commit}

Name:          amdvlk-vulkan-driver
Version:       2.21
Release:       0%{gitrel}%{?dist}
Summary:       AMD Open Source Driver For Vulkan
License:       MIT
Url:           https://github.com/GPUOpen-Drivers
Source0:       %url/AMDVLK/archive/%{amdvlk_commit}.tar.gz#/AMDVLK-%{amdvlk_short_commit}.tar.gz
Source1:       %url/llvm/archive/%{llvm_commit}.tar.gz#/llvm-%{llvm_short_commit}.tar.gz
Source2:       %url/xgl/archive/%{xgl_commit}.tar.gz#/xgl-%{xgl_short_commit}.tar.gz
Source3:       %url/pal/archive/%{pal_commit}.tar.gz#/pal-%{pal_short_commit}.tar.gz
Source4:       %url/wsa/archive/%{wsa_commit}.tar.gz#/wsa-%{wsa_short_commit}.tar.gz

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
BuildRequires: wayland-devel

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
%setup -q -c -n %{name}-%{version} -a 0 -a 1 -a 2 -a 3 -a 4
ln -s AMDVLK-%{amdvlk_commit} AMDVLK
ln -s llvm-%{llvm_commit} llvm
ln -s xgl-%{xgl_commit} xgl
ln -s pal-%{pal_commit} pal
ln -s wsa-%{wsa_commit} wsa

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

mkdir -p wsa/build && pushd wsa/build

cmake .. -DCMAKE_AR=`which gcc-ar` \
    -DCMAKE_NM=`which gcc-nm` \
    -DCMAKE_RANLIB=`which gcc-ranlib` \
    -DCMAKE_C_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_CXX_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
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
install -m 755 wsa/build/wayland/libamdgpu_wsa_wayland.so %{buildroot}%{_libdir}

%files
%doc AMDVLK/LICENSE.txt AMDVLK/README.md AMDVLK/topLevelArch.png
%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
%{_libdir}/amdvlk*.so
%{_libdir}/libamdgpu_wsa_*.so

%changelog
* Thu Mar 29 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.21-0.20180329.gitc38b52d

- wsa: New component Window System Agent, for Wayland support.
- xgl: Enable Wayland extension
- xgl: Implement below AMD extensions:
       - AMD_shader_fragment_mask
       - AMD_gcn_shader,
       - AMD_texture_gather_bias_lod
       - AMD_shader_trinary_minmax
       - AMD_shader_explicit_vertex_parameter
       - AMD_shader_ballot
       - AMD_texture_gather_bias_lod
- xgl: Enable subgroupQuadSwapHorizontal, subgroupQuadSwapVertical,
       subgroupQuadSwapDiagonal, subgroupQuadBroadcast(uint/int, uint)
- xgl: Enable support to group the devices if they have matching
       Pal::DeviceProperties::deviceIds,  pass CTS device group testing
- xgl: Hide VK_AMD_negative_viewport_height in Vulkan 1.1: using the
       extension is no longer legal, because 1.1 core includes
       VK_KHR_maintenance1
- xgl: [LLPC] make spir-v bool-in-mem i8 rather than i1
- xgl: Enable shader prefetcher for Serious Sam Fusion and Dota2, about
       2.5% performance gain
- xgl: Remove redundant divide in BindVertexBuffers() (PAL does the same
       divide). Remove extra bookeeping needed for the redundant divide
- xgl: Fix some issues in the RGP command buffer tag based capture code
- pal: Add Wayland support
- pal: Move Pipeline & User-Data Binding to Draw-Time, observed some nice
      gains in several applications, and other apps were neutral in terms of
      performance loss/gain
- pal: Fix an order of initialization issue related to public settings
- pal: VK_KHR_image_format_list for swapchains:  add the necessary PAL
       support for deciding image compression policy for presentable images
       based on a list of possible view formats
- pal: Report to clients that GFX OFF may reset the GFX timestamp to 0
       after an idle period
- pal: Fix some issues in command buffer dumping
- pal: Implement COND_EXEC style predication for CP DMA path in
       CmdCopyMemory on compute command buffers
- pal: Change CreateTypedBufferViewSrds() and
       CreateUntypedBufferViewSrds() to remove the requirement that the range is
       a multiple of the stride
- pal: Make Pal Linux VA manager support multi-device cases
- pal: Fix
       dEQP-VK.api.object_management.multithreaded_per_thread_resources.instance
       random crash
- pal: Fix validation bug with computing PBB bin sizes
- pal: Don't allow LayoutCopySrc on images of a format that doesn't
       support buffers
- pal: Fix issues  when grouping all identical devices into single device group
- pal: Add call to DevDriver ShowOverlay() function to determine if the
       developer driver overlay should be displayed.
- pal: Handle unaligned memory to image and image to memory copies on the
       DMA Queue
- pal: Convert some PAL inline utility functions into constexpr functions
       and fix some const-correctness issues.
- pal: Resolve potential HW bug with SDMA copy overlap syncs on GFX9
- pal: Temporarily disable the SDMA copy overlap sync feature on GFX9 for
       a suspected HW ucode bug with SDMA's ability to detect certain hazards
       which results in race conditions in SDMA stress tests.
- pal: Fix bug in PA_SC_MODE_CNTL_1 validation
- pal: Improve hotspots related to Color-Target & Depth/Stencil views,
       some improvements in CPU performance when creating color-target and
       depth-stencil view objects in PAL
- pal: Make GFX9's BuildSetSeqContextRegs() and BuildSetSeqConfigRegs()
       avoid reading from the command buffer similar to what is done for GFX6.
       Cleans up big spikes if Vulkan uses write combined command buffers (they
       were small bumps when using cacheable command buffers)

* Fri Mar 16 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.19-0.20180307.git9215e86

- xgl: Add Instance- and Device-specific dispatch tables. Comply with
       spec requirements.
- xgl: Handle unaligned memory to image and image to memory copies on the
       DMA Queue
- xgl: Use included headers to determine apiVersion instead of manual bumps
- xgl: Complete VK_EXT_sampler_filter_minmax extension, allows more
       formats and is completely driven by the formats spreadsheet
- xgl: VK_KHR_subgroup support:
        -  Add missing subgroup builtins in compute shader
        - Move the implementation of gl_SubGroupSize from patch phase to
          .ll library
        - Support for the shufflexor, shuffleup, shuffledown function
- xgl: VK_KHR_multiview support:
       - LoadOp Clears implementation
       - Rewrite the function ConfigBuilder::BuildUserDataConfig to
         support merged shader.
       - Adjust the position of SGPR to emulate ViewIndex.
       - Set the user data configuration of ViewId even if the stage is
         not the last vertex processing stage.
- xgl: Implement interaction between VK_KHR_multiview and
       VK_KHR_device_group by adding support for
       VK_PIPELINE_CREATE_VIEW_INDEX_FROM_DEVICE_INDEX_BIT.
- xgl: Change implementation of KHR_descriptor_update_template to move
       work from vkUpdateDescriptorSetWithTemplateKHR to
       vkCreateDescriptorUpdateTemplateKHR
- xgl: Batch large numbers of copy/clear/etc. image regions to avoid OOM
       errors
- xgl: Rearranged the loop in DescriptorSet::InitImmutableDescriptors()
       to avoid looking up the the descriptor sizes in the device unless
       necessary. Cuts time in DescriptorSet::Reassign() in half.
- xgl: Remove DescriptorSetHeap::m_pHandles. We can compute the handle
       with a little arithmetic instead of a memory lookup. Cuts the time in
       AllocDescriptorSets() in half.
- xgl: [LLPC]Implement sparse texture residency
- xgl: [LLPC]Fix Crash when parsing Hull Shader
- xgl: [LLPC]Fix problems with address space mapping
- xgl: [LLPC]Restored correct addr space for gs-vs ring buffer descriptor
       load
- xgl: Fix  an assert when running DOOM in Wine
- xgl: Fix 58 failures of vulkan-cts-1.1.0.3
- pal: Don't treat MSAA image as pure shader resolve/read src if CB fixed
       function resolve method is preferred
- pal: Implement the changes needed to change the fast clear code from
       the 3 special values ((0,0,0,1) , (1,1,1,1) and (1,1,1,0)) to
       ClearColorReg when we mix signed and unsigned formats views for a
       resource
- pal: Don't write IA_MULTI_VGT_PARAM and VGT_LS_HS_CONFIG in
       ValidateDrawTimeHwState
- pal: Remove unnecessary calls to SetContextRollDetected() during GFX9
       command buffer generation
- pal: Remove the software-based dynamic primgroup optimization on GFX9
- pal: Fix GpuProfiler ThreadTrace shader hashes. 64-bit to 128-bit
- pal: Optimize path with depth clamp disabled. Set
       DISABLE_VIEWPORT_CLAMP only if depth clamp is disabled in pipeline and
       depth is exported in fragment shader
- pal: Trace SQTT Causes Driver AV if sqtt.gpuMemoryLimit is Too Small
- pal: Update formats capable of min\max filtering

* Wed Mar 07 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.18-0.20180307.git9215e86

- xgl: Enable Vulkan 1.1 support
- xgl: Enable  VK_AMD_shader_core_properties extension
- xgl: Force per-sample shading if the shader is using per-sample features
- xgl: [LLPC] added addr space translation pass
- xgl: Handle OOM errors during command buffer recording
- pal: Fix the problem that driver unbinds vertex buffers when binding a new pipeline
- pal: Fix gpuProfiler crash when starting capture from first frame)
- pal: [gfx6] Update DB with correct address for PERFCOUNTERx_SELECT1 register,
       fixing GPU hang on issuing spm traces with more than 2 events for DB
- pal: Fix a CmdClearDepthStencil bug and adds validation to avoid 3D depth/stencil
       images
- pal: Expose perSampleShading PS parameter in PipelineInfo
- pal: Enable VmAlwaysValid feature for kernel 4.16 and above

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
