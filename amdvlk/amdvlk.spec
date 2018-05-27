%global amdvlk_commit       3540e83043efe2cdadce2fc4cd29b37f80ef6669
%global llvm_commit         f12ada52c53bcc0cd34376fe354dd9a93cb0dd31
%global xgl_commit          3ef40274448e9bce3e4a0658c3ed4335c3131ca7
%global pal_commit          ca2073448141cc14f4c5f3be3056dd7064bdc0ea
%global wsa_commit          c3ad69014e56f21a78a815e07a9834e1e5c22898
%global amdvlk_short_commit %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit   %(c=%{llvm_commit}; echo ${c:0:7})
%global xgl_short_commit    %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit    %(c=%{pal_commit}; echo ${c:0:7})
%global wsa_short_commit    %(c=%{wsa_commit}; echo ${c:0:7})
%global commit_date         20180525
%global gitrel              .%{commit_date}.git%{amdvlk_short_commit}

Name:          amdvlk-vulkan-driver
Version:       2.34
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

mkdir -p %{buildroot}%{_sysconfdir}/amd
echo "MaxNumCmdStreamsPerSubmit,4" > %{buildroot}%{_sysconfdir}/amd/amdPalSettings.cfg

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
%dir %{_sysconfdir}/amd
%config %{_sysconfdir}/amd/amdPalSettings.cfg
%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
%{_libdir}/amdvlk*.so
%{_libdir}/libamdgpu_wsa_*.so

%changelog
* Sun May 27 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.34-0.20180525.git3540e83

- xgl: Add fp16 interpolation intrinsics and register settings for
- xgl: AMD_gpu_shader_half_float
- xgl: Add extension VK_AMD_gpu_shader_half_float_fetch (not enabled)
- xgl: Support dual source blend on LLPC
- xgl: [LLPC]Enable on-chip GS by default for GFX6-8
- xgl: Check VkPhysicalDeviceFeatures2 on device create
- xgl: Barrier optimization: move decision about whether to apply layout
       transitions for this barrier in case of ownership transfers to the
       ImageBarrierPolicy class
- xgl: [LLPC] spir-v reader: fix clang compile error in image code
- xgl: Remove the support for PRT depth/stencil formats. Single-aspect
       depth and stencil are still supported
- xgl: Report per-aspect sparse image format properties for depth/stencil
- xgl: [LLPC] Fix an issue of MRT color out
- xgl: Simplify sparse texture bind virtual offset calculation
- xgl: Remove the implicit null sparse bind on queue 0
- xgl: Disable loop unroll for game TombRaider to work-around an issue
       that lighting is incorrect on main menu and in benchmark
- xgl: [LLPC]Support new dimension aware image instrinsics
        - Support general Fmask loading
        - Fix SubpassDataArray dimension in GL_EXT_multiview
- xgl: Fix assert caused by missing image layout in renderpass logger
- pal: Add IHashProvider and IHashContext to Util namespace
- pal: New a flag sampleLocsAlwaysKnown to enable defer MSAA depth expand
       optimization for GFX6~9
- pal: Null initialize the fmask srd if in CreateFmaskViewSrdsInternal()
       there is no fmask for the image
- pal: Fix the issue that VK_KHR_maintenance1 + sDMA queue: 2D Array
       image -> 3d image copy ops (and vice versa) does not work
- pal: Fix copies of BCn mip-levels where the HW determines the incorrect
       size of the mip level.

* Tue May 15 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.31-0.20180515.git3540e83

- xgl: Enable extension VK_KHR_display
- xgl: [LLPC]Add missing int64 function
- xgl: [LLPC]Support new dimension aware image instrinsics
        - Add runtime option to support switching between dimension aware
          image intrinsics and old image intrinsic
        - Add dimension aware version of fetch fmaskvalue,
        - Fix fmask loading failure in VulkanCTS
          dEQP-VK.amd.shader_fragment_mask group
- xgl: Expose the subgroup arithmetic capabilities
- pal: Pipeline stats crash the GPU profiler.
- pal: Only disable DE workload IB when PAL MCBP is off
- pal: Buffer->image copy op truncates output written to the image if a
       2D R32G32B32 linear 48x240 image is used.
- pal: Add new interface CmdDrawOpaque()

* Wed May 09 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.30-0.20180509.gite59fdd2

- xgl: Update Vulkan headers to 1.1.73
- xgl: Implement VK_EXT_descriptor_indexing (not enabled )
- xgl: [LLPC]Begin to add support  (ImageRead and ImageFetch) for
       dimension aware image intrinsics which is newly added in LLVM backend
       and will replace old hardware oriented image intrinsics
- xgl: [LLPC]Use wqm intrinsic for ds_swizzle derivatives
- xgl: [LLPC]Update SPIR-V header
- xgl: Fix bugs in fetch RGB10A2
- xgl: Barrier optimization, moving the responsibility of handling image
       layouts to the barrier policy classes
- pal: Set PARTIAL_VS_WAVE_ON to 1 for off-chip GS to work-around an
       issue of system hang
- pal: Remove support for image atomics from formats that should not
       support it
- pal: Remove the Per-Device Ring Buffers for CE RAM Dumps
- pal: Make Internal CE RAM Dumps Cacheline-Aligned
- pal: Fix GPU Scratch Memory Allocation Bug

* Sun Apr 29 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.29-0.20180429.gite59fdd2

- xgl: Enable AMD_shader_ballot and AMD_gpu_shader_half_float extension
- xgl: Expose the subgroup shuffle capabilities, implement  arithmetic
       16bit and 64bit operation
- xgl: Enable app_shader_optimizer in LLPC path
- xgl: Barrier optimization
- xgl: Workaroud TombRaider  third benchmark hang issue
- xgl: Fix allocation granularity issue
- xgl: Add max mask enum for ImageLayoutUsageFlags and
       CacheCoherencyUsageFlags
- xgl: Fix issues in FragColorExport::ComputeExportFormat()
- xgl: Remove 32-bit CTS workaround
- xgl: Set unboundDescriptorDebugSrdCount PAL setting to 0 to avoid CTS
       issues with using multiple devices through testing
- xgl: Fix the issue that driver reports currentExtent of (N, 0) on zero
       sized width/height surface;  According to Vulkan spec 1.1.70.1,
       currentExtent of a valid window surface(Win32/Xlib/Xcb) must have both
       width and height greater than 0, or both of them 0.
- xgl: Fix LLPC assert on image type
- xgl: Use runtime cache mode to get contextCache and reduce the time of
       running CTS tests
- pal: Command buffer dumping fixes,  provide the correct engine ID for
       SDMA command buffers
- pal: Set DropIfSameContext for the CE preamble stream.
- pal: Add max mask enum for ImageLayoutUsageFlags and
       CacheCoherencyUsageFlags
- pal: Fix assert and build error for PAL null device
- pal: Fix app crash when reading amdPalSettings.cfg
- pal: Fix source image descriptors for graphics depth/stencil copies.
- pal: Fix dEQP-VK.api.external.semaphore.opaque_fd.import_twice_temporary CTS
       test hang on Vega
- pal: Partially revert earlier change for clean-up of user data table
       management code. Most of the original change is not reverted, just the
       portion which moves some common structures from each HWL to the
       independent layer for universal command buffers. The compute command
       buffer changes were left as-is.
- pal: Moves the DescribeDraw calls after validateDraw in all CmdDraw calls
- pal: Implement support needed for KHR_Display extension

* Tue Apr 24 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.27-0.20180424.gite59fdd2

- xgl: Fix the issue of TombRaider, which causes Gpu hangs with the third
       benchmark.

* Sun Apr 22 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.27-0.20180422.gite59fdd2

- xgl: Enable extension VK_AMD_shader_image_load_store_lod
- xgl: Enable extension VK_AMD_gcn_shader
- xgl: Implement SYNC_FD handle type for External Fence and Semaphore.
- xgl: Implement subgroup arithmetic operations
- xgl: [LLPC] Add missing pipeline member in pipeline dump
- xgl: Optimize subgroup function name generating process, generate
       functions based on the subgroup arithmetic group op
- xgl: Remove releasing stack allocator in CmdBuffer::End()
- xgl: Set UseRingBufferForCeRamDumps default back to true
- xgl: No need to allocate memory for Sampler descriptors for all Gpus in
       the device group.
- xgl: Fix verification error using R32ui image format
- xgl: Fix pipeline compilation failure when running ManiaPlanet on Wine
- xgl: Fix and optimize the use of some of the barrier flags which were
       noted to be handled incorrectly or inconsistently
- pal: Enable SyncobjFence and choose which fence type to use during
       runtime
- pal: Expand reporting of CmdBindTargets in the logger
- pal: Enable support for IL_OP_LOAD_DWORD_AT_ADDR in ILP
- pal: Implement SYNC_FD handle type for KHR_EXTERNAL_SEMAPHORE_FD
- pal: Add logic to memtracker to detect when someone corrupts the
       allocation list by scribbling into the heap
- pal: Remove CE/DE counter syncs from the postamble command streams on
       gfxip8+
- pal: Fix the issue that vkAcquireNextImageKHR returning VK_TIMEOUT w/o
       waiting the timeout duration

* Mon Apr 16 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.25-0.20180416.gite59fdd2

- xgl: Reduce unnecessary malloc/free calls
- xgl: [LLPC] Change the undef value to 0 or 0.0 for those unsupported
       functions. This is because undef value will block constant folding in
       LLVM and the nested constant expression after lower will be
       time-consuming when backend does analysis
- xgl: [LLPC] Support int64 atomic operations
- xgl: Tweaks the way tha handles load op clears in renderpasses to fix too
- xgl: many barriers in render pass clear
- xgl: Add error handling where AddMemReference() is used; Add
- xgl: vk::Memory::CreateGpuMemory() and vk::Memory::CreateGpuPinnedMemory()
- xgl: Fix assertion when running DOOM 2016 in Wine
- xgl: Set "vm" flag for all fragment outputs
- xgl: Add FMASK shadow table support to the Vulkan Driver which changes
       descriptors are stored in memory. This allows writing the FMASK
       descriptors in the same corresponding upper 32 bits of the STA
       descriptors VA address
- pal: Fix missing cmd scratch memory heap in gpasession.  Prevents a
       divide by zero exception when initializing driver for RGP traces
- pal: Explicitly acquire and release ownership of the queue context in
       PAL's preamble and postamble command streams
- pal: PAL no longer try to chain from the last command buffer to the
       postamble command streams
- pal: Fix interfaceLogger access violation. DataAllocNames array does
       not match CmdAllocType enum.
- pal: VK_AMD_gpu_shader_int16 + VK_AMD_shader_trinary_minmax +
       GFX9:Graphics pipeline fails to create if functionality dependent on the
       two exts is used
- pal: Rewrite VamMgrSingleton to avoid static members
- pal: Clean-Up of User Data Table Management Code

* Mon Apr 09 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.24-0.20180409.gite59fdd2

- xgl: Add int16 support to AMD_shader_ballot and AMD_trinary_minmax extension
- xgl: [LLPC] Enable RetBlock in GS to make sure only one return is used in GS
- xgl: Refine Pipeline dump
       - Simplify pipeline panel options
       - Update variable name in llpcAbiMetadata.h to match
         palPipelineAbi original name.
       - Remove metadata name in RegNameMap, instead,
         Util::Abi::PipelineMetadataNameStrings is used.
       - Fix a bug in PipelineCompiler::ApplyBilConvertOptions, the
         return value of GetRuntimeSettings must be a reference
- xgl: AMD_shader_ballot:
       - Rename glslSpecialOpEmuF16 to glslSpecialOpEmuD16.
       - Add stubs of subgroup arithmetic operations for i64 and f16.
       - use tbuffer_load_d16 to do vertex fetching.
- xgl: Implement a consistent dispatch table mechanism across the driver
       - Now we have separate global, per-instance, and per-device
         dispatch tables
       - We can override individual entry points in each dispatch table
         to enable optimizations based on app profile or any other criteria
       - Entry points now can have complex requirement criteria and we
         now clearly distinguish between instance and device level
         functions
       - SQTT layer handling is still a bit clumsy because it operates
         more like a device-only layer, but at least it's injection code is
         less intrusive now
       - Also fixed a bunch of unrelated bugs and missing implementation
         on the way, as the new code revealed those
- pal: Update Pipeline Dump service to inherit from IService instead of
       URIService (which is deprecated and being removed).
- pal: Support marker offset for WriteMarker.
- pal: Changes ValidateDraw to reserve its own space rather than
       including it with the rest of the draw related packets. This avoids
       running out of reserved space in TimeSpy.
- pal: Move MetroHash and jemalloc to src/util/imported from src/core/imported.

* Tue Apr 02 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.23-0.20180402.gitae72750

- xgl:  Enable below extensions:
       - AMD_shader_explicit_vertex_parameter
       - AMD_shader_trinary_minmax
       - AMD_mixed_attachment_samples
       - AMD_shader_fragment_mask
       - EXT_queue_family_foreign
- xgl: Enable AMD_gpu_shader_int16 for gfx9
- xgl: Enable shaderInt64
- xgl: Disable extension  AMD_gpu_shader_half_float since the
       interpolation in FS is not implemented.
- xgl: Add arithmetic operations of AMD_shader_ballot
- xgl: Implement subgroup arithmetic reduce int ops
- xgl: Remove KHR suffixes for promoted extensions: replace some of the
       KHXs with KHRs, the rest should go away whenever device group KHXs are
       removed
- xgl: Remove Vulkan  1.0 headers because 1.1's are backward compatible,
       1.0 driver functionality can still be built with USE_NEXT_SDK=0
- xgl: Fix an issue that incorrect buffer causes compute shader loop
       infinitely
- xgl: Disable FmaskBasedMsaaRead for Dota2, which can bring ~1%
       performance gain for Dota2 4K + best-looking on Fiji:
- xgl: Add FMASK shadow table support to LLVM / LLPC
- xgl: Fix the issue that Wolfenstein 2 fails to compile compute shader
- pal: Fix dEQP-VK.api.image_clearing.core.clear_color_image.3d.* CTS
       tests failure
- pal: Eliminate Stalls Between Command Buffers, Phase #1
- pal: Clarifies an existing 3D color target interface requirement and
       fixes a bug which can cause DCC corruption.
- pal: Fix an issue related to fast clear eliminate
- pal: Do late expand for HTILE if it used fixfuction resolve

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
