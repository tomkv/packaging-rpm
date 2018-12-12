%global amdvlk_commit       63811556d533858caba2b95ccf46a8a322363b1c
%global llvm_commit         0843ddd6f5a03468d42b90715e98e9798f772555
%global llpc_commit         27692580ad9eb4f173ad0c421c932d6dd4300184
%global xgl_commit          6df80a52773aa1126fd7518254fa4cc01d38b819
%global pal_commit          bf91cb29233ffceff95eb9ad16c6dc00b2029541
%global wsa_commit          f558403d3292039de4d17334e562bda58abfc72c
%global amdvlk_short_commit %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit   %(c=%{llvm_commit}; echo ${c:0:7})
%global llpc_short_commit   %(c=%{llpc_commit}; echo ${c:0:7})
%global xgl_short_commit    %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit    %(c=%{pal_commit}; echo ${c:0:7})
%global wsa_short_commit    %(c=%{wsa_commit}; echo ${c:0:7})
%global commit_date         20181212
%global gitrel              .%{commit_date}.git%{amdvlk_short_commit}

Name:          amdvlk-vulkan-driver
Version:       2.66
Release:       0%{gitrel}%{?dist}
Summary:       AMD Open Source Driver For Vulkan
License:       MIT
Url:           https://github.com/GPUOpen-Drivers
Source0:       %url/AMDVLK/archive/%{amdvlk_commit}.tar.gz#/AMDVLK-%{amdvlk_short_commit}.tar.gz
Source1:       %url/llvm/archive/%{llvm_commit}.tar.gz#/llvm-%{llvm_short_commit}.tar.gz
Source2:       %url/llpc/archive/%{llpc_commit}.tar.gz#/llpc-%{llpc_short_commit}.tar.gz
Source3:       %url/xgl/archive/%{xgl_commit}.tar.gz#/xgl-%{xgl_short_commit}.tar.gz
Source4:       %url/pal/archive/%{pal_commit}.tar.gz#/pal-%{pal_short_commit}.tar.gz
Source5:       %url/wsa/archive/%{wsa_commit}.tar.gz#/wsa-%{wsa_short_commit}.tar.gz

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
BuildRequires: libXrandr-devel
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
%setup -q -c -n %{name}-%{version} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5
ln -s AMDVLK-%{amdvlk_commit} AMDVLK
ln -s llvm-%{llvm_commit} llvm
ln -s llpc-%{llpc_commit} llpc
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
* Wed Dec 12 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.66-0.20181212.git6381155

- xgl: Update Vulkan headers to 1.1.94
- xgl: Use VK_DRIVER_ID_x in xgl for driver properties
- xgl: Enable primitiveUnderestimation capability of
       VK_EXT_conservative_rasterization
- pal: PCOM and Blt Shaders integration to mmpipelines in PAL
- pal: Remove call to WriteVsFirstSliceOffset() if the pipeline doesn't
       require it
- pal: Move the ownership of conservative rasterization register back to
       the MSAA state
- pal: Modify copybuffer byte and dword shaders to support a copy size of
       up to 4GB
- pal: Modify the RPM code to perform multiple smaller copies (of
       currently 16MB) in place of a single large copy and now it should
       be able to handle gpusize (64 bit) copy sizes
- pal: Fix Cube crash on debug version due to empty ShaderCacheFileDir
- pal: Fix GPU hang when Vulkan API accesses the stencil aspect of
       VK_Format_S8_Uint image explicitly
- pal: Fix mmVGT_GS_ONCHIP_CNTL access issue
- llpc: Merge tbuffer.store.i32 with tbuffer.store.v2i32 and
        tbuffer.store.v4i32, up to 5% performance gain for tessellation
- llpc: Enable the atomic optimizer
- llpc: Hook up Spirv Support for VK_KHR_shader_float_controls
- llpc: Fix compile error: non-scalar type cannot be used in a
        pseudo-destructor expression
- llpc: Rename PatchPrepareAbi to PatchPreparePipelineAbi
- llpc: Fix dxvk streamoutput11.exe on gfxip 8 and 9 cards for extension
        Ext-transformfeedback buffer
- llpc: Fix unused variable error in clang build
- llpc: Temp whole-pipeline passmgr fix for CTS 
        dEQP-VK.spirv_assembly.instruction.graphics.16bit_storage.struct_mixed_types.uniform_geom
        failure
- llpc: Remove conservative rasterization register from the pipeline ABI.
        This is now managed by PAL MSAA state

* Wed Dec 05 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.65-0.20181205.gitbb80191

- xgl: Enable VK_EXT_scalar_block_layout extension
- xgl: Enable VK_KHR_swapchain_mutable_format extension
- xgl: Enable on-chip GSVS ring on GFX9, seeing up to 10% performance
       gain
- xgl: Update base address offset calculation to be per device
- xgl: Use SW compositor path for MGPU in windowed modes
- xgl: Add missing files to CMakelist to fix undefined reference to
       vk::OverrideDispatchTable_ND(vk::DispatchTable*)
- xgl: Fix errors with multiple monitors and direct display
- xgl: Add dccBitsPerPixelThreshold setting
- xgl: Fix the issue that Pipeline keeps a reference to layout after it
       is created
- xgl: Fix dEQP-VK.api.device_init.create_instance_device_intentional_alloc_fail
       test failure
- xgl: Fix a crash issue on Raven caused by the implementation of
       VK_AMD_memory_overallocation_behavior extension
- xgl: Fix calculation of the pRegions offset in
       CmdBuffer::PalCmdResolveImage()
- pal: Change the unit of buffer-filled-size to bytes
- pal: Add an option to print all pipelines in GPUprofiler
       timingReport.py
- pal: Add the ability for certain settings to be reread from the
       registry/file
- pal: Implement Release-acquire based barrier
- pal: Add timeline_semaphore support
- pal: Clarify when .sgpr_limit and .sgpr_limit are written to pipeline
       metadata
- pal: Add 64-bit version of BitMaskScanForward
- pal: Add BitMaskScanReverse to optimize Log2 and Pow2Pa
- pal: In BitMaskScanForward, replace bsf with tzcnt
- pal: Replace some PsUsesUavs() checks in OOO prim and DFSM
       optimizations with PsWritesUavs(). Add PsWritesUavs,
       PsWritesDepth, and PsUsesAppendConsume fields to legacy pipeline
       metadata
- pal: [ThreadTrace] Change assert to an alert when the perf token is
       enabled in the token mask config
- pal: Remove Bundle State Inheritance
- pal: Add HawaiiPro to AsicRevision and NullGpuId
- pal: Change PBB alpha to mask condition check to also require MSAA log2
       samples > 0
- pal: Re-enable tracing of missing registers in thread trace
- pal: Don't initialize counters when not in a mode for counter collection
- pal: Remove some useless settings
- pal: Simplify unnecessary BitMaskScanForward, replace another use of
       BitMaskScanForward with Reverse in gfx9MetaEq
- pal: Change note namespace from "AMD" to "AMDGPU" to match HSA code
       objects.
- pal: Fix compile and link error with clang
- pal: Fix CopyTextureRegion failure when copying a MSAA Resource in
       D32_FLOAT or D16_UNORM to a R32_UINT format
- pal: Fix  GFX9: CB_DCC_CONTROL register is programmed incorrectly
- pal: Fix perf counter instance incorrect calculation
- llpc: Add implementation for VK_KHR_shader_float16_int extension
- llpc: Add implementation for transform feedback extension
- llpc: Rationalize LLPC's various ad-hoc pass managers into a single
        pass manager that runs on a single whole-pipeline LLVM IR module
- llpc: Ensure declaration attributes copied from external lib
- llpc: Ensure llvm.amdgcn.set.inactive is not marked readnone
- llpc: Remove unnecessary and illegal alloca in emulation functions
- llpc: Clear sets of unused values after use
- llpc: Remove +vgpr-spilling from default options as this is now always
        enabled in LLVM upstream
- llpc: Ensure llvm.amdgcn.set.inactive is not moved in control flow
- llpc: Avoid remembering view index value outside of IR
- llpc: Fix incorrect implementation of OpSubgroupAllEqual
- llpc: Fix clang unused variable error
- llpc: Fix  dEQP-VK.glsl.atomic_operations.*_*signed64bit_* failure on
        gfx7
- llpc: Fix some dodgy deleting of instructions in SpirvLowerAccessChain
- llpc: Fix ELEX crash with Steam Proton

* Tue Nov 20 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.63-0.20181120.git81fd878

- xgl: Enable sparse support by default
- xgl: Enable VK_AMD_memory_overallocation_behavior extension
- xgl: Enable degenerate triangles for conservative rasterizations
- xgl: Fix issue that can't clear a mutable format image
- xgl: Fix CTS memory.pipeline_barrier.transfer_dst_storage_image tests
       fail
- xgl: Fix MGPU asserts when creating graphics pipeline
- xgl: Fix issue that wrong target device ID passed to PAL
- xgl: Fix issue that dual source bend is being enabled when blending is
       disabled
- xgl: Add setting for exiting after compilation failure
- xgl: Update base address offset calculation to be per device
- pal: Hook up more pipeline ABI metadata fields
- pal: Shader prefetch updates, remove the PrefetchMgr entirely
- pal: Change a SparseVector assert to be more clear
- pal: Add a pair of more generic BuildReleaseMem and BuildAcquireMem
       functions
- pal: Fix a couple inconsistencies in platform settings
- pal: Fix copies of BCn mip-levels where the HW determines the incorrect
       size of the mip level
- pal: Check if pMsaaState is null to avoid possible access violate
- pal: Add parameters firstInstance and instanceCount to CmdDrawOpaque to
       support Vulkan API DrawIndirectByteCount
- pal: Fix GetPeerImageSizes relying on zero initialization of parameters
- pal: Fix a regression
       dEQP-VK.wsi.wayland.swapchain.create.min_image_count test crashes
- pal: Fix dependency on x11/xcb libraries even there is no x11/xcb
       surface created
- pal: Add setting CsCuEnLimitMask for limiting CUs enabled for compute
       shaders
- pal: Add the ability to dump debug stack traces
- pal: Update swap chain to handle VSync fullscreen present
- pal: Add ICmdBuffer::CmdSetBufferFilledSize
- llpc: Fix clang unused function warnings
- llpc: Fix clang unused-variable warnings
- llpc: Fix default output file extension for ISA asm output
- llpc: Build emu lib with opt -strip
- llpc: Set default -log-file-dbgs to "" (meaning stderr): this brings
        amdllpc into line with other LLVM tools.
- llpc: Implement transform_feedback support
- llpc: Fix a typo to calculate ldsSizeDwordGranularity for on-chip ESGS
        ring on GFX9
- llpc: Correct minor issues for inline constant
- llpc: Add proper type mangling to llpc builtin and generic functions

* Thu Nov 08 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.61-0.20181108.gitb15aaf9

- xgl: Implement VK_EXT_inline_uniform_block
- xgl: testShaders.py: don't use amdllpc -auto-layout-desc
- xgl: Add script for lit test
- xgl: Add panel setting for debugging shader
- pal: Add SamplerInfo::disableSingleMipAnisoOverride flag to allow
       client have control over this Sampler optimization when creating
       Sampler SRDs
- pal: Clean up some old code in PAL related to state inheritance
- pal: Move SyncReqs determination code from RPM to barrier functions
- pal: Refine wayland window system support (last change)
- pal: Fix CB_DCC_CONTROL register is programmed incorrectly
- pal: Fix barrier secondary buffer test failure
- pal: Make setting to test lateAllocVs behavior
- pal: Fix empty perf traces under gfx9
- pal: Fix external_memory_host.bind_image_memory_and_render tests
       failing on Vega10
- pal: Fix GFX9's hardware specific CmdBarrier functions forgot to call
       its base function
- pal: Refactor thread trace token mask interface
- pal: [GpuProfiler] Fix ThreadTraceViewer CRCs for full frame captures
- llpc: cmake: fix dependencies for emulation library
- llpc: Tidy amdllpc's use of spvgen
- llpc: amdllpc switched to using static vfx library
- llpc: Remove need for -auto-layout-desc option
- llpc: New -verify-ir option: This option adds a verify pass after each
        pass in the LLPC compilation process
- llpc: Fix clang warnings

* Fri Oct 26 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.60-0.20181026.git96a0ad8

- xgl: Support swapchain composite alpha
- xgl: Fix crash when running Killer Instinct with Steam Proton
- xgl: Fix testShaders.py to not depend on AMDLLPC SUCCESS message
- pal: Change CreateBvhSrds() to allow for a NULL GPU memory object when
       useZeroOffset==1
- pal: Refine wayland window system support in PAL
- pal: Remove dx9Mipclamping from SamplerInfo and keep MIP_POINT_PRECLAMP
       = 0
- pal: Add swapchain composite alpha support
- pal: Fix packet files RELEASE_MEM missing ordinal2 fieldname
- pal: Remove support for view 3d as 2d array
- pal: [GpuProfiler] Add support for injecting pipeline and shader hashes
       into ThreadTraceViewer thread traces
- pal: Unset color flag for block-compressed format
- pal: Fix clears of 32-32-32 format images.  Address library computes
       the dimensions of a 96bpp surfaces as if were a 3xWidth 32bpp
       surface, which is happily just what we need to do image clears
       instead of buffer-based image clears
- llpc: Fix an issue that loop invariant code motion does not work in
        certain cases when there are multiple push constant, seeing ~13%
        performance gain in  Serious Sam Fusion 4k - Low setting
- llpc: Fix llvm.amdgcn.fmed3.f16 doesn't work on gfx8, use min/max to
        emulate it
- llpc: Move lowering optimizations to after patch phase
- llpc: Enable building amdllpc on clang, including MacOS
- llpc: Compile multiple pipelines in the same context
- llpc: amdllpc do not output 'AMDLLPC SUCCESS' when -enable-outs=false
- llpc: Enable asserts on debug build of amdllpc
- llpc: enable-outs now defaults off. -v is an alias for it
- llpc: amdllpc -emit-llvm now outputs .ll not .bc

* Fri Oct 19 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.59-0.20181017.gite718bcf

- xlg: Update Vulkan headers to 1.1.86
- xlg: Enable VK_KHR_shader_atomic_int64 extension
- xlg: Enable VK_GOOGLE_decorate_string and VK_GOOGLE_hlsl_functionality1
       extension
- xlg: Use VK_KHR_image_format_list to set PAL flag noStencilShaderRead
- xlg: Add driver software compositor
- xlg: Add code object API Loader Events chunk to RGP traces
- xlg: Remove VK_KHX_device_group
- xlg: Fix MGPU Present Caps / Surfrace Modes
- xlg: Reserve ALL Mode for Querying Targets
- xlg: Implicit fullscreen mode optimization/cleanup
- xlg: Remove support for 3D PRT BC 128-bit block-compressed formats
- pal: Refine wayland window system support in PAL
- pal: Add Indirect Function Support to PAL
- pal: Improve CPU performance hotspots that a large amount of time was
       spent in a few CmdUtil functions that RMW command memory
- pal: Improve handling of scratch memory in PAL
- pal: Change MaxOutputSlots to 32+6
- pal: Updates flags for bitmask settings to allow the RDP UI to
       display/modify them properly
- pal: Add implicit fullscreen exclusive mode query
- pal: Add code object API Loader Events chunk to RGP traces, Part 2 of 2
- pal: Always enable, disable SQG events in SPI_CONFIG_CNTL for
       gfx9PerfExperiment
- pal: Add the support for rotated copy in graphics scaled copy path
- pal: Enable gamma conversion in graphics scaled copy path
- pal: Handle failure better while dumping command buffers
- pal: Update to view3dAs2dArray
- pal: Implement a PAL_NOT_IMPLEMENTED() in the CmdBufferLogge
- pal: Flush DB data and meta cache in case CmdClearDepthStencil of
       rsrcProcMgr.cpp take graphic engine based fast clear
- pal: Avoid crashing if the shaderDbg.cfg file is not available and add
       the option to only trace a specific number of draws per command
       buffer
- pal: Improve GpaSession handling of per-draw granularity performance
       counters
- pal: Adds State field to the settings JSON schema to indicate to the
       tool which driver state the settings can be changed during
- pal: Allow calling TemporarilyHangTheGpu() debug feature from non
       hw-specific classes
- pal: Add more null devices, one for each AsicRevision not already
       represented. Change some GFXIP stepping versions to match the
       latest version of HSA's table
- pal: Fix GpuMemory leak in GpaSession
- pal: Fix User-Data Management when finishing an RPM blit
- pal: Fix gpuProfiler crash when both perfcounters and sqtt are enabled
- pal: Fix an issue with the load index context register path that was
       affecting GFX9 asics
- llpc: Add support for VK_KHR_shader_atomic_int64
- llpc: Support .raw.buffer and .struct.buffer
- llpc: Fix  error on ICompiler::Create for 2 different GPUs
- llpc: [dxvk/wine] Fix Final Fantasy XII  missing text
- llpc: Fix peephole crash in the Witcher 3
- llpc: Remove sample_lz optimization since it is implemented in LLVM
- llpc: Fix intermittent assert on gfx9
- llpc: Switch emu lib to an archive of bitcode modules

* Sat Sep 29 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.55-0.20180929.gite718bcf

- xgl: Enable VK_KHR_driver_properties extension
- xgl: Implement VK_KHR_shader_atomic_int64 extension
- xgl: Add MGPU support to DynamicDescriptorData. The second GPUs VA's
       dynamic descriptor data was getting bound for the first GPU
       causing a PageFault
- xgl: Fix vkGetPhysicalDeviceSurfacePresentModes
- xgl: Fix corruption observed in game Just cause 3 + dxvk
- xgl: Allow mapping the memory on device index > 0 in device group
- xgl: Remove the redundant device group loop from vkCmdFillBuffer
- xgl: Refine the implementation of GetRandROutputDisplay
- xgl: Add a panel setting to drop the instruction in pipeline binary
       specified in order to debug the shader quickly
- pal: Implement direct display for console mode
       - Get the drm file descriptor from device while there is no leased
         screen
       - Find a proper crtc (the old one or an idle one) right before set
         mode
- pal: Refine the interface for screen to simplify the interface of
       palScreen, and remove the un-necessary properties
- pal: Investigate DATA_AND_OFFSET mode for LOAD_*_REG_INDEX, Part #1
- pal: Add code object database chunk to RGP traces. Part 1 of 2
- pal: Update NULL device names to include compute capability
- pal: In NullGpuId::All mode, create the last MaxDevices null devices in
       the enumerated list
- pal: Add new query to obtain the PCI bus id for a physical device
- pal: Add dest color key and src alpha blend support in graphics scaled
       copy path and enable the path
- pal: Pipeline reinjection
- pal: Support YCbCr plane of UYVY and YUY2 color filling
- pal: Hook up new dev mode platform halt point and creates platform
       settings component
- pal: Merge VS and PS Pipeline Chunk Classes in Gfx9 HWL
- pal: Remove QueryResultWait requirement (just to eliminate the
       assertion) for streamout stats query and add wait support in
       ComputeResults
- pal: Increase cache line size for Gfx9
- pal: Change DCC UAV support
- pal: Fix incorrect GpaSessionFlags reserved bit count
- pal: Fix the memory leak when the exception/error cause the trace
       capture to be aborted
- pal: Fix undefined symbol: AddrCreate with debug driver
- pal: Add panel setting to allow for restricting DCC to surfaces with a
       minimum BPP
- pal: Fix RGP profiling regression caused by full screen metadata
       feature enable
- pal: Add setting to never set clock values
- pal: [GPUProfiler]Do more perfcounter error handling
- pal: Add setting to disable XOR modes for AddrMgr2
- llpc: Replace buffer.load intrinsic with raw.buffer.load intrinsic in
        GS off-chip path
- llpc: Add peephole optimizations for PHI's & vector operations, up to
        6% performance improvement
- llpc: Fix CTS ssbo, ubo test failures
- llpc: Fix sparse bindings/residency: texture gather operations doesn’t
        work correctly
- llpc: Fix FP16 support issue for GFX8
- llpc: Fix several crash/hang issues for running games on dxvk
- llpc: Code Refine
        - Add certain rsState fields to hash calculation. This is missing
        - Rename files PassPeepholeOpt to SpirvLowerPeepholeOpt
        - Rename files PassLoopUnrollInfoRectify to
          SpirvLowerLoopUnrollInfoRectify
- llpc: Correct some coding comments
- llpc: Remove option -enable-dim-aware-image-intrinsic and all related
        LLVM IR functions

* Wed Sep 12 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.52-0.20180912.gite57ec8c

- xgl: Don't use LayoutShaderFmaskBasedRead for depth/stencil images
- xgl: Reduce size of Buffer object, remove fields that aren't necessary,
       merge three flags members into one,  lowers size from 168 bytes to
       88 bytes for single GPU.
- xgl: Check settings before using the passed in pPipelineCache argument
       during compilation, otherwise application calls to
       vkCreatePipelineCache override panel/registry keys to disable
       shader caching
- xgl: Remove DOTA 2 APU workaround since Valve has fixed this and will
       now consider system ram when determining the size of the texture
       pool on integrated GPUs
- xgl: Fix the issue of vkGetDeviceQueue2 crash and incorrect behavior
- xgl: Fix sign-compare compiling issue
- xgl: Reduce size of Image class from 288 bytes to 136 bytes
- pal: Implement  a graphics path for scaled copy in PAL.  There are some
       CTS failures, so force to use computer path for scaled copy first
- pal: Change the different cull modes to enable masks so that we can
       enable on a per-pipeline type.
- pal: Fix the issue that GpuProfiler return zero when getting GPU
       counters for Vega10/Vega12/Raven
- pal: Pipeline/code object metadata refactoring using MsgPack
- pal: Fix segfaults on gpuProfiler/RDP
- pal: Speed up gpuProfiler SQTT dumps
- pal: Move GpuProfiler granularity from GpuProfilerPerfCounterConfig to
       GpuProfilerConfig as it is applies to traces as well
- pal: Remove setting to gather global perf counter per instance since
       the config file now determines this behavior
- pal: Enable direct display for console mode
- pal: Change AmdGpuMachineType to be uint8-based. Interpret only the
       first byte of ELF header e_flags as this enum
- pal: Fix a memory segfault issue when running PRT on SRIOV
- pal: Fix some CTS failures for vega12
- pal: GpuProfiler: increase max TargetCmdBuffer allocator size
- pal: Remove support for graphics-only command buffers from PA
- llpc: Fix the issue of "No data written to a non-zero color attachment
        if previous attachments are not bound image views"
- llpc: Fix amdllpc test, option AutoLayoutDesc is dependent on the
        inOutUsage.fs.cbShaderMask from LowerResourceCollect
- llpc: Support PAL new metadata format in Vulkan and dump pipeline with
        new PAL metadata format
- llpc: Set allowContract and allow reassociation by recursively search
        user functions for fadd

* Sat Sep 01 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.51-0.20180830.git3775c7f

- xlg: Update to VulkanSDK 1.1.82
- xlg: VK_KHR_create_renderpass2 and VK_KHR_8bit_storage are now in
       public headers, remove the header files under devext.
- xlg: Added support for VK_EXT_conservative_rasterization, only
       "Primitive overestimation" feature is supported.
- xlg: Fix dereference of
       pDeviceGroupRenderPassBeginInfo->pDeviceRenderAreas when
       pDeviceGroupRenderPassBeginInfo->deviceRenderAreaCount == 0
- xlg: VK_EXT_descriptor_indexing: support non-uniform flag in image and
       atomic operations.
- pal: Fix F1 2017 Corruption observed while running benchmark
- pal: Fix assertion in RsrcProcMgr::CopyImageCompute()
- pal: [DbgOverlay] Fixes invalid gpu time in Debug overlay.
- llpc: Fixed uniform_buffer_dynamic_array_non_uniform_access_* test
        failures issues on GFX6.
- llpc: Moved translator files to match upstream Khronos
        spirv-llvm-reader

* Fri Aug 24 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.50-0.20180824.git3775c7f

- xgl: Set sampleLocsAlwaysKnown flag for PAL images. This enables a PAL
       optimization to skip/defer any MSAA depth decompress until resolve
       (where the sample pattern must now be provided)
- xgl: Support for 64-bit hash input to OverrideShaderHashUpper/Lower
- xgl: Fix build failure after make clean
- pal: Add vega12 support
- pal: Allow linear even if the image type was requested to be optimal. 
       There are cases where the only choice is linear
- pal: [GpuProfiler] Fences used by GpuProfiler not reset before re-use
- pal: DB_SHADER_CONTROL causing excessive context rolls
- pal: Remove unused IL Opcodes
- pal: PAL fence refactoring (phase 1)
- pal: Pick addrlib fix to fix WGF11ResourceAccess -11on12 failures
- pal: Use the real definition of DISABLE_CONSTANT_ENCODE_REG since we
       now have chip headers that define it correctly
- pal: Added support for VK_EXT_conservative_rasterization extension
- llpc: Add Vega12 support
- llpc: Educate LLPC on choosing better loop trip counts for loop
        unrolling  (Note: The change causes some performance drop in Dawn
        of War 3, will be fixed in next drop)
- llpc: Fix crash issue when running Doom with wine/dxvk
- llpc: Move the GroupOp Code of glslSpecialOpEmu.ll  to glslGroupOpEmuxx.ll
- llpc: Fix amdllpc compile warning-as-error with clang

* Sat Aug 18 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.49-0.20180817.git40b2f81

- xgl: Refine WriteFmaskDescriptors and CopyDescriptorSets for fmask
- xgl: Enable non-uniform indexing support for VK_EXT_descriptor_indexing
- xgl: Add debug support with  pipeline binary replacement
- xgl: Update PAL Interface in Vulkan to 424
- xgl: Fix a potential build dependency issue of strings.cpp
- xgl: Fix flag externalOpened is misused, it only needs to be set in
       open path
- xgl: Fix sparseAddressSpaceSize physical device limit
- xgl: Add some shift op tests to shaderdb
- xgl: Disable jemalloc from CMake
- pal: Change GpuProfiler setting name enumerations to be more readable
       and remove a redundant setting.
- pal: Don’t use raw copy when pal format is match but swizzle is not
       matched.
- pal: Update ICompiler interface to add OverrideCreateInfo entry points
       and add settings URI service support
- pal: [Raven] - Support UMC block perfcounters
- pal: Recommend more sensible heaps for query pools
- pal: Implement MemoryCacheLayer for PAL cache layer system
- pal: Minor profile and shader dumping fixes
- pal: Fix overhead of RGP capture in some applications.
- pal: Fix VK_AMD_shader_info is broken on top of PAL NULL backend
- pal: Fix device groups enumeration for mGPU support
- pal: Remove imported Jemalloc from Pal
- pal: Disable multisampled and depth/stencil PRT features
- pal: Bump version number to 174
- llpc: Support non-uniform descriptor index for store operations
- llpc: Remove format A8B8G8R8_SRGB_PACK32 from support list in LLPC;
        Disable A2B10G10R10 patch on gfx9
- llpc: Support pipeline binary replacement
- llpc: Fix a witcher3  crash issue
- llpc: Set shaderCacheFileDirOption to "-shader-cache-file-dir=."  if no
        environment variable is set
- llpc: Add Wave32 support in subgroup arithmetic code path
- llpc: Use python to generate subgroup arithmetic Op wrapper code
- llpc: Replace  spvCompileAndLinkProgram with
        spvCompileAndLinkProgramWithOptions, and enable EOptionDebug in
        default
- llpc: Support re-parse command options in Llpc::Compiler.  It only
        works when all compiler instance are destroyed
- llpc: Add dump compiler option in LLPC
- llpc: Remove AcquireContext in Llpc::Compiler::Compiler()
- llpc: Move verifySpirvBinary from ValidatePipelineShaderInfo to
        BuildShaderModule
- llpc: Add ShaderCacheManager::Shutdown to fix the memory leak in
        amdllpc

* Wed Aug 15 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.47-0.20180815.git402097f

- xgl: Fix setting of pQuadSamplePattern in RPSyncPoint().
- xgl: Add option to prefix cache and debug file paths
- pal: Fix the reading of the NggMode register
- pal: Fix that Bristol's queue 1 is non-functional
- pal: Fix some issues in Util::IsKeyPressed implementation. Now GPU
       profiling could be triggered by pressing shift-F11
- pal: Updates ISettingsLoader interface to remove Device dependency and
       to use IndirectAllocator
- pal: Clean up Linux VA partition initialization
- pal: Fix handling of OS specific #if blocks in auto-generated settings
       code.  Some default values were not being set when other fields in
       the same structure had OS specific defaults
- pal: Fix InterfaceLogger crash due to mismatched function locations and
       invalid Init call.
- pal: Fix mistake made in rename of palSettingsLoaderImpl.h to
       palSettingsLoader.cpp
- pal: Upgrade gpuopen
- wsa:  Fix file descriptor leak issue.
- llpc: Add some workarounds
- llpc: Add NGG state
- llpc: Change the setting of pipeline cache and dump file paths
- llvm: Revert "xfailed test for [AMDGCN] InstCombine work-around"
- llvm: Re-enable image inst_combine 
- llvm: Extra waterfall test for multiple readfirstlane intrinsics. Make
        sure that the waterfall intrinsic clauses support multiple
        readfirstlane intrinsics.

* Fri Aug 03 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.46-0.20180803.git402097f

- xgl: Enable VK_KHR_8bit_storage extension
- xgl: Set GpaSession queue timing flag
- xgl: Revert a previous  change which changed RenderPass::m_createInfo
       from including the structure in the class to including a pointer
       to the structure.  Change it back to avoid a step through memory
       when accessing it
- xgl: Fix bugs in testShaders.py: compile_name is not set in asyc
       process; crash when shader number is less than 8
- pal: Add option to prefix the ICD's multiple debugging paths
- pal: Use BitMaskScanForward instead of log2 for power-2 numeric
- pal: Move non-uniform table nodes to a separate client populated array
       instead of inlined in user data node list
- pal: Fix an issue for MGPU that
       vkGetPhysicalDeviceXlibPresentationSupportKHR returns false when
       presentation is supported
- pal: Increase the MaxOutputSlots from 33 to 37: There are up to 5
       built-in variables which export to position buffer, so the total
       output should be (32+5)
- pal: Bumps RGP file version to 1.1 so back end can detect the prior
       addition of the ETW queue semaphore data flag
- pal: Switch some code to more Cpu-friendly in hotspot functions
- pal: Refine WaitForCompletion for Wayland support,  let wsa to wait
       event to fulfill doWait requirement
- pal: Fix memory error handling
- pal: Update implementation for VK_EXT_acquire_xlib_display extension
       - Don’t build lease-related functions if the xcb-randr dev package
         used for driver build doesn’t support lease
       - Dri3WindowSystem::AcquireScreenAccess returns error if lease is
         not supported at runtime
- pal: Implement Util::IsKeyPressed
- pal: Properly initialize and enable stalls when SQTT fifo is full
- pal: Fix some compile and runtime issues with the ShaderDbg logic
- pal: Clean-up code for LOAD_*_REG_INDEX on Gfx9+
- pal: Replace numTotalRbs with numActiveRbs in
       Gfx9RsrcProcMgr::HwlBeginGraphicsCopy in case some Rbs are
       disabled
- pal: Settings Refactor - convert the legacy settings config files to
       the new JSON format that is used by the DevDriver settings service
- pal: Fast clear eliminate performance optimization
- llpc: Support VK_KHR_8bit_storage
- llpc: Begin to add dpp (data parallel primitive) support for gfxip8/9
- llpc: Fix failure to parse some bad SPIR-V

* Wed Jul 25 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.44-0.20180725.git402097f

- xgl: Disable memory clause formation if forcing si-scheduler
- xgl: Change the type of ConnectorId from int32 to uint32
- xgl: vkUpdateDescriptorSetWithTemplate(): move the loop over the GPUs
       into the UpdateEntryXXX() functions. This avoids having to pass
       the device index to each UpdateEntryXXX() function and makes the
       loop over the number of GPUs a compile time loop which simplifies
       the code that is generated
- pal: Update timingReport.py script
- llpc: Move some functions in llpcInternal.h/.cpp to other proper files
- llpc: Refine  register settings
- llpc: Fix dEQP-VK.spirv_assembly.type.scalar.u16.switch_* failure
- llpc: Implement non-uniform descriptor index support
- llpc: Add an option to do dynamic loop unroll
- llpc: Fix dxvk: F.E.A.R. 3 black screen in menu

* Sat Jul 21 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.43-0.20180721.git402097f

- xgl: Enable general variable pointer support
- xgl: Enable VK_KHR_create_renderpass2 extension
- xgl: Enable  VK_KHR_get_display_properties2 extension
- xgl: Add a runtime setting (OptEnablePrt) to enable PRT feature
- xgl: Add support for non-MSAA programmable sample locations
- xgl: Add support for non-0 defaultIndex for memory object allocated in
       device group.
- xgl: Use thin tiles for non-standard 3D PRT 64-bit format images
- xgl: Don't use LayoutShaderFmaskBasedRead for depth/stencil images
- xgl: Fix compile error with clang.
- xgl: Fix device groups enumeration: use GetMultiGpuCompatibility() to
       check for mGPU support.
- xgl: Fix memory error handling
- xgl: Add option to control zero-initialization of IL registers
- xgl: Dota2: Enable ReZ for several G-Buffer shaders on Ellesmere
- xgl: Report VK_ERROR_OUT_OF_DEVICE_MEMORY once heap size is exceeded.
       Currently the feature is hidden behind the
       MemoryEnableExternalLocalTracking panel setting
- pal: Correct logic for CreatePlatformKey() argument validation
- pal: Use thin tiles for 3D PRT 64-bit format images
- pal: Add support for non-MSAA programmable sample location
- pal: Refine code and fix issue for PRT support
- pal: Fix soft hang in EQP-VK.wsi.wayland.swapchain.render.basic
- pal: Fix initialization of indirect user data table pointer
- pal: Fix MGPU support
- pal: Adjust code to fit new Wayland window system interface definition
- pal: Disable the workaround for delayed reserve of PRT VA Range
       starting from version 2.27 of amdgpu kernel module or version 4.18
       of Linux kernel
- pal: Change FCE optimization to remove CPU perf hotspot due to memset
- pal: Remove PAL setting forcedUserDataSpillThreshold
- pal: Fix build error when comparing int32 with uint32
- pal: Fix build and link error with clang
- llvm: Part of the adjustCopiesBackFrom method wasn't correctly dealing
        with SubRange intervals when updating.
- llpc: Add general variable pointer support
- llpc: Enable new dimension aware image intrinsic by default
- llpc: Add i32 format integer gather patch to dimension aware intrinsic
        path
- llpc: Enable ReZ support
- llpc: Fix GL_AMD_gpu_shader_int16 + GL_AMD_shader_ballot interaction
        issue: various GLSL functions return invalid output
- llpc: Fix PushConstants issue
- llpc: Refine ELF dump related code
- wsa: Fixed the soft hang issue of CTS
       dEQP-VK.wsi.wayland.swapchain.render.basic
- wsa: Fixed the issue that assert is not triggerred properly with debug
       driver.

* Mon Jul 16 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.41-0.20180716.git402097f

- xgl: Enable VK_EXT_direct_mode_display extension
- xgl: Implement VK_EXT_acquire_xlib_display extension
- xgl: Enable variable pointer of storage buffer
- xgl: Update Vukan headers to 1.1.77.0
- pal: Direct rendering display support
- pal: Add image usage flag to make 3d arrays work when accessed as 2d
- pal: Add a counting suffix to the end of every layer's per-platform
       logging directory to prevent collisions when PAL is recreated in
       less than a second.
- pal: Move WAIT_CE_COUNTER To Immediately Before Draw
- pal: Disable Write Confirm for CPDMA Shader Prefetch
- pal: Expose the feature of gathering different global perf counter per
       block instance through gpu profiler
- pal: Fix the command buffer IDs in the Gpu Profiler and Cmd Buffer
       Logger layers.
- pal: Fix issue that clSVMAlloc is failing to create allocations greater
       than 2GB on Vega10
- llpc: dxvk: F.E.A.R. 3 black screen in menu #39
- llpc: Implement variable pointer of storage buffer
- llpc: Add integer gather patch for i32 resource format
- llpc: Fix DXVK flickering garbage issue
- llpc: Extract 6 low bits from 1D offset since we translate 1D texture
        to 2D on gfx9
- llpc: Fix some 64-bit case failures in dEQP-VK.spirv_assembly.type.*
- llpc: Fix clang compile error in image code
- llpc: Fix some Renderpass attachment_write_mask test failures
- llpc: Sync LLPC translator source code with upstream

* Mon Jul 02 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.40-0.20180702.gitdbb9dda

- xgl: Separate LLPC to https://github.com/GPUOpen-Drivers/llpc
- xgl: Enable EXT_vertex_attribute_divisor extension
- xgl: Enable EXT_descriptor_indexing extension (limited to dynamic
       indexing)
- xgl: Enable VK_KHR_draw_indirect_count  extension
- xgl: Update Vulkan headers 1.1.76
- xgl: Increase reported mip tail size to match Addrlib alignment
       requirements (3D PRT)
- xgl: Zero-initialize data in Semaphore
- xgl: Refactor the device group resource binding logic
- xgl: Add device group for semaphore
- xgl: Clean up PRT CTS test failures
- xgl: Idle time in between submits during RGP capture
- xgl: Remove the copy in GetSparseImageFormatProperties2
- xgl: Change barrier policy to handle 3 aspects - in case of YUV images
- xgl: Add FS2 support and some colorspace and transfer function tweaks
- xgl: Barrier optimization: add per-queue family policies to limit the
       scope of buffer and image memory barriers to those applicable to
       the specified queue family.
- xgl: Remove DescriptorSet::m_pPool sine it is only used in Destroy()
       and Destroy() is never called
- xgl: Fix an issue that vkCmdPipelineBarrier calls which only define
       execution dependencies are ignored
- xgl: Make sure DescriptorSet::dynamicDescriptorData is 64 bit aligned.
- xgl: Skip the subpass self-dependencies
- xgl: Pass fmaskBasedMsaaReadEnabled and robustBufferAccess  as template
       parameters to avoid using space in each descriptor set.
- xgl: Ordered Approach to App Detection
- pal: Fix pEngineInfo->sizeAlignInDwords evaluation
- pal: Disable degamma for sRGB source images when executing
       vkCmdColorSpaceBlitImageAMD
- pal: Add Util::Event::Wait and remove the unused Util::WaitForEvents
- pal: vk_Interop support: waite on a master fence whose OPAQUE_FD
       payload has been reset by waiting on a "user" fence succeeds as if
       it were still signaled
- pal: Use virtual page size instead of buffer size to map/unmap External
       Physical buffer. For External Physical memory, free marker before
       freeing its surface
- pal: Add a script timingReport.py which could be used to analyze GPU
       profiling result to identify top pipelines
- pal: FastClearEliminate optimization for performance
- pal: Fix F1 2017 Corruption observed while running benchmark
- pal: Add SyncobjFence created with FENCE_CREATE_SIGNALED_BIT
- pal: Add a workaround for the issue that amdgpu doesn’t synchronize PTE
       updates
- pal: Fix several device group PRT test failures

* Sun Jun 10 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.36-0.20180608.git0615262

- xgl: Add Barrier optimization to avoid unnecessary cache
       flushes/invalidations in case of ownership transfer barriers
- xgl: [LLPC]Default enable new LLVM dimension aware image intrinsics
- xgl: Add MGPU support for VkDeviceGroupBindSparseInfo. Sparse binding
       with resourceDeviceIndex != memoryDeviceIndex still doesn't work
       correctly. The root cause wasn't found yet
- xgl: [LLPC] Add an option to set loop unroll count
- xgl: Fix an issue for sparse texture support that gather component is
       not correctly passed to dmask
- xgl: Fix dEQP-VK.pipeline.push_constant.graphics_pipeline
       .overlap_4_shaders_vert_tess_frag failure on Vega10
- pal: Fix an issue that clSVMAlloc is failing to create allocations
       greater than 2GB
- pal: Update pm4 packet headers
- pal: Fix a typo that was causing an explosion of stack space.
- pal: Force fMask swizzle mode to be 4kB on GFX9 platforms in order to
       take advantage of optimized copy path.
- pal: Fix Gfx6 failure on
       VK_KHR_maintenance1_copy_image_2D_array_to_3D_transfer_R32G32B32A32_*
- pal: Remove the usage of AMDGPU_CS_MAX_IBS_PER_SUBMIT because it's
       deprecated in libdrm after version 2.4.92
- pal: Remove explict fence reset check in Queue::SubmitInternal
- pal: Add IndirectAllocator utility class
- pal: Print ClientMem pointer in the leaked list, which helps debugging
       memory leak

* Sun Jun 03 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.35-0.20180603.git3540e83

- xgl: [LLPC] Add image operation lz optimization
- xgl: [LLPC] Add an option to dump llvm module's CFG
- xgl: Add timestamp hash to VkPipielineCache ID to make it more unique
- xgl: Add more implementation for sparse texture support
- xgl: Support new dimension aware image intrinsic: sample group and
       gather group
- pal: Add recommended heap in Pal::DeviceProperties to client for each
       engine for best performance
- pal: Add Util::ArrayLen, a constexpr function to get the length of an
       array at compile time. This is meant to be used in place of
       "sizeof(foo)/ sizeof(foo[0])"
- pal: Remove asserts that fire on images that aren't render targets
- pal: WriteEventCmd should translate HwPipePostIndexFetch to WRITE_DATA
       on ME engine
- pal: Add implmentations for ComputeResults for StreamoutStats queries

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
