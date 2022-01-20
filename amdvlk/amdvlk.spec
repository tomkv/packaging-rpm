%global amdvlk_commit               9f829604d89370cdc7377cef981ec56552cc9f35
# commits from AMDVLK/default.xml
%global llvm_commit                 665a520d8f74057333d70cf7261ce46ec4afef44
%global llpc_commit                 4f9ca6cdeb6b64f0f30b24a9060367234c2dcf44
%global xgl_commit                  d01032b9f8f7f3b7ce54a3078e9aae149386b716
%global pal_commit                  0a0a4ae4ab062d31fcd68863c35952967a8060ee
%global spvgen_commit               6c2f36bcf0f8ff7ba8d20c8b789ca6346d1e16b1
%global metrohash_commit            3c566dd9cda44ca7fd97659e0b53ac953f9037d2
%global cwpack_commit               39f8940199e60c44d4211cf8165dfd12876316fa
# commits from spvgen/CHANGES
%global glslang_commit              b9ba4c5743997abbc0df858f2458a86d62af6a25
%global spirv_tools_commit          4578db3c419a9300485155fd8b81f6b1d822b5fb
%global spirv_headers_commit        19e8350415ed9516c8afffa19ae2c58559495a67
%global spirv_cross_commit          e4243b898ca5e1e19e48725a991ada1e5744691c

%global amdvlk_short_commit         %(c=%{amdvlk_commit}; echo ${c:0:7})
%global llvm_short_commit           %(c=%{llvm_commit}; echo ${c:0:7})
%global llpc_short_commit           %(c=%{llpc_commit}; echo ${c:0:7})
%global xgl_short_commit            %(c=%{xgl_commit}; echo ${c:0:7})
%global pal_short_commit            %(c=%{pal_commit}; echo ${c:0:7})
%global spvgen_short_commit         %(c=%{spvgen_commit}; echo ${c:0:7})
%global metrohash_short_commit      %(c=%{metrohash_commit}; echo ${c:0:7})
%global cwpack_short_commit         %(c=%{cwpack_commit}; echo ${c:0:7})
%global glslang_short_commit        %(c=%{glslang_commit}; echo ${c:0:7})
%global spirv_tools_short_commit    %(c=%{spirv_tools_commit}; echo ${c:0:7})
%global spirv_headers_short_commit  %(c=%{spirv_headers_commit}; echo ${c:0:7})
%global spirv_cross_short_commit    %(c=%{spirv_cross_commit}; echo ${c:0:7})
%global khronos_url                 https://github.com/KhronosGroup/

Name:          amdvlk-vulkan-driver
Epoch:         1
Version:       2022.Q1.1
Release:       1%{?dist}
Summary:       AMD Open Source Driver For Vulkan
License:       MIT
Url:           https://github.com/GPUOpen-Drivers
Source0:       %url/AMDVLK/archive/%{amdvlk_commit}.tar.gz#/AMDVLK-%{amdvlk_short_commit}.tar.gz
Source1:       %url/llvm-project/archive/%{llvm_commit}.tar.gz#/llvm-project-%{llvm_short_commit}.tar.gz
Source2:       %url/llpc/archive/%{llpc_commit}.tar.gz#/llpc-%{llpc_short_commit}.tar.gz
Source3:       %url/xgl/archive/%{xgl_commit}.tar.gz#/xgl-%{xgl_short_commit}.tar.gz
Source4:       %url/pal/archive/%{pal_commit}.tar.gz#/pal-%{pal_short_commit}.tar.gz
Source5:       %url/spvgen/archive/%{spvgen_commit}.tar.gz#/spvgen-%{spvgen_short_commit}.tar.gz
Source6:       %url/MetroHash/archive/%{metrohash_commit}.tar.gz#/MetroHash-%{metrohash_short_commit}.tar.gz
Source7:       %url/CWPack/archive/%{cwpack_commit}.tar.gz#/CWPack-%{cwpack_short_commit}.tar.gz
Source8:       %khronos_url/glslang/archive/%{glslang_commit}.tar.gz#/glslang-%{glslang_short_commit}.tar.gz
Source9:       %khronos_url/SPIRV-Tools/archive/%{spirv_tools_commit}.tar.gz#/SPIRV-Tools-%{spirv_tools_short_commit}.tar.gz
Source10:      %khronos_url/SPIRV-Headers/archive/%{spirv_headers_commit}.tar.gz#/SPIRV-Headers-%{spirv_headers_short_commit}.tar.gz
Source11:      %khronos_url/SPIRV-Cross/archive/%{spirv_cross_commit}.tar.gz#/SPIRV-Cross-%{spirv_cross_short_commit}.tar.gz

Requires:      vulkan
Requires:      vulkan-filesystem

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.13.4
BuildRequires: make
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
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: ninja-build

%description
The AMD Open Source Driver for Vulkan® is an open-source Vulkan driver
for Radeon™ graphics adapters on Linux®. It is designed to support the
following AMD GPUs:

    Radeon™ RX 6900/6800/6700/6600/6500 Series
    Radeon™ RX 5700/5600/5500 Series
    Radeon™ RX Vega Series
    Radeon™ RX 400/500 Series
    Radeon™ Pro WX 9100, x200 Series
    Radeon™ Pro W5700/W5500 Series

%prep
%setup -q -c -n %{name}-%{version} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11
ln -s AMDVLK-%{amdvlk_commit} AMDVLK
ln -s llvm-project-%{llvm_commit} llvm-project
ln -s llpc-%{llpc_commit} llpc
ln -s xgl-%{xgl_commit} xgl
ln -s pal-%{pal_commit} pal
ln -s spvgen-%{spvgen_commit} spvgen
mkdir third_party
ln -s ../MetroHash-%{metrohash_commit} third_party/metrohash
ln -s ../CWPack-%{cwpack_commit} third_party/cwpack
ln -s ../../glslang-%{glslang_commit} spvgen/external/glslang
ln -s ../../SPIRV-Tools-%{spirv_tools_commit} spvgen/external/SPIRV-tools
ln -s ../../SPIRV-Headers-%{spirv_headers_commit} spvgen/external/SPIRV-tools/external/SPIRV-Headers
ln -s ../../SPIRV-Cross-%{spirv_cross_commit} spvgen/external/SPIRV-cross

%build
mkdir -p xgl/build && pushd xgl/build

cmake .. -DCMAKE_AR=`which gcc-ar` \
    -DCMAKE_NM=`which gcc-nm` \
    -DCMAKE_RANLIB=`which gcc-ranlib` \
    -DCMAKE_C_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_CXX_FLAGS_RELEASE=-DNDEBUG \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_WAYLAND_SUPPORT=ON \
    -DLLVM_ENABLE_WARNINGS=OFF \
    -G Ninja

ninja && ninja spvgen
popd

%clean
rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_datadir}/vulkan/icd.d
mkdir -p %{buildroot}%{_datadir}/vulkan/implicit_layer.d
mkdir -p %{buildroot}%{_libdir}

mkdir -p %{buildroot}%{_sysconfdir}/amd
echo "MaxNumCmdStreamsPerSubmit,4" > %{buildroot}%{_sysconfdir}/amd/amdPalSettings.cfg

%if 0%{?__isa_bits} == 64
    install -m 644 xgl/build/icd/amd_icd64.json %{buildroot}%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
    install -m 755 xgl/build/icd/amdvlk64.so %{buildroot}%{_libdir}
%else
    install -m 644 xgl/build/icd/amd_icd32.json %{buildroot}%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
    install -m 755 xgl/build/icd/amdvlk32.so %{buildroot}%{_libdir}
%endif
install -m 755 xgl/build/spvgen/spvgen.so %{buildroot}%{_libdir}

%files
%doc AMDVLK/LICENSE.txt AMDVLK/README.md AMDVLK/topLevelArch.png
%dir %{_sysconfdir}/amd
%config %{_sysconfdir}/amd/amdPalSettings.cfg
%{_datadir}/vulkan/icd.d/amd_icd.%{_arch}.json
%{_libdir}/amdvlk*.so
%{_libdir}/spvgen.so

%changelog
* Thu Jan 20 2022 Tomas Kovar <tkov_fedoraproject.org> - 2022.Q1.1

- xgl: Add Navi24 support
- xgl: Move pointSizeUsed to PipelineMetadata
- xgl: Enhance ASTC software Gpu decode pass: add cache for pipeline
       binaries, improve CPU performance,fix memory leak
- xgl: Update PAL Version in XGL to 696
- xgl: Change order of exception handling, and add attachment count guard
- xgl: Sampler compareFunc with disabled data comparison
- xgl: PAL Version in XGL Clean Up
- xgl: Cleanup VK_IGNORE macros
- xgl: Extract command buffer ring to new class
- xgl: Add change to enable overriding the VRAM size with a value higher
       than actually present on the GPU
- xgl: Add 3rd heap choice
- xgl: Avoid redundant get PAL device props call
- pal: Add Navi24 support
- pal: Use atomic increment on swizzle index
- pal: Replace static const char* with constexpr const char*
- pal: Remove OSS1 and OSS2 functionality
- pal: Let Util::Vector handle moved values
- pal: Add a nullptr check for the pipeline
- pal: Silent a wait point assertion
- pal: Add usage hints to linux archivefile impl and remove datasync
- pal: For chips that are sufficiently small, disable NGG Late Alloc
- pal: Add missing macros in conversion function of AsicInfoTraceSource

* Mon Dec 27 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q4.3

- xgl: TilingOptMode::OptForSpace cannot be used with block compressed
       format
- xgl: VkFormatProperties.bufferFeatures should be zero for depth/stencil
       formats
- xgl: Initialize enabled features for device
- xgl: bufferFeatures for Depth/Stencil formats
- xgl: Update PAL Version in XGL 692
- xgl: dEQP-VK.dynamic_rendering.*cmdbuffer* - failing on Linux
- xgl: VK_EXT_global_priority_query - Expose the extension
- xgl: Improve check for privateData
- xgl: Update Khronos Vulkan Headers to 1.2.201
- xgl: Update XGL driver reported CTS Compliance version
- xgl: Minor rework of physical device properties
- xgl: Check compareFunc before set the truncateCoords flag
- xgl: Support SPIR-V 1.5 upgrade to SPIR-V 1.6
- xgl: Add a conversion from vkgc to vk shader stage
- xgl: Fixed memory leak of DeferredHostOperation
- xgl: Fix another leak of fence memory
- xgl: Avoid shader module caching by default
- xgl: Update hash func for VRS render state cache objects
- xgl: Set disableSingleMipAnisoOverride=1
- xgl: [LLPC] Enable xnack code gen only if it is enabled in the driver
- xgl: Convert DbgBarrierCmd to 64bit
- pal: Add ReadSetting cross-platform wrapper
- pal: Correct RereadSetting name
- pal: dEQP-VK.dynamic_rendering.*cmdbuffer* - failing on Linux
- pal: Incorrect CPU logical cores shown in the RGP Device Configuration
- pal: WriteBufferImmediate  CP copydata top: ME->PFP and Cleanup
- pal: Implementation of device info trace source
- pal: Add option to open shared memory with globalGpuVa
- pal: [Streaming SDK 1.5] Pass frame index from the app to KMD
- pal: Debug logging support in PAL
- pal: Fixup Linux ArchiveFile implementation
- pal: Adjust default tessFactorBufferSizePerSe
- pal: Tweak Shader Cache Hash Map settings to reduce memory usage
- pal: StringView class implementation
- pal:  Hook up memory budget value in PAL to SW addrlib
- pal: Add ICmdBuffer::CmdCopyMemoryByGpuVa
- pal: Fix settings script
- pal: PAL_NOT_IMPLEMENTED Assert triggers with MGPU
- pal: Fix for SPM regr
- pal: Remove pointless cache layer alerts
- pal: Null device dummy values for swizzling
- pal: Add utility function to read a file into memory
- pal: Use old SPM layout until RGP is ready
- pal: Ubuntu21.04+Wayland Vulkan perf ~40% lower compared U20.04
- pal: Add sample info to ShaderEarlyCompileInfo
- pal: Fix InitBusAddressableGpuMemory decorator
- pal: Updated waForce1kHtileMin size in Gfx9
- pal: RDF lib update
- pal: Clean up NullDevice tables

* Fri Dec 10 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q4.2

- xgl: Fixed memory leak in ImportWin32Fence by moving = nullptr.
- xgl: Add ColorTargetInfo and DepthTargetInfo to ShaderEarlyCompileInfo
- xgl: Stop allocating framebuffer memory for immutable descriptors
- xgl: Fix segfault in resource opt
- xgl: dEQP-GLES2.functional.clipping.point.wide_point_clip fail on angle
- xgl: Implement fast-link mode
- xgl: Enable extension VK_EXT_index_type_uint8
- xgl: Fix assert in PalToVkSwapChainFormat
- xgl: Implementation of indirect pipelinel layout scheme
- xgl: Update Khronos Vulkan Headers to 1.2.197
- xgl: VkGraphicsPipelineCreateInfo::flags should not inherit from
       library
- xgl: Move some of multisampling states to FOI
- xgl: VK_KHR_format_feature_flags2 - Expose the extension
- xgl: Reduce size of extensions class
- xgl: Early_fragment_test: Add depth and stencil state for pipelineInfo
- xgl: Update PAL Version in XGL 687
- xgl: VK_EXT_border_color_swizzle - Expose the extension
- xgl: VK_KHR_dynamic_rendering Expose Extension
- xgl: Refactor code about pipeline layout for the new scheme
- xgl: VK_EXT_primitive_topology_list_restart - Expose the extension
- xgl: Expose VK_EXT_pageable_device_local_memory
- xgl: VK_KHR_format_feature_flags2 - Expose the extension
- xgl: Fix include issue about vk_pipeline.h
- xgl: VK_EXT_ycbcr_image_arrays - Expose the extension
- xgl: Separate shader early compilation from BuildShaderModule()
- xgl: Change opensource package libssl dependency to soft dependency
- xgl: Build resouce mapping if PRS or FGS is available
- xgl: Sets sample pattern before DS clears/resolves
- xgl: World War Z: Aftermath - Tuning Opts
- xgl: Segmentfault when build with VKI_DYNAMIC_RENDERING=ON using
       gcc>=6.1
- xgl: Disable NGG culling for Rainbow Six Siege perf
- pal: Trace data and RDF file fix
- pal: Adds a Public Setting to control whether the ACE is used for
       Indirect Cmd Generation
- pal: Remove gl2uncached from GpaSession
- pal: Update pal_lz4 to LZ4 version 1.9.3
- pal: Cleanup pal subprojects
- pal: Fix invalid memory access issue
- pal: Fix access violation issue in Hashmap DPWARN
- pal: PalVersionHelper cleanup
- pal: Added include guards for all PAL Trace related code
- pal: Fix settings generation
- pal: Update Hash Map tuning params
- pal: Initializes a trace session within PAL
- pal: 12 bit MM format support
- pal: Bring LZ4 back into PAL source
- pal: Use delete in PAL_DISALLOW_COPY_AND_ASSIGN /
       PAL_DISALLOW_DEFAULT_CTOR
- pal: modify settings in running state
- pal: Add Gs/Ngg guard
- pal: RDF lib latest update
- pal: Output HexValue in JsonWriter as string
- pal: Handle zero metadata on cross GPU BOs
- pal: Add helper to detect debugger
- pal: Add "HexValue" to JsonWriter
- pal: For non-BC views, set pitch=0
- pal: Signal error from gen script exit status
- pal: Add missing override in SetHdrMetaData
- pal: Replaced pure virtual method with virtual method
- pal: sqtt_file_format.h file updates
- pal: Missed setting cmake flag in PAL
- pal: Add logging for CmdBindStreamOutTargets
- pal: Initial implementation for trace data I/O
- pal: AUTO_FLUSH_MODE Workaround Implemented
- pal: Make sure all pairs of
       AddCommandStreamReference/RemoveCommandStreamReference are called
       under the same conditions.
- pal: Remove ComputePipeline::pipeBinary() which is not used
- pal: Fix "unknown option '/std:c++11'"
- pal: Fix an assert on Navi
- pal: [CMake] Fix 2 CMake Issues
- pal: PAL restricts YUV planar image views to 1 layer which is against
       the spec

* Fri Nov 05 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q4.1

- xgl: Runtime Setting `PipelineCachingEnvironmentVariable' Incorrect
       Behavior
- xgl: Add app profile for angle
- xgl: Handle all flag combinations in VkToPalWaitPipePoint()
- xgl: Update PAL Version in XGL 685
- xgl: Remove CreatePartialPipelineBinary()
- xgl: Implement Dispatch Tunneling
- xgl: Add optional preferred present mode for XWayland
- xgl: Fix compiler warnings
- xgl: limit the maximun memory size of pipeline cache in 32-bit system
- xgl: Update Khronos Vulkan Headers to 1.2.195
- xgl: Fix memory size requirements
- xgl: Assert if the gpu address is not found
- xgl: Support VK_EXT_ycbcr_image_arrays extension implementation.
- pal: Fix pal language support issues
- pal: Missed overriding this default for Gfx9+
- pal: Fix c++14 constexpr warnings
- pal: Add RGP detailed thread trace support for compute
- pal: Clean up gfx9 image GetAddrHi/Lo helper functions
- pal: Remove redundant parse of metadata that is unused afterwards
- pal: Fix a typo in GfxCmdBuffer::LeakPerPipelineStateChanges
- pal: DCC Present Pal Setting
- pal: Replace indirect multi draws in execute indirects IB2 with
       indirect draws
- pal: Resource correlation
- pal: Remove PAL_DBG_COMMAND_COMMENTS
- pal: PAL: Need to program the high address bits for CB and DB
       interaction
- pal: Fix resolvePipelineStatsQuery
- pal: Don’t allow to remove the layer system at build time
- pal: Add StringBag and msgpack things
- pal: Minor code cleanup, pal events
- pal: Fix minor logging issue
- pal: Do not call BitMaskScan intrinsics if the mask is zero
- pal: Fix taking reference of local variable
- pal: Move SPI_SHADER_IDX_FORMAT
- pal: Better return values for all file ops
- pal: Fix deadlock in MemoryCacheLayer: double locking in LRU
       functionality
- pal: Add support for the HSA ABI in PAL's native compute pipeline paths
- pal: Optimize DbCountControl reg logic
- pal: Disable D swizzle mode for RBPlus + BC + Gfx10 (Rearrange)
- pal: Fix mapping of ENOSPC to Result
- pal: Add supportFloatAtomics flag
- pal: RELEASE_MEM EOS event should avoid issuing GCR_CNTL
- pal: Fix some msaa rpm shader problem
- pal: Fix missing pixel copy on pre-gfx9 asics
- pal: Remove 'WaveRdy' token from "SqttTokenConfigNoInst"
- pal: TDR observed with SPECviewperf2020 Energy on 4k display with ReBAR
       enabled
- pal: Allow Util::File to work with 64-bit file sizes
- pal: Don't use graphics copy if not supported.
- pal: Add optional preferred present mode for XWayland
- pal: Implement the new version of the gfx10 "SQ counters cannot be
       stopped" workaround
- pal: Logger init fails should not fail all init

* Thu Sep 30 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.7

- xgl: Misc cleanup changes
- xgl: Set shader*Float64Atomic in GetFeatures2()
- xgl: Support defer compile optimized pipeline for early compile
- xgl: VK_EXT_pageable_device_local_memory - implementation
- xgl: Update PAL version in Vulkan to 678
- xgl: Removed unnecessary checks.
- xgl: Set Quad Sample Pattern State Bug Fixes
- xgl: Enable extension: VK_KHR_shader_integer_dot_product
- xgl: [AMDVLK-203][DXVK-1.8]Skyrim Special Edition: Rendering issues
       with menu spell effects
- xgl: Enable extension:
       VK_EXT_shader_atomic_float/VK_EXT_shader_atomic_float2
- xgl: Update Khronos Headers to 1.2.191
- xgl: Support cache convert shader module
- xgl: Workaround for Quake II RTX performance until bug is fixed
- xgl: Support uber-fetch shader in Vulkan driver
- xgl: Enable flat scratch for navi21
- xgl: Fix SwapChain::Create
- xgl: Update PAL version in Vulkan to 677
- xgl: Align subpasses in RenderPassCreateInfo
- xgl: Disable module cache for x86 build
- pal: CMake cleanup
- pal: Move PA_STATE_STEREO_X reg from UCmdBuf to UQueueCtx
- pal: Fix corruption issue when turning on DebugOverlayEnable
- pal: Some cmdbuffer/dispatch cleanup
- pal: [cmake] Replace pal_build_parameter
- pal: Debug BitfieldIsSet assertion in ScaledCopyImageGraphics
- pal: [genSetting] Add more complex BuildType support for setting
- pal: SPI_PERF_RA_* counters report 0 on all GFX9 hardware
- pal: Create new PalAbi namespace for future handling of multiple ABI's
- pal: Replace constexpr with inline
- pal: RPCS3 Corruption is observed on game window
- pal: GPU Profiler: per-draw SPM traces can clobber each other
- pal: Prevent PM4Optimizer from splitting
- pal: Remove PAL_INLINE
- pal: Remove DB_PRELOAD_CONTROL
- pal: Fix untracked cmdAllocator destroying before cmdBuffer is deleted
- pal: [CMDLOGGER] Remove shaderWrite flag from Presentable surface
- pal: [GFX10] The "array_pitch" field of the SRD determines
- pal: [AMDVLK][#236] Confusing implementation of VK_EXT_hdr_metadata

* Thu Sep 09 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.6

- xgl: Update PAL Interface in Vulkan to 675
- xgl: Cleanup use of VK_INLINE
- xgl: Fix wrong use of pDepthStencilResolveAttachment in
       SubpassDescription::Init
- xgl: Don't put cmdbufs in local when memory oversubscription is allowed
- xgl: [XGL issue#126] Switchable graphics layer filters out cards AMDVLK
       dropped support for
- xgl: Cleanup unused argument pCmdAllocator to
       CmdBuffer::PalCmdBufferReset()
- xgl: VK_EXT_load_store_op_none - Expose the extension
- xgl: VK_KHR_zero_initialize_workgroup_memory - Expose the extension
- xgl: Add exclusion for implicit external synchronization if there is no
       layout transition.
- xgl: Heavy flickering observed while performing ALT-TAB in Ghost Recon:
       Breakpoint Vulkan
- xgl: Disable enableBackfaceCulling for conservative rasterization
       overestimation
- xgl: Buffer creation enhancements
- xgl: Update Khronos Headers to 1.2.188
- xgl: Overrides of mallNoAllocCtPolicy and mallNoAllocCtSsrPolicy should
       use enums
- xgl: PalCmdResolveImage for device groups
- xgl: Valhiem shader optimization
- xgl: Revert a change causing hang of dEQP-VK.memory.allocation.*
- pal: CMake cleanup
- pal: Move PA_STATE_STEREO_X reg from UCmdBuf to UQueueCtx
- pal: Fix corruption issue when turning on DebugOverlayEnable
- pal: Some cmdbuffer/dispatch cleanup
- pal: [cmake] Replace pal_build_parameter
- pal: Debug BitfieldIsSet assertion in ScaledCopyImageGraphics
- pal: [genSetting] Add more complex BuildType support for setting
- pal: SPI_PERF_RA_* counters report 0 on all GFX9 hardware
- pal: Create new PalAbi namespace for future handling of multiple ABI's
- pal: Replace constexpr with inline
- pal: RPCS3 Corruption is observed on game window
- pal: GPU Profiler: per-draw SPM traces can clobber each other
- pal: Prevent PM4Optimizer from splitting
- pal: Remove PAL_INLINE
- pal: Remove DB_PRELOAD_CONTROL
- pal: Fix untracked cmdAllocator destroying before cmdBuffer is deleted
- pal: [CMDLOGGER] Remove shaderWrite flag from Presentable surface
- pal: [GFX10] The "array_pitch" field of the SRD determines
- pal: [AMDVLK][#236] Confusing implementation of VK_EXT_hdr_metadata

* Fri Aug 27 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.5

- xlg: Add Navi23 support
- xlg: Support uber-fetch shader in Vulkan driver
- xlg: Make DeviceGroupMemory a POD struct
- pal: Add settings to override bin size calculation
- pal: Fix CmdGenUsingAce when MS HWS is enabled
- pal: [AcqRelBarrier] InitMaskRam needs l2 flush and invalidation for
       meta cache misalignment WA

* Wed Aug 11 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.4

- xgl: Fix horrifically broken switchable graphics layer

* Fri Aug 06 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.3

- xgl: Cache the number of PAL devices (m_pDevice->NumPalDevices()) in
       the command buffer
- xgl: Change DeviceFeatures to be a bitfield instead of using VkBool32
- xgl: Rename DirtyState to DirtyGraphicsState
- xgl: Add ASTC Gpu decode pass
- xgl: Reduce Driver Binary Size - Device::Create
- xgl: [Rage2] Disable DCC for an individual resource instead of all
       color attachments
- xgl: Update Khronos Headers to 1.2.185
- xgl: Limit maxExtent.depth for 2D_ARRAY_COMPATIBLE
- xgl: Update Reporting of Limits maxImageDimension3D and
       maxFramebufferLayers
- xgl: Turn off the ImplicitExternalSynchronization for affected apps.
- xgl: Update PAL Interface in Vulkan to 674
- xgl: [pipeline_cache] driver uses wrong pipeline cache between
       enable/disable fp16
- xgl: Turn off the ImplicitExternalSynchronization for Mad Max, Doom
       Eternal, Rage 2, World War Z
- xgl: Adjust the Fragment Shading Rate Properties to spec limits.
- pal: Fix relocs for unmapped sections
- pal: Amdgpu Back-end incorrectly reporting gang-submission support is
       enabled.
- pal: [AMDVLK #228][The Surge 2] kernel driver crash if the game has
       been started with RADV before
- pal: Run CmdGen shaders using ganged ACE.
- pal: Add support for OpenSSL v1.0.x
- pal: Fix all invalid asserts
- pal: Add support for R_AMDGPU_REL16 relocation
- pal: Miss to update pBarrierOps->layoutTransitions.updateDcc
- pal: Consistent comments in config files
- pal: Add cached setting for 32b pred emu
- pal: Support 32bit predicates on the universal engine on GFX6-8.
- pal: Remove PAL_INLINE from public headers
- pal: [Vulkan] Valheim crashes when GPU profiler is enabled in
- pal: Add operator == and != for OsWindowHandle on Linux
- pal: [PAL] Add view instancing for task shaders
- pal: Support tile swizzle values per plane instead of per image
- pal: Send absolute frequencies instead of ratios
- pal: Exposing C++ standard version that PAL is compiled with
- pal: palUtil: Allow open-source standalone LLPC build on Windows
- pal: Supply full address to SRD's.

* Thu Jul 22 2021 Tomas Kovar <tkov_fedoraproject.org> - 2021.Q3.2

- xgl: Add missing checks for dynamicStateFlags
- xgl: Fix ignored structs for rasterization disabled
- xgl: VK_KHR_fragment_shading_rate: pFragmentShadingRateAttachment can
       be NULL
- xgl: VK_EXT_extended_dynamic_state2 - Expose the extension
- xgl: VK_KHR_copy_commands2 - Expose the extension
- xgl: Update PAL Interface in Vulkan to 673
- xgl: Enable implicit external synchronization for all GPUs
- pal: Fix references to compute state in dynamic launch changes
- pal: Removing PAL_INLINE from util
- pal: Fix bug of image view of X8_Unorm format
- pal: Adding dumpCmdBufPerFrame setting
- pal: Fix hole in nested CB reset logic
- pal: Fix NdGpuMemory alloc alignment bug
- pal: [AcqRelBarrier] BottomOfPipe wait stage needs to sync CPDMA
- pal: Correct SDMA Predication logic for GFX9
- pal: Put last chip hdrs in namespace

* Fri Jul 09 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.292.0.20210709.gitdc6c848

- xgl: Fix missing calls to DestroyLineStipple() and DestroyFragmentShadingRate()
- xgl: Update Khronos Vulkan Headers to 1.2.182
- xgl: Remove redundant Pal::CmdSetPerDrawVrsRate() calls if VRS state is static
- xgl: Remove dimension correction to blocks for compressed image formats
       for CmdColorSpaceConversionCopy and ScaledCopy
- xgl: Align return types of functions with API functions
- xgl: Enable interpMode patch
- xgl: vkGet*MemoryRequirements should not return device coherent memory
       types when extension is disabled
- xgl: VK_KHR_shader_subgroup_uniform_control_flow - Expose the extension
- xgl: Improve the multi-pipeline cache files init
- xgl: Change bools in GraphicsPipeline's CreateInfo to flags
- xgl: Update PAL Interface in Vulkan to 670
- xgl: VK_EXT_extended_dynamic_state2 - Driver Implementation
- xgl: [Navi10] DCC Tuning
- xgl: Add Pal::GpuHeapGartUswc to the compatible memory types available
       for host memory allocations using the
       VK_EXTERNAL_MEMORY_HANDLE_TYPE_HOST_ALLOCATION_BIT_EXT
- xgl: Change how resource keys are built
- pal: Remove core LoadIndex path support from the PipelineUploader
- pal: Fix ATC perfcounters on navi2
- pal: Add support for 2D_RECTANGLE VGT_PRIMITIVE_TYPE
- pal: Some checks for IsGfx103 would never be true as they were
       preceeded by IsGfx10 checks
- pal: Retire Pre-Polaris and Pre-Raven specific code
- pal: Fix for synchronization issue when using pinned memory
- pal: Bump version number to 319
- pal: Remove stack alignment compiler options

* Fri Jun 25 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.290.0.20210624.git9d69602

- xgl: Consolidate where the app profiles are done
- xgl: Memory leaks in the driver during full CTS run
- xgl: Clean up viewFlags argument in ImageView::BuildDepthStencilView()
       and ImageView::Create()
- xgl: Require final keyword on leaf classes
- xgl: Update PAL Interface in Vulkan to 668
- xgl: VK_EXT_extended_dynamic_state2 - Driver Implementation
- xgl: Cleanup usePalPipelineCaching use
- pal: Add CmdDispatchAce to be called from RPM
- pal: Disable LoadIndexObjectBinds by default
- pal: Fix hole GfxBltState flag wrongly cleared by
       range-checked-target-stall
- pal: Retire Pre-Polaris and Pre-Raven specific code
- pal: Tweak the FCE optimization in acquire release path and some other
       clean up
- pal: [GFX10] Remove DB_PRELOAD_CONTROL
- pal: Rename useGraphicsFastDepthStencilClear
- pal: Bump version number to 316
- pal: VK_EXT_extended_dynamic_state2 - Driver Implementation
- pal: Support monotonic raw clocks

* Fri Jun 11 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.289.0.20210610.git7387247

- xgl: Disable the settings ImplicitExternalSynchronization for Gpu's
       above Gfx8
- xgl: Fix implicit synchronization in renderpass for gpu below gfx9 for
       implicitExternalOutgoing = 1
- xgl: Update Khronos Vulkan Headers to 1.2.179
- xgl: Fix profile script randomly breaking on empty folders
- xgl: [RGP][RenderDoc] Unable to capture due to "trigger mode" getting
       wiped mid-capture
- pal: Bump version number to 314
- pal: Fix the SQ's LEVEL counters in SPM traces
- pal: Deprecate PAL_BUILD_GPUOPEN / PAL_ENABLE_DEVDRIVER_USAGE
- pal: [MGPU][wayland] Corruption Observed while running Wayland render
       tests

* Wed May 26 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.188.0.20210526.git29fd70a

- xgl: Expose VK_EXT_custom_border_color
- xgl: Expose VK_EXT_color_write_enable
- xgl: [AMDVLK] Generate driver package through CMake/CPack
- xgl: Update Khronos Vulkan Headers to 1.2.178
- xgl: Update PAL Interface in Vulkan to 667
- xgl: Add support for memory and leak sanitizer
- xgl: VK_EXT_color_write_enable - Driver Implementation
- pal: Bump version number to 312
- pal: Remove public references to ThreadTraceViewer
- pal: [cmake] Move shared, res, include functionality to the appropriate
       locations
- pal: Enable shader write compression for Depth+Stencil images on GFX10
- pal: [GpuDebug] SurfaceCapture add missing barriers
- pal: CPU Perf Simplify Binning code
- pal: [PAL]gfx9CommandGenerator using wrong packet to set index_type

* Tue May 18 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.186.0.20210517.git8acc216

- xgl: Change PipelineProfile::PipelineProfileEntry array to use dynamic
       memory
- xgl: XGL's AmdCMakeHelper.cmake has hidden dependency on pal's
       AmdCMakeHelper.cmake
- xgl: Update PAL Interface in Vulkan to 666
- xgl: XGL + VK_KHR_synchronization2 support: Invalid assertion failure
       triggers in PAL when transfering owership from compute to
       universal queue fam
- xgl: Update Khronos Vulkan Headers to 1.2.177
- xgl: Disallow Copy Constructors
- pal: Add more than one heap preference support to GpuMemory Events to
       PAL and deprecate "preferredHeap”
- pal: Initialize gang-submit semaphore
- pal: Inconsistent layout masks for ResolveSrc/ResolveDst
- pal: Changing the name of the iterate256 panel setting
- pal: Disallow iterate256 only for Vulkan and samples>=4 on Navi21
- pal: Remove Deprecated ISA Database Chunk from RGP Files in GpaSession
- pal: [Wayland] Fix warning in building WaylandWindowSystem
- pal: Fix segfaults in dev callbacks on non-x11 linux
- pal: Use source file hacks for Wayland to fix Linux builds
- pal: Adds support for the RmtVersion event so the tool can properly
       identify which RMT spec version is being used for emitted RMT
       tokens
- pal: CPU Perf Calculate Pipeline binning on/off at pipeline creation
       time
- pal: Fix performance issue in Dawn of War 3 and Civilization 6
- pal: [cmake] Improve PAL configure/generate speed with 3.12/3.13
       functionality
- pal: Support dynamic enable of color writes
- pal: Extend format support on Wayland
- pal: Fix segfaults in CmdBufferLogger
- pal: Fix ExecuteIndirect Changes
- pal: [GpuDebug] Add Depth Stencil Support to Surface Capture
- pal: Hook up CPU present path on Linux to a setting
- pal: Vulkan apps ignoring previously created shader cache and creating
       new duplicate cache
- pal: Indirect Command Generation creates long chain of NOPs
- pal: Allow use of 256B swizzle modes in PAL

* Wed Apr 28 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.184.0.20210428.gitd42d2c7

- xgl: Update PAL Interface in Vulkan to 665
- xgl: Few applications are running with llvmpipe driver by default with
       AMD switchable graphics layer
- xgl: Disallow Copy Constructors
- xgl: Driver Implementation for VK_KHR_synchronization2
- xgl: Update Khronos Vulkan Headers to 1.2.174
- xgl: [AMDVLK-187] AMDVLK give out of memory errors when no AMD GPU
       installed
- pal: Bump version number to 306
- pal: FMask's pipeBankXor bug of optimal shared image
- pal: Support dynamic enable of color writes
- pal: Added supportInt8Dot and supportInt4Dot to DeviceProperties
- pal: Move UseDcc to PAL Core settings.
- pal: [GFX9+]Reduce ES verts per subgroup with on-chip GS and
       Tessellation (NGG pipeline)
- pal: Rework logic for DCC support with multiple available formats
- pal: Add partial nested cmd buffer support to GpuDebug layer
- pal: [AMDVLK-187]AMDVLK give out of memory errors when no AMD GPU
       installed
- pal: Fix PAL_NOT_IMPLEMENTED_MSG issues.
- pal: Fix access violation when enable "CmdAllocatorFreeOnReset"
- pal: Renegerate the PAL MALL cursor setting
- pal: Build fix for acq-rel on old iface versions
- pal: [GpuDebug] Add DDS functionality to Surface Capture

* Wed Apr 07 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.181.0.20210407.gitf1b97f7

- xgl: Add Navi12 support
- xgl: Driver Implementation for VK_KHR_synchronization2
- xgl: Update PAL Interface in Vulkan to 664
- xgl: Update Khronos Vulkan Headers to 1.2.173
- xgl: Add support for no alloc to our resource optimizer
- xgl: Add new DCC settings and update the DCC defaults for Navi10+
- xgl: Update settings file to add top level DriverState Field
- xgl: Generate the json file by template
- xgl: Fix memory leak on create device queues failure
- xgl: Cleanup unnecessary code in CmdBuffer::BindPipeline()
- xgl: Fix potential issues in AMD switchable graphics layer
- xgl: Remove settings for dispatch tunneling
- pal: Add Navi12 support
- pal: [GpuDebug] Avoid GpuDebug making a token-style CmdBuffer for
       nested command buffers
- pal: Fix DmaCmdBuffer::GetMemImageCopyMethod for Gfx10
- pal: If there is no AMD GPU in the system, then return Initialization
       Failed error
- pal: PWS on legacy barrier to expose more wait stages
- pal: Fix Reported MaxEventId for EA block on Gfx10
- pal: Fix software stream-out event packet write asserts
- pal: Indirect Command Generation creates long chain of NOPs
- pal: [cmake] Improve Pal configure speed
- pal: PAL writes two copies of the compute user-data registers
- pal: Adding cmd Submit into WriteUniversalPreamble() to prevent
       exceededing the cmd "reserve_limit"
- pal: Panel setting for inlining nested command buffers. Useful for
       logging the buffers at submit time.
- pal: Fix usage of ::std::random_device()
- pal: Add a public settings disableDebugOverlayVisualConfirm to disable
       debug overlay after Platform initialization
- pal: Add back the deprecated event-based AcqRel interface functions
- pal: Fix memory leaks on create failures with layers enabled
- pal: Add option to add DrawDispatchInfo for only true app-draws
- pal: Add the interface and support in PAL to prime cache
- pal: Avoid flushing gfx-only caches on async compute
- pal: AQL path update
- pal: Rename GenericAllocatorAuto to GenericAllocatorTracked and only
       define it if PAL_MEMTRACK=1 otherwise alias it to GenericAllocator
- pal: Fix the reported VGPR allocation granularity

* Fri Mar 19 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.179.0.20210319.gitf404771

- xgl, pal: Add Navi22 support

* Fri Mar 12 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.179.0.20210312.git56170eb

- xgl: Add missing VK_PIPELINE_STAGE_2 flags
- xgl: Update PAL Interface in Vulkan to 659
- xgl: Expose the device extension VK_KHR_sampler_ycbcr_conversion
- xgl: Fix WaitEventsSync2ToSync1
- xgl: [cmake] cmake clang llvm-ar named llvm-ar-6.0 on 18.04 ubuntu
- xgl: VK_KHR_synchronization2 fix the
       CmdBuffer::PipelineBarrierSync2ToSync1
- xgl: Reduce work in CmdBuffer::Reset() if cmd buffer was never begun
- xgl: Expose the extension VK_KHR_synchronization2
- xgl: Expose the extension VK_EXT_4444_formats
- xgl: Use -fPIC compile parameter for cmake builds
- xgl: Fix issues with pipeline cache uuid
- xgl: Update Khronos Vulkan Headers to 1.2.170
- xgl: VK_KHR_synchronization2 fix CmdBuffer::ExecuteAcquireRelease
- xgl: In RPBeginSubpass(), only create the VirtualStackFrame if we are
       going to use it
- xgl: Fix CmdBindBorderColorPalette in PalCmdBufferBegin
- xgl: BindDescriptorSets changed to operate on device mask
- xgl: Fix wrong pointer alignment in PatchedDynamicDataFromHandle()
- xgl: Disallow Copy Constructors
- xgl: Store settings we need to CmdBuffer functions in the CmdBuffer
       object to avoid following the pointer to the device
- xgl: Add shader activity logging for 'disableLoopUnrolls' and
       'wavePrioOnStartup'
- pal: Dota2 : ~20% perf drop with Re-Size bar enable
- pal: Use upstream vmid support
- pal: Bump version number to 300
- pal: Code refactoring of mmpipelines up to possible extent.
- pal: Update interface logger and add a bunch of static asserts
- pal: Remove pal code object elf header validation from "init from
       binary" functions
- pal: [NAVI21][PAL] Updating DMA command to use subresource for the
       corresponding plane when programming
- pal: Rename function to avoid shadowing
- pal: Remove some cruft from Barrier and RsrcProcMgr
- pal: [GpuDebug] Add Surface Capture functionality
- pal: Add UUID support to PAL
- pal: Csc changes and HDR shaders modification by removing studio/full
       ragne conversions from the kernels
- pal: Fix interface logger assert/error
- pal: Add pal code object elf header validation to "init from binary"
       functions
- pal: Add Developer::CallbackType::SurfRegData handling to layer
       callback functions to avoid asserts

* Thu Feb 25 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.177.0.20210225.gitab996a7

- implicit layer disabled
- xgl: Reduce CPU spike in CmdBuffer::RebindPipeline()
- xgl: VkPipelineCreationFeedbackEXT.flags isn't being cleared
- xgl: Reduce work in CmdBuffer::Reset() if cmd buffer was never begun
- xgl: Update PAL Interface in Vulkan to 656
- xgl: Allow sub-allocating of shared buffers
- xgl: Also skip preinitialized layout with barrier filter option
       SkipImageLayoutUndefined
- xgl: Remove adjusting vertex index and offset for DynamicVertexStride
- xgl: Mad Max: Performance tuning
- xgl: Update Khronos Vulkan Headers to 1.2.169
- xgl: Improve the CMake code for vulkan and spirv header
- pal: Fix abi loader failing when detecting unsupported header flag for
       xnack and sramecc
- pal: Add panel setting for personal experiments
- pal: Bump version number to 298
- pal: Remove unuseful MD5 related files
- pal: Allow clearing 96-bit texels with CmdClearColorBuffer
- pal: Set default IsolineDistributionFactor to 12
- pal: Fix settings generator helper script to properly display 'help' if
       user enters unsupported arguments
- pal: Cover additional edge-case for image to image copies of BCn MIP
       levels which require supplementary per-texel copy
- pal: Set 32b predication support for GFX9 & GFX10.1
- pal: Fix VGPR/SGPR reporting for functions in a library. Need to
       extract statistics from shader metadata instead of registers
       (which does not store absolute values)
- pal: Add a trackable PAL forwardAllocator

* Mon Feb 08 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.175.0.20210208.git3e7f94e

- xgl: Update PAL Interface in Vulkan to 648
- xgl: War Thunder : Performance tuning
- xgl: Update Khronos Vulkan Headers to 1.2.168
- pal: Add assert check to make sure submitOptModeOverride matches the
       SubmitOptMode enum
- pal: Apply final keyword to the CmdBuffer::CmdAllocateEmbeddedData()
       function and the GpuEvent class
- pal: Skip Generation of Signal and Wait Semaphore Event Timing Data
       when GET_KMD_CONTEXT_INFO Escape is Unavailable
- pal: Add surface address developer callback
- pal: If command memory is in the local heap, use the uncached mtype and
       disable prefetching
- pal: Don't assume the CPUID intrinsic exists

* Fri Jan 29 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.174.0.20210129.gitcfbfe47

- xgl: Clean up Fullscreen Manager
- xgl: Vulkaninfo crash when VK_LAYER_AMD_switchable_graphics enabled
- xgl: Update PAL Interface in Vulkan to 644
- xgl: Update Khronos Vulkan Headers to 1.2.167
- xgl: Fix Run-Time Check Failure: Stack around the variable
       'pSrdMemorys' was corrupted
- xgl: Fix the GetMemoryRequirements for images
- xgl: vkAllocateDescriptorSets should return error if allocating dynamic
       descriptor set from pool that doesn't support dynamic
- xgl: Fix wrongly assert in ImageBarrierPolicy GetLayouts
- xgl: [RGP] Crash if instance fails to acquire debug VMID
- xgl: Disables queue timing when kernel context handle is unavailable
- xgl: Clean Up Unused Classes
- xgl: Minor change related to ForceDisableDcc
- xgl: Doom Eternal: Performance tuning on Navi21
- xgl: DOOM: Performance tuning on Navi21
- xgl: Wolfenstein II: Performance tuning on Navi21
- xgl: Wolfenstein-Youngblood: Performance tuning on Navi21
- pal: Apply final keyword to classes
- pal: Update Mesh/TaskShader entries per ring to 256 per SE
- pal: Bump version number to 294
- pal: Build error with Mutex Init
- pal: Add a checked version of StringToValueType
- pal: Update coding standard to require "final" keyword on leaf classes
- pal: Add DDR5 related enum and informations
- pal: The Barrier in LateExpandResolveSrcHelper doesn't have a reason
- pal: Update coding standards to allow anonymous namespaces
- pal: Shareable YUV images are non-functional
- pal: CPU Perf Remove some binning settings
- pal: Ensure three plane YUV images (YV12) have the plane data in the
       correct order
- pal: TDR when running Maxon drawport test
- pal: Make loader scripts run on python3
- pal: Remove useless code found in debugging
- pal: Expose maximum number of format planes
- pal: Add setting of RLC_SPM_ACCUM_MODE to PerfExperiment
- pal: The previous AssociateNativeFence() implementation is not that
       correct
- pal: Update copyright dates for 2021
- pal: Enable Depth+Stencil compute-based decompress BLT
- pal: Add support in PAL for YUV P210 format and MM formats for DCC for
       YUV
- pal: Access violation if BestFitAllocator was initialized failed
- pal: Fix typo in palLib.h
- pal: Adding comments describing shadow state register ranges to improve
       code readability

* Fri Jan 08 2021 Tomas Kovar <tkov_fedoraproject.org> - 2.172.0.20210106.git0b8a719

- xgl: Update due to argument IImage* retired from SignalNativeFence()
- xgl: Remove Mutex::Init(), RWLock::Init(), and
       ConditionVariable::Init() usage
- xgl: [Navi21] X-Plane: LLPC performance tuning
- xgl: Add scope to some settings
- xgl: Add AMD switchable graphics layer to switch AMD Vulkan driver
       between amdvlk and RADV
- xgl: [Navi21] Madmax LLPC performance tuning
- xgl: Fix memory alignment for memory dedicated allocation
- xgl: [Navi21] Talos Principle: LLPC performance tuning
- xgl: Update PAL Interface in Vulkan to 640
- xgl: Update Khronos Vulkan Headers to 1.2.164
- xgl: Remove DebugReportCallback::Message() and
       DebugUtilsMessenger::Message() since they are unused
- xgl: PhysicalDevice::m_memoryUsageTracker::trackerMutex corrputed
- xgl: [Navi21] Rise of Tomb Raider-LLPC performance tuning
- xgl: Move spirv-headers from XGL to LLPC
- xgl: flags cleanup - meaningless const on return types
- xgl: Enable NGG compactionless for GFX10.3+
- xgl: [Navi21] F12017 LLPC performance tuning
- pal: Add Mesh shader support
- pal: ImageAspect Removal (clean up IsFullSubresRange asserts)
- pal: Bump version number to 288
- pal: Reorder start of CMakeLists.txt in pal root so that
       TEST_BIG_ENDIAN works for stand alone builds
- pal: Add declarative heap selection in GpuMemoryCreateInfo
- pal: Fix warning (found in cmake build) that bltSyncToken is defined
       twice
- pal: [Navi21] Meta equation of multiple layer image is incorrect.
- pal: Add new interface function to query command feedback status from
       PAL Security Processor
- pal: Remove Util::ConditionVariable::Init()
- pal: Remove RWLock::Init() from PAL
- pal: Ensure there is a fallback to local visible memory when requesting
       invisible memory for RGP traces
- pal: Move initialization of Util::ConditionVariable to constructor
- pal: Initialize Util::RWLock in constructor
- pal: Fix several issues in error handling
- pal: Fence style barrier signaling and waiting, part1
- pal: Remove Mutex::Init()
- pal: File::Rseek & File::FastForward Added
- pal: [Navi21] Meta equation of 4/8xMsaa image is incorrect
- pal: Update UserDataMapping enum
- pal: Add Tonga back to null device tables
- pal: Fix DRI3, Wayland and DRM traces
- pal: Remove several dead settings
- pal: Allow Util::Vector to qualify as a `range_expression` concept
- pal: Generate different RPM shaders on diff milestones of a chip
- pal: YV12 format update
- pal: Inconsistent layout masks for ResolveSrc/ResolveDst
- pal: Initialize Mutex in the constructor
- pal: [GFX9/10] Remove RMW for DB_RENDER_OVERRIDE in most cases
- pal: Remove ImageAspect from PAL interface (replaced with plane index),
       and add numPlanes to SubresRange
- pal: Fix invalid SET_PREDICATION asserts
- pal: [cmake] Created PalBuildParameters.cmake
- pal: Add a nodiscard helper
- pal: Minor mistake on handling exception in palElfProcessorImpl.h
- pal: Missing DrawDispatchInfo in CmdBufferLogger output
- pal: [Navi10] RPCS3  Corruption observed on Game window

* Tue Dec 15 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.170.0.20201214.git3940b58

- xgl: Update Khronos Vulkan Headers to 1.2.162
- xgl: Miss to update memory metadata for dedicated image
- xgl: Update PAL Interface in Vulkan to 638
- xgl: [NAVI21]Shadow of the Tomb Raider-LLPC performance tuning for
       Navi21
- xgl: Remove Image Format in VkToPalImageUsageFlags Conversion
- xgl: Change DisableDisplayDccForMgpu from a bool to an enum
       DisableDisplayDcc
- xgl: Expose extension VK_EXT_shader_terminate_invocation
- xgl: Propagating up the error to the caller
- xgl: Move the PerGpuRenderState out of the CmdBuffer object and
       allocate memory for it after the CmdBuffer object. Reduces the
       memory for the xgl and pal command buffers
- xgl: Use a more canonical way to merge low/high address
- xgl: Change deviceUUID calculation method
- xgl: Fix error format enum
- xgl: Add build option to use external upstream spirv and Vulkan header
       files
- xgl: Update MALL no alloc tuning for Red Dead Redemption 2
- xgl: Expose extension VK_KHR_fragment_shading_rate
- pal: Fix unhandled exception and avoid assertion if  dummy chunk
       repeatedly assigned
- pal: TDR when running Maxon drawport test
- pal: [GFX6] Wrong tile mode translated from amdgpu-tileMode to
       pal-tileMode
- pal: Fix crash when barrier targets contains nullptr
- pal: [cmake] add pal_build_parameter
- pal: Add detailed instruction tokens through configuring
       threadTraceConfig instead of configuring
       threadThreadShaderTypeMask.
- pal: The HW requirement for the linear pitch during internal buffer to
       image copy and vice-versa was not being honored for certain cases.
- pal: Change name of IsDepthStencil because its misleading
- pal: Do not issue StencilRef RMW if no state to update.
- pal: Don't enable BigPage/LargePage/Iterate256 padding for local
       visible heap in ResizeBarOff case
- pal: Bump version number to 283
- pal: [GpuDebug] Add check to make sure currently bound render targets
       match the format of the bound pipeline.
- pal: Ease of Use for Settings Generation Script
- pal: Add mmSPI_SHADER_PGM_RSRC3_GS into nonshadowedList to fix assert
- pal: Remove some tabs from the source code
- pal: Another out of bound index case for "waIndexBufferZeroSize"
- pal: Gfx9::Image::ImageSupportsShaderReadsAndWrites() is incorrect
       (layout transition cleanup)
- pal: Propagating up the error to the caller correctly when
       InitSubresourceInfo failed
- pal: [cmake] Get rid of warning
- pal: Remove IDevice::GetValidFormatFeatureFlags because it is no longer
       used or relevant
- pal: Fix depthPitch calculation error when get external shared Image
       with mipLevels
- pal: Create section on memory allocation and initialization in PAL
       coding guidelines
- pal: [AMDVLK-179] Corruption in X-Plane 11.50
- pal: [GFX10+] Remove unneeded shadow regs.
- pal: Call Destroy() if Init() has failed for objects in src/core/layers
- pal: Forbid Yoda conditions.
- pal: Allow TC Compatible fast clears to slices of color array resources
- pal: [ChipMerge] Handle multiple input files of a given type per-asic

* Thu Nov 19 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.167.0.20201119.git2cd49c0

- Support Navi21

* Tue Nov 17 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.167.0.20201113.git57c3821

- xgl: Update PAL Interface in Vulkan to 632
- xgl: Update Khronos Vulkan Headers to 1.2.159
- xgl: vk::ImportSemaphoreInfo::handleType should only contain a single
       handle type
- xgl: Remove the VertBufBindingMgr class and store the vertex buffer
       binding data in the command buffer's m_state.perGpuState to keep
       the 1280 bytes needed for each gpu out of the way when running
       single GPU
- xgl: [RGP] Fix Assert When vkInstance is Destroyed under DevMode
- xgl: Shrink size of Memory object - 328 bytes to 184 bytes
- pal: Bump version number to 279
- pal: Client option for SQ Thread Trace stall behavior was not being
       honored.
- pal: NGG GS: Modify an assertion
- pal: Align some of our AmdGpuMachineType's to their actual values.
- pal: Fix ambiguous comments for acquire/release barrier path.
- pal: Minor improvement for ValidateDraw
- pal: Remove one unnecessary input parameter "setDataSize" for
       Pm4Optimizer::OptimizePm4SetReg()
- pal: Fix trivial doxygen comment issues seen by chance.
- pal: Driver does not work with two videocards: radeon+amdgpu
- pal: Add LPDDR5 support on PAL
- pal: Assert Check failure on Recording GPU Memory Reference Event
- pal: Clarify some alerts
- pal: Tropico 4 demo: Corrpution observed during Game play
- pal: [GpuDebug] Add GpuDebug layer.
- pal: Optimize PAL ValidateDraw<PipelineDirty=false, StateDirty=false>
       path

* Thu Nov 05 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.166.0.20201105.git247e0ac

- xgl: Remove redundant LLPC options
- xgl: Enable VK_EXT_robustness2 for pre GFX9
- xgl: Shrink SetUserDataLayout
- xgl: Remove dynDescDataRegCount from SetUserDataLayout
- xgl: Update Khronos Vulkan Headers to 1.2.158
- xgl: Driver development for extension: VK_KHR_SHADER_TERMINATE_INVOCATION
- pal: Based on newly understood requirements from KMD for BigPage
- pal: Avoid context roll on SwitchGraphicsPipeline for RB+ parts
- pal: Fix srcExtent.depth  in GenerateMipmapsSlow
- pal: Vulkan test failures due to iterate256
- pal: Add missing overrides
- pal: [Wayland] Vulkan apps fails in Wayland on upstream since Mesa 20.1
- pal: Optimize PAL ValidateDraw<PipelineDirty=false, StateDirty=false>
       path (part 1)
- pal: Remove some obsolete logging settings
- pal: Improve compiler detection on linux
- pal: Bump version number to 276
- pal: Fix CmdWriteImmediate for 64-bit values on DMA
- pal: Clarifiying language for inline functions in coding guidelines
- pal: [GPA][RenderDoc] Counter collection hangs RenderDoc

* Thu Oct 29 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.165.0.20201029.git4781635

- xgl: Update pNext Looping
- xgl: Shrink size of DescriptorSet
- xgl: Update Khronos Vulkan Headers to 1.2.157
- xgl: Remove the assertion for heap type
- xgl: PalAllocator should be a class not a struct
- xgl: Update SPIR-V headers
- pal: Bump version number to 275
- pal: Refactor meta equation code out of Gfx9MaskRam class into its own
       optionally allocated member class
- pal: Add missing alignment check in internal memory manager
- pal: Fix src3dSlice in ScaledCopyImageGraphics
- pal: Add Missing ShaderLibrary Stuff to InterfaceLogger
- pal: Bumps RGP max server version to 11
- pal: Rebuild generated shaders
- pal: Add steppings for gfx6.0.2, gfx7.0.5, gfx8.0.5, gfx10.1.0xFFFC
- pal: MemTracker::Free is now O(1) instead of O(N)

* Tue Oct 20 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.163.0.20201020.git7ee7a2f

- xgl: Update 3D tiling setting to apply to storage images
- xgl: CmdPool::Create() should share allocation between xgl and pal
       objects
- xgl: Add heap override settings and app detects
- xgl: Update Khronos Vulkan Headers to 1.2.156
- xgl: Remove unnecessary depth expands/resummarizes
- xgl: Use local heap for command buffers if heap is > 256 MBs
- xgl: Disable shared cmd allocator
- xgl: X-plane new update cause 50% drop in 4K low
- xgl: Cpu performance optimization
- xgl: Add support for extension: VK_EXT_shader_image_atomic_int64
- xgl: Update PAL Interface in Vulkan to 629
- pal: Allow ShaderWrite/CopyDst usages for compressed depth/stencil
       images on GFX10+
- pal: Color fast clear needs to examine usage flags to determine if
       clear-to-reg can be supported
- pal: GFX9/GFX10 Allows ShaderWrite usage for compressed MSAA color
       images
- pal: Add Util::Rename to rename a file/directory with Posix-ish
       semantics
- pal: Unspecified workaround disables htile for all d/s image < 8x8
- pal: [GFX6-10] Trivial cleanup remove some unneeded std:: refs
- pal: Util::File: Opening "-" gives you stdin or stdout
- pal: Fix palThread.h to work if palMutex.h not already included
- pal: Enable CS_PARTIAL_FLUSH events on ACE queues for gfx9+ if the CP
       ucode bug is fixed
- pal: [cmake] Delete unneccessary files
- pal: [DbgOverlay] Add Date/Time to VisualConfirm
- pal: Bump version number to 274
- pal: [cmake] pal_override helper function
- pal: Async compute work does not contribute to SPM
- pal: Allow the command buffer state inheritence feature to work from
       compute to graphics
- pal: X-plane new update cause 50% drop in 4K low
- pal: [G-Truc] Add more clamp type
- pal: Reduce CPU overhead for ValidateDraw
- pal: Surfaceflinger/swapbuffer performance issue
- pal: [cmake] Deprecate PAL_ENABLE_LTO
- pal: Connect panel settings to disable Z Compression and S Compression
- pal: Cleanup interface for pipeline residency
- pal: [cmake] Fix multiple GPU support issues
- pal: Clarify style for testing booleans
- pal: Improve CopyMemoryCs()
- pal: Build display dcc by default but disable it by default on Linux
       panel

* Tue Sep 29 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.159.0.20200927.git0d3edb1

- xgl: Junk Screen is observed during gameplay on Doom VFR Game on Navi10
- xgl: Baldur's Gate 3 stops responding after enabling Vsync
- xgl: Update PAL Interface in Vulkan to 628.2
- xgl: Flickering corruption visible in shadows in Baldur's Gate 3
- xgl: [cmake] Update cmake minimum required version to 3.13.4
- xgl: Add shader read usage for presentable images
- xgl: Enable extension VK_EXT_robustness2
- xgl: Sample Locations being overwritten by renderpass
- pal: Deprecate PAL_CLIENT_INTERFACE_MINOR_VERSION
- pal: Add Linux Flip Status to PAL Overlay
- pal: [cmake] Compile definitions PRIVATE/PUBLIC issues
- pal: [cmake] Use CMAKE_DL_LIBS/FindThreads
- pal: Make DMA updates the memory with Embedded allocated memory
- pal: Add support for compute thread group scheduling using
       numThreadGroupsPerCu.
- pal: [cmake] Reduce public dependencies
- pal: Allow TC Compatible fast clears to slices of color array resources
- pal: Bump version number to 271
- pal: Add shared bo table in Vam manager
- pal: Scan Converter polygon offset with 16 bit fixed precision
- pal: Refine amdgpu vam manager codes, preparing to add shared bo table
       in class VamMgr
- pal: CreateMultiQueue calls exit with Result::Unsupported when various
       PAL layers are enabled
- pal: Compute buffer fill for sizes > 4GB broken
- pal: Reduce RMW usage for KEEP_TOGETHER_ENABLE
- pal: Use PGO in CMake only if enabled
- pal: Green color corruption flashes and disappears on launching the
       jesse-cube demo

* Mon Sep 14 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.157.0.20200912.git7933159

- xgl: Fix the erasing elements from HashSet m_sparseBindMemory
- xgl: Corruption observed in Detroit: Become Human on RX 5600XT
- xgl: Update LLPC Interface in Vulkan to 41
- xgl: Update Khronos Vulkan Headers to v1.2.152
- xgl: Add override settings for LLPC Tuning
- xgl: Change heap order for InternalPoolGpuReadOnlyCpuVisible
- xgl: Correct setting of maxInterpolationOffset
- xgl: Replace StencilOpsCombiner with draw time validation
- xgl: Update PAL Interface in Vulkan to 624
- xgl: Clean-up LLPC interface macros that are unnecessary below version
       40
- xgl: Add spvDisassembleSpirv check in case spvgen is not loaded in the
       amdllpc
- xgl: Update pNext Looping
- xgl: Remove WaveBreak::DrawTime in LLPC interface
- xgl: Use unsigned to replace uint32_t to keep LLPC style
- pal: [cmake] Pal should set AMD_SOURCE_DIR
- pal: Fix CmdUploadRing not being detected correctly.
- pal: Add Shader Library Support to GpaSession
- pal: Set initial GfxCmdBufferState barrier tracking flags based on the
       command buffer's support flags.
- pal: Bump version number to 268
- pal: Rework Linux IsKeyPressed implementation
- pal: Move color key related shader code out of ScaledCopy CS/GFX
       pipelines
- pal: Eliminate invisible copy of trace buffer on APU platforms

* Sun Aug 30 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.155.0.20200821.git0fad196

- xgl: Process ForceAppProfileEnable before any profiles
- xgl: Enable extension: VK_EXT_image_robustness
- xgl: Development of extension: VK_EXT_4444_formats
- xgl: Fix intermittent crash of Doom Eternal on Navi10
- xgl: Update api version 1.2.150
- xgl: Disable sharing for timeline semaphores
- xgl: Strange Brigade Crashes on Launch
- xgl: Fixes for sparse unmap before destroy
- xgl: Fix a defect when determining the last vertex processing stage to
       generate stream-out resource node
- xgl: CmdBuffer::Create needs to allocate host memory with allocator
       from the command pool
- xgl: Update PAL Interface in Vulkan to 622
- xgl: Shader Tuning opts for Ghost Recon Breakpoint
- xgl: HDR display gamut chromaticity coordinates is wrong
- pal: Move GpuProfiler granularity setting from PerfCounterConfig to
       general GpuProfilerConfig
- pal: Allow TC Compatible fast clears to slices of color array resources
- pal: Delay Residency for Pipeline Memory Until Necessary
- pal: Bump version number to 266
- pal: Make CopyDepthStencilImageGraphics faster
- pal: Add counting elements for IntrusiveList
- pal: Remove CS fixed user data layout restriction
- pal: Add allocation of two command chunks for ExecuteIndirect Task+Mesh
       implementation
- pal: Add settings json files to cmake
- pal: Fix for crash in GPA tests
- pal: GPASession: Add a mask to control detailed instruction tracing on
       a per-SE basis
- pal: Add panel setting for prefer compute path for non-local copies
- pal: [GFX9/10] Remove a few unneeded members in MSAA State obj
- pal: Surfaceflinger/swapbuffer performance issue
- pal: [GFX9/10] Solidify PBB bin size programming
- pal: Make CmdScaledCopyImage faster
- pal: [Profiler] Output filename hashes and force-draw-granularity-profiling
- pal: Initialize pUserDataTable when
       "pComputeState->pipelineState.dirtyFlags.pipelineDirty" is not set
- pal: Add a setting to disable thread group level preemption for
       pipelines with inter-threadgroup dependencies
- pal: Expose function ExportKmtHandle() to client driver
- pal: [Wayland] Vulkan apps fails in Wayland on upstream since Mesa 20.1
- pal: Update compute user-data validation function to accept any
       ComputeState and UserDataTableState
- pal: Remove CE RAM user-data update path
- pal: Allow write_compress_enable in image SRD for more cases
- pal: The missing msaa state rebind at some internal graphics operation,
       include: CopyDepthStencilImageGraphics() and ResolveImageGraphics()
- pal: Support SPM chunk v1.3 in PAL
- pal: Make pipeline initialization take in an AbiReader
- pal: Change imageRsrcTypeCheck from an enable bit to a disable bit to
       default-on the workaround
- pal: Allow TC Compatible fast clears to slices of color array resources
- pal: [Profiler] Add option to allow skipping of data writes for
       non-draw/dispatch cmd-bufs
- pal: Add TMZ flag in PresentableImageCreateInfo to avoid no swapchain
       created

* Fri Aug 07 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.153.0.20200806.git24551b2

- xgl: Improve binding loop efficiency and logic in
       Queue::BindSparseEntry
- xgl: Follow up implementation for adding Write Multiplane Resource
       Descriptor Support for Combined Image Sampler
- xgl: DescriptorPool::Init needs to use passed in allocator
- xgl: Update PAL interface to 613
- xgl: Enable pipeline cache
- xgl: Enable sharing metadata of images.
- xgl: CmdBuffer::Begin() uses a non-const ref. This should be changed to
       use a pointer
- xgl: Add Write Multiplane Resource Descriptor Support for Combined
       Image Sampler
- pal: Fix for memory leak in VaMgr Singleton
- pal: Load all elf sections
- pal: Missing offset for CmdCloneImageData()
- pal: CmdBufferLogger: Add dump Viewports
- pal: Remove Legacy ELF Metadata
- pal: Improve the implementation of defer-freeing command chunk in
       QueueContext
- pal: Bump PAL_MINIMUM_INTERFACE_MAJOR_VERSION to 551 update
- pal: Remove unused enum type Gfx9InitMetaDataFill
- pal: Add support for DispatchMeshIndirectMutli

* Thu Jul 23 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.152.0.20200722.git080542c

- xgl: Prefer y-coordinate major swizzle modes for 3D color attachments
       on GFX10
- xgl: Update pNext Looping
- xgl: Update api version to 1.2.146
- xgl: Remove unnecessary NGG settings "EnableGsUse"
- xgl: Move dynamicStatesInternal to vk_pipeline.h and use xgl naming
       conventions
- xgl: Add ICache adapter
- xgl: Upate LLPC Interface in Vulkan to 40
- pal: Support tmz shader ring on GFX6
- pal: Disable metadata when TMZ enable
- pal: Fixing shared metadata bug of gfx6
- pal: Dead code removal - some methods were removed but the declarations
       are still there
- pal: Change doxygen style comments to non-doxygen
- pal: Restrict pipelined cache flush optimization to only cases where
       it's definitely legal
- pal: Bump version number to 264
- pal: Deferring chunk reuse as default
- pal: Support tmz shader ring on GFX6
- pal: Missing dcc state metadata init for InitMaskRam and
       InitMetadataFill
- pal: Don't disable alpha and color RB+ blend opts individually

* Thu Jul 16 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.151.0.20200710.gitc6404f7

- xgl: Redefine m_enabledFeatures in Device
- xgl: Implementation of extension: VK_EXT_private_data
- xgl: Update Vulkan headers to 1.2.145
- xgl: Amend behavior of disableLoopUnrolls tuning option
- xgl: Performance tuning of LLPC compiler for The Talos Principle in
       ultra mode
- xgl: Sort extension names as they appear in Khronos spec
- xgl: Performance tuning for Doom: Eternal
- xgl: Add support for extension: VK_EXT_extended_dynamic_state
- pal: Expose RWLockData to the client for Util::RWLock and add a Wait on
       RWLock for Util::ConditionalVariable
- pal: Move call to StartLateDeviceInit to clients
- pal: Add setting to override GbAddrConfigOverride input to AddrLib
- pal: [RPM] Add FP16 GenMips shader.
- pal: Performance tuning for Mad Max
- pal: [cmake] Minor style changes
- pal: [cmake] Fix GPU compile definitions
- pal: [cmake] Fixup some GPU override code
- pal: Add GFX9 support to Image Creation Developer Callback
- pal: [cmake] Fix documentation issue

* Tue Jun 30 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.150.0.20200630.git90a6644

- xgl: Add support for extension: VK_GOOGLE_user_type
- xgl: Disable NGG for GS by default
- xgl: Performance tuning for Remove Ghost Recon Breakpoint
- xgl: Update Vulkan headers to 1.2.143
- xgl: Performance tuning for Zombie Army 4: Dead War
- xgl: Improve performance of pipeline compiler by using
       PipelineAbiReader instead of Processor
- pal: [DebugOverlay] Solve a hang/crash when alt-tabbing with graph
       active
- pal: Change UseDcc panel key name with Gfx prefix
- pal: Bump version number to 263
- pal: [cmake] Add new cmake file PalCompileDefinitions.cmake and move
       calls to target_compile_definitions into their own files
- pal: Fix /analyze warnings
- pal: Add "Zero-copy" and "Reserve" semantics for ICacheLayer
- pal: Fix wrong assertions issue
- pal: Remove GPU CPU Sync from PAL Pipeline Creation in HwlInit
- pal: Fix mismatching wave sizes in a merged shader by always preferring
       the second stage (primary stage) and falling back to the first
       stage otherwise
- pal: [cmake] Move some modules from pal/cmake/Modules to pal/cmake
- pal: Filter redundant SET_BASE packets
- pal: Clean up other IsGfx10 references
- pal: Avoid creating a dmaUploadRing in case there is no dma engine
       available

* Wed Jun 24 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.149.0.20200624.gitfe996fc

- xgl: Fix Randr lease display is broken: find_package(XCB) is missed in
       cmake
- xgl: Update PAL Interface in Vulkan to 610
- xgl: Add a setting to return extra memory requirement via
       GetMemoryRequirements
- xgl: Add colors to cmake build
- xgl: Implement multigpu capture replay flag
- xgl: Fix driver crashes when setting basePipelineHandle to an invalid
       value
- xgl: Enable -Werror in dependencies if required
- xgl: Enable vkGetDeviceQueue2
- xgl: Fix Vulkan's debug_utils markers are not shown without a
       validation layer
- xgl: [metrohash][cwpack] Clean up dependency
- xgl: Add VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR in
       supportedCompositeAlpha
- pal: Handle a case where the CmdAllocator last paging fence can be
       zeroed
- pal: [cmake] Clean up the cmake override code
- pal: Improve some of our chip properties logic (physical WGP/CU counts,
       TCP counts)
- pal: Calculate Scratch ring maxScaledSize based on all availble video
       memory
- pal: Fix bit count so the union is 32b.
- pal: [cmake] Fixup installation logic
- pal: [cmake] Delete python/perl packages code
- pal: PAL interface bump 595 bug
- pal: [Vega10/Raven] Update DFSM/POPS related Workaround.
- pal: Updates settings gen script to correct number of setting hashes
       and regenerates all of the settings files
- pal: Make CmdCopyImageGraphics faster
- pal: Fix GpuProfiler memory leak regression
- pal: Put null backend code behind a compile flag. Enabled by default,
       but can be overriden by client drivers if they do not need or want
       this feature
- pal: Remove unneeded workaround code
- pal: Delete secure flag from amdgpu_cs_submit_raw2
- pal: [GFX9/10] Remove DFSM support.
- pal: Improve error messages in merge header script
- pal: [RGP] Provide a function to validate a list of perfCounters given
       a device
- pal: Bump version number to 260
- pal: [NGG] Phase 1 - Change the NGG culling constant buffer layout
- pal: [NGG] Remove some NGG culling constant buffer validation
- pal: [NGG] Workaround should only be considered when NGG is enabled
- pal: Use big page and iterate256 alignments from kmd. Part 2: Aligning
       unbound memory
- pal: [cmake] Fixup PAL options/overrides
- pal: [NGG] Make templated shaders NGG
- pal: Don't overwrite timezone to fix GPUOpen-Drivers/AMDVLK#162
- pal: Bump PAL_MINIMUM_INTERFACE_MAJOR_VERSION up to 500
- pal: Set presentable flag of image to gpumemory when opened shared gpu
       memory object
- pal: Add two new cmake files: PalOptions.cmake and PalOverrides.cmake
       for clarity and easier version control
- pal: Fix a nullptr crash when we set DisableAceCsPartialFlush = false
       and fix some memtracker errors in the GPU profiler
- pal: [cmake] Message Helper Functions
- pal: Add compositeAlphaMode to SwapChainProperties so that client can
       get it
- llpc: Shader Tuning opts for different titles
- llpc: Add shader_profiles/llpc to llpc feature

* Thu May 28 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.147.0.20200528.gitfc576d9

- xgl: Fix Vulkan RGP instruction tracing is not working
- xgl: Add wavesize tuning option for Doom Eternal for LLPC.
- xgl: Fix assertion failures with ShaderImageLoadStoreLod tests
- xgl: Allow building with LLVM_USE_SANITIZER
- xgl: Don't set threadSafe if useSharedCmdAllocator is false
- xgl: Turn off command buffer prefetch for local memory
- xgl: Add setting for cpDmaCmdCopyMemoryMaxBytes
- xgl: Add back the support for non local externally shared memory
- xgl: Fix CTS crash with Hybrid Graphics enabled on GFX10
- xgl: Add requireMrtForNggCulling to VK Panel Setting
- xgl: Add alignment for Attachments after Framebuffer
- xgl: Fix unaligned stencil load and store
- xgl: Add call to pScreen->GetColorCapabilities() back to Linux path in
       vkGetPhysicalDeviceSurfaceFormats()
- xgl: Enable TMZ feature
- xgl: Fix CLANG build
- xgl: Convert existing shader opt app profiles to json
- xgl: Fix LlpcOptions doesn't work when pipeline cache is enabled
- xgl: Fix OpAtomicIDecrement and OpAtomicIIncrement for
       shader_image_atomic_int64 extension
- xgl: Update PAL Interface in Vulkan to 604


- pal: Allow debug builds without assertions
- pal: Expand the SharedMetadataInfo structure to accomodate DCC on
       multiple aspect
- pal: Add forcedShadingRate to replace forceSampleRateShading in
       GraphicsPipelineCreateInfo
- pal: The max scratch ring size can now scale up based on the GPU's
       local invisible heap size
- pal: [GpuProfiler] Expand multiple instance config selection beyond
       just "ALL"
- pal: Resolve cs shaders dcl_literal minor bug
- pal: Use memcpy to allow unaligned footers
- pal: [NGG] allow to specify the constant buffer layout via a lookup
       table (LUT)
- pal: Remove "isNgg == false" from Tess control point for patches. This
       code was added in Gfx9 to handle the annoyance that was Gfx9 NGG
       and should no longer be necessary
- pal: Support scissor enabled image blit
- pal: Change maxWavesPerCu (in DynamicComputeShaderInfo and
       DynamicGraphicsShaderInfo) from uint32 to float, so clients are
       able to specify less waves. i.e. less number of waves than number
       of CUs per shader array.
- pal: Fix interface logger build when the client bump the version to 603
- pal: Fall back the pipeline upload memory to heap[0] = GpuHeapLocal  
       if there is no invisible heap
- pal: Fix pointer alignment check
- pal: Update merged PM4 header output
- pal: Replace some setting refs with cached settings
- pal: Replace some gfxip level checks with versions using m_gfxIpLevel
- pal: [RGA][PAL] Support retrieve isa dissembly per shader function for
       pipeline indirect mode
- pal: Move isResummarize from internal use to public and rename it to
       resummarizeHiZ, so clients are able to enable it
- pal: Support float type copy region in
       palCmdBuffer::CmdScaledCopyImage()
- pal: Remove 'adjacency' from the input assembler info when creating a
       pipeline
- pal: Batch RemapVirtualMemoryPages when queue is stalled to fix issue
       in some timeline waitBeforeSignal testing cases
- pal: Allow PAL's cmdAllocator to fall back to the visible heap if
       invisible is full (or doesn't exist at all)
- pal: Remove workaround for NGG as it is no longer required
- pal: Add tmzSupportLevel to indicate which queue supports per-command,
       per-submit, or per-queue TMZ based on the queue type
- pal: Properly align hash structs
- pal: Bump version number to 257

* Thu May 14 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.145.0.20200514.gitf98a1b7

- xgl: Enable VK_EXT_pipeline_creation_cache_control extension
- xgl: Implement VK_EXT_robustness_2 extension
- xgl: Use new FMask only image metadata mode when appropriate
- xgl: Remove CmdBufGpuEventMinAllocCount setting from settings_xgl.json
- xgl: Fix external memory CTS tests on platform that doesn't have local
       invisible heap
- xgl: Enable BUILD_WAYLAND_SUPPORT by default
- xgl: GraphicsPipeline constructor takes non-const reference
- xgl: Modify CmdBuffer::EndTransformFeedback to handle
       firstCounterBuffer correctly
- xgl: Fix GetSurfaceCapabilities2KHR for situation when pPalScreen is
       null
- xgl: Update Vulkan headers to 1.2.139
- xgl: Update PAL Interface in Vulkan to 595
- pal: Set AMDGPU_IB_FLAG_EMIT_MEM_SYNC flag
- pal: Add support for TMZ(trusted memory zone) feature
- pal: Update ilInstructionSet.cpp with new IL opcodes, and attempt to
       update existing opcodes with correct data for 'noModifiers'
- pal: Fix NGG small prim filter culling with custom sample positions
- pal: Fix app hang / crash related to shader ring change
- pal: Fix  Trackmania 2 glitchy graphical issue
- pal: Make pal separately reads Pal settings files for different PAL
       clients. For Vulkan, Pal will read amdVulkanSettings.cfg. If
       amdVulkanSettings.cfg does not exist, read amdPalSettings,cfg
- pal: Fix assertion failure triggering in  PAL + >=GFX9 when importing
       memory allocation into a 2D D32_S8 image
- pal: Fix vkGetRandROutputDisplayEXT on repeated calls
- pal: Query perf experiment Properties
- pal: Fix PAL_ASSERT bug in
       Pal::Amdgpu::Device::CreateGpuMemoryFromExternalShare
- pal: Fix typo for QueryProfiling memory clock
- pal: Correct a few errors in PAL's subgroup size calculation for NGG GS
- pal: Pack DepthStencilStateCreateInfo better to reduce the size
- pal: Remove the numScratchWavesPerCu public setting
- pal: [cmake]Create pal_include_guard helper function
- pal: Bump version number to 255

* Thu Apr 30 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.143.0.20200430.git7b51aa7

- xgl: Add framebuffer dimensions to ensure that we are not render
       outside the framebuffer
- xgl: Fixes for VK_EXT_conditional_rendering
- xgl: Automate shader tuning result code check-ins
- xgl: Fix ANGLE conformance test functional_transform_feedback crash
- xgl: Use pipeline options for shadow descriptor settings
- xgl: Enable pipeline binary cache by default
- xgl: Change the Catch-all Error to VK_ERROR_UNKNOWN
- xgl: [RGP] Fix incorrect start/stop frame/tag values reported back to
       SQTT file
- xgl: Fix the wrong VK_SAMPLE_COUNT_1_BIT setup
- xgl: Vulkan change to add YUV P210 format and MM formats for DCC for
       YUV.
- xgl: Remove "base_" from entry_points.txt and extensions.txt filenames
- xgl: Support VK_MEMORY_PROPERTY_PROTECTED_BIT
- xgl: Print compile time to log file
- xgl: Decouple the CMake of XGL and LLPC
- xgl: Update PAL Interface in Vulkan to 590
- pal: Add ElfReader and PipelineAbiReader
- pal: Use PipelineAbiReader instead of PipelineAbiProcessor
- pal: Add supportFp16Dot2 to DeviceProperties.
- pal: Improve CmdCloneImageData()
- pal:  [Wayland] Fix type mismatch issue
- pal: Update NGG culling buffer for viewports
- pal: Shadow of Tomb Raider benchmark performance tuning: remove GTT
       from the preferred heap for high priority GPU memory
- pal: Fix predication inheritance on compute command buffers
- pal: Add image usage flag to support view 3d as 2d array
- pal: [gfx10] Expand UMC(UMCCH) perf counter support
- pal: Add formats for DCC for YUV
- pal: Fix DescribeBarrier() assert
- pal: Fix an issue with fast clears of 3D images on GFX9. Use
       dccMipInfo.startZ as the starting slice for 3D images
- pal: Rewrite some PipelineUploader code
- pal: Update ComputeMaxSampleDistance to check all 4 pixels instead of
       just the topLeft pixel
- pal: Add support in PAL for YUV P210 format and MM formats for DCC for
       YUV.
- pal: [Gfx10] Add write to PA_SC_NGG_MODE_CNTL
- pal: Revert programming of cmask pipe-align bit when no cmask is
       present
- pal: Don't allocate fast clear eliminate metadata for image with
       comp-to-single (and disable comp-to-reg) support
- pal: [GFX9/10] Switch Workaround class to reference CachedSettings
- pal: Use gfx engine instead of compute engine for CmdCopyImage to sRGB
       image without format conversion
- pal: [GFX9/10] Fix a bug in Workaround PreDraw
- pal: Rename CommonShaderStats.stackFrameSizeInBytes to be
       CommonShaderStats.maxStackFrameSizeInBytes.
- pal: Add PFP_SYNC_ME before LOAD_CONTEXT_REG_INDEX loading memory into
       mmVGT_STRMOUT_DRAW_OPAQUE_BUFFER_FILLED_SIZE
- pal: Add DbgPrintCatMsgFile
- pal: Update ILP opcode table and asserts
- pal: Fix off by one size check issue in PAL settings code
- pal: Bump version number to 253

* Thu Apr 16 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.140.0.20200416.gitc59322a

- xgl: Enable Renoir support
- xgl: Update the code to source the max compute shared memory size from
       PAL rather than using a hardcoded constant
- xgl: Implement VK_KHR_incremental_present
- xgl: Add panel setting to disable AMD Vendor extensions. Enabling this
       panel setting will remove AMD extensions from the list of enabled
       and supported extensions
- xgl: HDR support without the need for
       VkSurfaceFullScreenExclusiveWin32InfoEXT
- xgl: Properly report MSAA support
- xgl: Add limitation on cache directory size
- xgl: Add mandatory execution of CmdSetGlobalScissor
- xgl: Clean up promoted KHR/EXT suffixes
- xgl: Update Vulkan Headers to 1.2.135 + BETA
- xgl: Remove 1.1 build and headers
- xgl: Update PAL Interface in Vulkan to 582
- pal: Add Renoir support
- pal: Alert when default hash function is used for non-pointer keys
- pal: Add -Wconversion -Wno-sign-conversion to gcc flags
- pal: Add  adaptive sync support which could be enabled with PAL setting
       “EnableAdaptiveSync”
- pal: Convert Gfx6 chip headers to use constexpr
- pal: Add support for DCC compression on planar YUV surfaces
- pal: Remove ALLOC flag from some ELF sections
- pal: Fix an issue where scratch allocations, once multipled for wave
       size, could be under the WaveSize granularity
- pal: Add support for fast clears of YUV surfaces
- pal: Add two debug options for memory tuning.
- pal: Introduce `$<COMPILE_LANGUAGE:CXX>` for some flags, specifically
       -std=c++11, -fno-rtti and -fno-threadsafe-statics
- pal: Add RemoveFilesOfDir and GetStatusOfDir in Pal Util
- pal: Polyphase filter bug fix
- pal: Add Cmake helper modules to encapsulate pal's compiler options
- pal: Cmake helper modules to encapsulate pal's compiler options
- pal: Add PipeUnaligned path for Gfx9MaskRam::CalcMetaEquationGfx10()
- pal: Fix CmdSetGlobalScissor states
- pal: Add predication suspend/resume and command buffer inheritance
       option
- pal: Bump version number to 250
- llpc: Enable Renoir support

* Sat Mar 28 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.139.0.20200326.gitd5ddc3f

- xgl: Shader tuning:  add options in app shader profile to set waveSize
       to 64 for some compute shaders
- xgl: Make compatible change for moving non-LLPC declarations and code
       out of llpc directory
- xgl: Spec behaviour change for vkGetDeviceProcAddr
- xgl: Update PAL Interface in Vulkan to 575
- pal: Add more choices to the VAR swizzle panel option for performance
       runs
- pal: Implement DevDriver::BaseEventProvider on the EventProvider
- pal: [GPUProfiler] Improve parsing of config EventId field values
- pal: [GFX9/10] Add a UseDcc setting bit for DCC on Array+MipMap Images.
- pal: Adding AtomicWriteRelaxed64 and AtomicReadRelaxed64. These are
       needed to handle 64-bit atomics on 32-bit CPUs
- pal: Define NOP-embedded signatures in the interface so that more
       client drivers can utilize them through the ICmdBuffer::CmdNop()
       function
- pal: Turn 451 context RMWs into 57 sets (as measured in the Skyros
       benchmark) by making SC_PA_AA_CONFIG draw-time sta
- pal: Fix SPM block instance programming for the TA, TD, and TCP on
       gfx10
- pal: Flush CB metadata for images with metadata only
- pal: Enable Immediate and Mailbox mode for direct display
- pal: [GFX9/10] Minor CPU opt to use cached pipeline flags
- pal: Remove dead param/template param and trivial UpperCamelCase fixes
- pal: Add ability to use stack frame size to determine scratch memory
       usage of pipelines with indirect shader functions
- pal: Fix conversion from 'size_t' to 'type' issue

* Fri Mar 13 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.137.0.20200312.git12df867

- xgl: Enable flip by default
- xgl: Expose VK_EXT_post_depth_coverage extension
- xgl: Expose VK_EXT_texel_buffer_alignment extension
- xgl: Expose VK_KHR_non_semantic_info extension
- xgl: Enable fullCopyDstOnly for MSAA color image for Thrones of
       Britannia
- xgl: Amend shader tuning for some games (Talos principle, Serious sam…)
- xgl: Map VkComponentSwizzle to LLPC YCbCr Sampler Enum
- xgl: Add Vulkan ApiType in GpaSession constructor as in new, 575 PAL
       version.
- xgl: Call Pal::Screen::SetColorConfiguration in
       FullScreenMgr::SetHdrMetaData
- xgl: Update VkToPalGlobalPriority
- xgl: Update Vulkan headers to 1.2.133
- xgl: Update PAL Interface in Vulkan to 570
- pal: Add SPM VCOPs only when SPM trace is enabled.
- pal: [GFX9/10] Add panel setting to force all CUs/WGPs for NGG
- pal: Use ReclaimAllocations3Cb for PAL
- pal: Define ReclaimResult enum interfaceLogger
- pal: Include padding to avoid corruption in non power of two compressed
       textures on Gfx9 and Gfx10 when using the CopyImage2DMipLevel
       shader
- pal: ValidateDraw is getting too long to fit into one chunk. Split it
       around the center.
- pal: [Gfx10] Fix scratch sizes when Wave64
- pal: Only set GE_CNTL.BREAK_WAVE_AT_EOI for Tessellation shaders
- pal: Allow clients to specify ApiType in RGP files saved through
       GpaSession
- pal: Rewrite parse barriers to work with the latest GPU profiler logs
- pal: Disable SDMA for Linux while it's set in Setting
- pal: [ShaderDbg] Add mode to avoid dumping to disk
- pal: Remap QueuePriority to AmdgpuPriority
- pal: Fix the UnmapVirtualPages for deleted memory
- pal: Fix compiling error when enabling PAL_DEBUG_PRINTS
- pal: Support programming GE_CNTL properly for single-wave subgroups
- pal: Add a new HwPipePreColorTarget in HwPipePoint enum.
- pal: Enable additional VK_KHR_buffer_device_address feature flags
- pal: Remove some redundant context rolls and fix late alloc VS when the
       PM4 optimizer is enabled
- pal: VK_KHR_incremental_present implementation for Wayland
- pal: Add override to functions
- pal: Add PFP_SYNC_ME when stopping perf experiment
- pal: Move SPI_SHADER_REQ_CNTL_VS/PS to the graphics queue context
- pal: Disable the SPI user accumulators in the preamble streams instead
       of doing it every time we bind a pipeline
- pal: Set VAR swizzle to disable by default. Investigating some perf
       drops with it enabled
- pal: Bump version number to 249

* Sat Feb 22 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.134.0.20200221.gitb81c3a0

- xgl: Enable VK 1.2 build by default
- xgl: Support barrier for streamout buffer
- xgl: Fix compilation with cmake and clang
- xgl: Fix Vk GPA extension not returning correct return code
- xgl: Adjust parameter setting after Pal FenceOpenInfo change
- xgl: Disable VK_IMAGE_CREATE_SPARSE_BINDING_BIT for images with YUV format
- xgl: Fix a potential stack overflow issue
- xgl: Change the command line unrolling threshold and partial-unrolling
       threshold options passed to LLVM so that they are only passed for
       apps that actually need non-default values to be used
- xgl: Fix the issue that clearing 3D image views (created from 3D PRT
       images) via clear load ops does not work as expected
- xgl: Wait for a per swap chain image fence before generating post
       processing commands
- xgl: Fix GetMemoryRequirements for buffer size MAX_UINT64
- xgl: Replace use of unroll threshold option by shader tuning
- xgl: Update PAL Interface in Vulkan to 567
- pal: Image corruption during memory defrag copy (Corrupt non power of 2
       textures)
- pal: Fix random failure with XFBCaptureAndVerifyOnHost test cases when
       using vkDrawIndirectByteCountEXT() draw calls
- pal: Fix extra DccDecompress just before present if fullResolveDstOnly
       is set
- pal: Add a developer mode event service for forwarding events out the
       message bus in a lightweight way
- pal: Add a new type FmaskOnly for Image MetadataMode which makes color
       msaa Image only have Cmask/Fmask metadata
- pal: Avoid issue TCC metadata cache invalidation for image without
       metadata
- pal: Allow compressed copySrc layout for color msaa image that supports
       MetaDataTexFetch
- pal: Fix a minor logic error causing a whole bunch of extra updates to
       DCC state metadata inside PAL barriers
- pal: [GFX9/10] Remove need for RMW of CB_COLORx_INFO registers in most
       cases
- pal: Add PAL panel setting DisableSdmaEngine for debug purpose, the
       default value is false
- pal: Fix a bug of DCC constant encoding
- pal: Fix a memory corruption bug
- pal: Remove hardcoded timestampResetOnIdle value for Vega 20
- pal: Fix a nullptr dereference due to an earlier OOM error.
- pal: Prevent the GPU profiler from turning every barrier's cache masks
       into garbage
- pal: Change CB_COLOR_INFO programming on Nested CmdBuf to be more like
       the old path
- pal: Mute the assertion for shaderWrite==0 for GFX9 when metadataMode
       is ForceEnabled
- pal: Fix excessive context rolls from waLqoHangWithRbPlus
- pal: [AcqRelBarrier] Optimizations on the use of WAIT_REG_MEM and
       WRITE_DATA packets
- pal: Work-around CTS 1.2 api.image_clearing.*.clear_depth_stencil_*
       random failures on Linux for asics before gfx10
- pal: Don't do a fast compute depth clear outside of [0, 1] range, fixes
       dEQP-VK.pipeline.depth_range_unrestricted.*d32_sfloat_* by
       avoiding the compute path
- pal: Implement writing scaled copy regions in CmdBufferLogger
- pal: Notify tools of errors via Developer Callback
- pal: Add wave32 support for indirect command generator dispatches
- pal: Move graphics pipeline DB_RENDER_OVERRIDE RMW to the command
       buffer and add a DISABLE_VIEWPORT_CLAMP override
- pal: Disable DCC on mipmap array resource by default and adjust the
       UseDCC validation logic
- pal: Optimize Gfx10CreateUntypedBufferViewSrds to match GFX9 version
- pal: Mute assert to allow fixed 0 tileSwizzle value for
       non-single-sampled-color image
- pal: Fix ODR warnings from SDMA under GCC
- pal: Fix number of available VGPRs being reported
- pal: Percolate errors from Profiler up to the client
- pal: Fix PageFault in RenderDoc replay related to CB_COLOR_INFO dirty
       logic
- pal: Removal of Gfx10 specific builds of PAL
- pal: Bump version number to 248

* Thu Jan 23 2020 Tomas Kovar <tkov_fedoraproject.org> - 2.127.0.20200121.git813f090

- xgl: Implementation of partial pipeline compile
- xgl: Initial implementation of VK_EXT_conditional_rendering
- xgl: Update Vulkan headers to 1.1.130/1.2.131
- xgl: Implementation of VK 1.2 support (could be enabled by
       USE_NEXT_SDK)
- xgl: Some APU/GPU doesn't have invisible heap, we shouldn't initialize
       a none-existent memory heap.
- xgl: Fix bugs in CmdBuffer::BindTransformFeedbackBuffers()
- xgl: Shader tuning for Rise of Tomb Raider
- xgl: Shader tuning for DiRT4
- xgl: Add support for the inherited occlusion query for secondary
       command buffer
- xgl: Fix corruption observed while running vkmark
- xgl: Add a shader tuning option "unrollThreshold" to allow the default
       loop unroll threshold used by LLVM to be initialised to the
       specified value
- xgl: Hook up alphaToOne support
- xgl: Fix build link error while using Clang
- xgl: Add Capture/Replay support for VK_KHR_buffer_device_address
       extension
- xgl: Make sure pBufferDeviceAddressCaptureReplay is FALSE until we
       fully support pBufferDeviceAddress
- xgl: Update PAL Interface in Vulkan to 556
- pal: Add ClearColorType::Yuv and handle both packed and planar clear
       color when this ClearColorType is specified.
- pal: Remove WritePm4Image
- pal: Add color to depth and 1xAA depth to depth gfx compressed copy
       support
- pal: Make sure client overrides of DCC modes don't override internal
       debug work
- pal: Add PresentMode to CmdPostProcessFrameInfo so that it can be
       printed in the PAL debug overlay
- pal: Modify Pal::MaxUserDataEntries to 128
- pal: Remove the redundant empty submission which has already been
       handled by xgl for the wait semaphore
- pal: Add a new image creation flag "fullCopyDstOnly"
- pal: Fix the link error for Clang build
- pal: Hardcode PA_SC_BINNER_CNTL_0.FLUSH_ON_BINNING_TRANSITION = 1
- pal: Give a chance for clients to force enabling DCC for RT+UAV
       resources
- pal: Don't call IsHtileDepthOnly on an image unless that image actually
       has hTile data
- pal: Use deallocate2Cb instead of deallocateCb
- pal: When GS instancing is enabled with the use of API GS, the GS-VS
       ring allocated on on-chip LDS requires more space
- pal: timingReport: Don't print the directory walk status if the output
       is being piped to a file
- pal: Clean up VAM on failed initialization
- pal: Internal memories are possibly allocated before queue creation,
       need to add them into the queue memory reference list while
       creating queue
- pal: Fix NGG GS issue for CTS failure in
       dEQP-VK.geometry.basic.output_vary_by_attribute_instancing
- pal: When GS instancing is enabled with the use of API GS, the GS-VS
       ring allocated on on-chip LDS requires more space
- pal: Set m_pCurrentExperiment dangling pointer to nullptr in
       GfxCmdBuffer::CmdEndPerfExperiment()
- pal: Bump version number to 246

* Mon Dec 23 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.123.0.20191219.gite6d1928

- xgl: Enable VK_KHR_shader_float_controls extension
- xgl: Enable  VK_KHR_separate_depth_stencil_layouts extension
- xgl: Implement VK_KHR_buffer_device_address extension
- xgl: Add disableLicm tuning option
- xgl: Enable VertexAttributeInstanceRateZeroDivisor
- xgl: Add Query Pool support for Acceleration Structures
- xgl: Remove a workaround for the issue that Elite Dangerous game is too
       bright as the defect in SkipFceOptimization is fixed in PAL
- xgl: Fix crash triggered by Sparse bind + timeline semaphores
- xgl: Don't disable depth clamping unless
       VK_EXT_depth_range_unrestricted is requested.
- xgl: Update vulkan_core.h to Vulkan 1.1.129
- xgl: Update PAL Interface in Vulkan to 552
- pal: Track the presentable memory and do not add window system owned
       presentable memory into resource list.
- pal: Correct SDMA Predication logic
- pal: Fix a mismatch between GetFastClearCode's pNeedFastClearElim and
       IsFastClearColorMetaFetchable
- pal: Correctly set the bits for the ACQUIRE_MEM packet
- pal: Update libdrm header files
- pal: Fix assertion failure triggers at Vulkan device creation time &
       during cmd buf recording
- pal: Fix performance drop issue of vkmark and vkcube when flip is
       enabled
- pal: Optimize CmdGenerateMipmaps
- pal: Don't supply the KMD with allocation requests involving heaps that
       don't exist.
- pal: Initial implementation of the new command buffer dumping path
- pal: Remove WritePm4Image, Part #1 and 2
- pal: Bump version number to 244

* Fri Dec 13 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.121.0.20191212.git887460b

- xgl: Enable VK_EXT_pipeline_creation_feedback extension
- xgl: Enable SUBGROUP_CLUSTER_SUPPORT
- xgl: Increase app specific unrolling threshold value as other changes
       meant that the value was not sufficient to ensure loops were
       unrolled for the app
- xgl: Consolidate code to look up pipeline binary in caches
- xgl: Changes for GPU memory event logging
- xgl: Update the shader optimizer for Dawn of War 3
- pal: Enable waUtcL0InconsistentBigPage for GFX10
- pal: Add Util::Gcd() and Util::Lcm() functions
- pal: Fix typo drity -> dirty
- pal: enable iterate256 in cases where the vram bus size is not a power
       of 2.
- pal: Fix few CTS failures for Navi14, that does not handle cmask enable
       and DCC disabled situation during checking the first mipmap level
       for a single aspect when suffers the pipe-misaligned metadata
       issue on GFX10
- pal: Updates the block enum in the file format spec.
- pal: Adds a static assert to ensure updating this enum for any future
       block additions in PA
- pal: Store UserData dirty bits as size_t instead of 16b
- pal: Cleaning up warnings in PAL/mmPipelines
- pal: Correct the behaviour of Amdgpu::Device::ReserveGpuVirtualAddress()
- pal: Add "PAL_CLIENT_INTERFACE_MINOR_VERSION" definition in cmake
- pal: Remove GDS
- pal: Fix HiStencil (and all of RPM) by always using the compiled spill
       threshold
- pal: Bump version number to 242
- llpc: Revert [PR273] Group BuiltInTessLevel* stores together

* Wed Nov 27 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.119.0.20191125.gitb2600e0

- xgl: Add Navi14 support
- xgl: Support VK_EXT_pipeline_creation_feedback extension
- xgl: Support VK_EXT_shader_demote_to_helper_invocation extension
- xgl: Shader performance tuning for TOTALWAR WARHAMMER II and DiRT4
- xgl: Fix spirv_assembly.instruction.compute.float_controls
       .independence_settings.independence_settings test failures
- xgl: Remove implementation for vkFlush/InvalidateMappedMemoryRanges
- xgl: Implement VK_KHR_sampler_ycbcr_conversion
- xgl: Implement VKI_KHR_SEPARATE_DEPTH_STENCIL_LAYOUTS
- xgl: Update Vulkan headers to 1.1.127
- xgl: Bump up LLPC version to 38 to remove app shader cache interface
- xgl: Bump PAL interface version to major=548, minor=1
- pal: Add Navi14 support
- pal: GFX10: Setting SX_PS_DOWNCONVERT_CONTROL to cause HW to obey the
       driver's programmed value of SX_PS_DOWNCONVERT
- pal: Reenable vertex grouping
- pal: Enable single thread for immediate mode.
- pal: Discard the reply for presentPixmap request since it should never
       be failed. Just flush the xcb requests
- pal: GFX10: Modify default of VGT_TF_RING_SIZE based on HW feeback
- pal: Fix an issue where the stencil hTile aspect would remain
       uninitialized for surfaces that had perSubResInit==0
- pal: Fix for dEQP-VK.pipeline.depth_range_unrestricted.*d32_sfloat* -
       tests failure
- pal: Fix an issue where compute based depth expands would push the
       compute state twice without popping it
- pal: Add atomic OR functions
- pal: Support 32-bit predication
- pal: SwapChainMode::Immediate can be inline
- pal: [GFX9/10] Correct CB fixed function resolve condition checking
       logic
- pal: Add isMergedShader to RelocatableShaderFlags. Always use this flag
       to check if this is a merged shader
- pal: Correct shader dump in DisassembleShader
- pal: Remove duplicated codes in SetupPreCompileRegisters
- pal: Bump version number to 241

* Fri Nov 08 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.117.0.20191108.gitff4e604

- xgl: Support VK_KHR_shader_subgroup_extended_types extension
- xgl: Support VK_KHR_pipeline_executable_properties extension
- xgl: Support VK_KHR_TIMELINE_SEMAPHORE extension
- xgl: Support VK_KHR_SHADER_CLOCK extension
- xgl: Support VK_KHR_SPIRV_1_4 extension
- xgl: Enable computeFullSubgroups support
- xgl: Switch vk pipeline cache to PAL pipeline binary cache
- xgl: Shader tuning for game Rise of Tomb Raider
- xgl: Remove use of dynamic loop unrolling
- xgl: Use the correct engineIndex when substituting Compute for Transfer
       engine
- xgl: Update Vulkan headers to version 125
- xgl: Update PAL Interface in Vulkan to 547
- pal: Enable DB-CB fix function resolve in PA
- pal: AcqRelBarrier] Narrow down the scenario that release at BOP due to
       no VS_DONE.
- pal: Remove texture quilting support as no future HW will support this
- pal: Fix a DMA bug uncovered by the PCIe copy optimization
- pal: Enable tile-mode when present gpu is rendering gpu
- pal: Disable use of CE IB2's in gfx10
- pal: Remove copyFormatsMatch and replace the "CopyDst is compressed"
       logic with settings
- pal: Ignore the "useCpuPathForTableUpdates" flag and the
       "cmdBufForceCpuUpdatePath" setting on products that don't support
       a constant engine
- pal: Provide a CPU-based version of the UpdateNggCullingDataBuffer
       function for use with products that don't have a constant engine
- pal: Fixed some gcc unused variable errors
- pal: Remove the remaining CE ram reference, used with inherited command
       buffers
- pal: Don't use doubles in any RPM shaders
- pal: Fix possible null dereference when deallocating memory
- pal: Disable vertex grouping except in cases where necessary (NGG Fast
       Launch)
- pal: Account for the sdl address user data registers when calculating
       the available ones
- pal: [GFX9/10] expose settings for CB/DB policy change
- pal: Fix the order of the tags for this setting so that it will
       actually show up in the panel
- pal: Bump version number to 237

* Tue Oct 22 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.115.0.20191022.gitaab8cd0

- xgl: Add VKI_EXT_HOST_MAPPED_FOREIGN_MEMORY support
- xgl: Fix build error when LTO is disabled
- xgl: Update SPIR-V headers
- xgl: Remove static asserts for ABI shader types
- xgl: VertBufBindingMgr::GraphicsPipelineChanged should use device mask
- xgl: Fix numSlices in Pal::ImageScaledCopyRegion
- xgl: Memset driver name and info strings
- xgl: Preserve the default values for runtime settings that are not
       overwritten with an app profile
- xgl: Update PAL Interface in Vulkan to 543
- xgl: Implement VK_EXT_post_depth_coverage
- xgl: Re-work vkPipelineCache
- xgl: Add "enableLoadScalarizer" option to app_shader_optimizer
- xgl: Tune shader performance for F1 2017 and the Talos principle
- xgl: EXT_vertex_attribute_divisor: Add missing features query and
       support verification
- xgl: Fix a case fallthrough bug with
       VK_AMD_memory_overallocation_behavior at device creation
- xgl: Move platformKey to physical device
- xgl: Make InitializePlatformKey() as a void function
- xgl: Add ShaderDbg to LLPC
- xgl: Bump LLPC client interface version to 34
- pal: Ensure that the two resources have identical layouts before
       enabling an alignment optimization during a subresource copy
- pal: [AcqRelBarrier] Fix a hole that may cause missing a
       MsaaColorDecompress.
- pal: GFX10: Fix an assert related to a zero max-event-ID by using the
       correct enum for the GE1 block
- pal: Remove "using namespace" from gpuUtil headers
- pal: Add 32 bit Streamout Query support
- pal: Add setting for ASTC format
- pal: Allows clients/layers to embed a binary payload directly into the
       command stream for better tooling
- pal: Fix IFH mode back-compatibility issue
- pal: Add a condition to mark MSAA images with samples>1 and with
       DepthStencil and ShaderWrite aspect to be Unsupported
- pal: Fix null pointer in cmdBufferLogger
- pal: [AcqRelBarrier] Maintain an auto-release info hashmap for acquires
       to clear CmdBufState flags
- pal: Add shaderClock features to gfxipProperties.flags
- pal: DrawDispatchInfo Addition to Cmd-Stream
- pal: [Sqtt] Modify SQTT size and base reg write order + Change thread
       trace token config reg mask enumeration
- pal: Shader functions regCOMPUTE_PGM_RSRC1 gfx10 registers need to be
       taken into account for the pipeline
- pal: Extend list of supported keys
- pal: Fix image corruption presented on screen with multiGPU
- pal: Add the global sync flags to the command buffer logger output
- pal: Bump version number to 235

* Mon Sep 23 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.109.0.20190923.git8a1733a

- xgl: Modify the NGG culling settings to be specified on a pipeline type
       basis instead of globally,
- xgl: Enable VK_AMD_device_coherent_memory extension
- xgl: VK_EXT_calibrated_timestamps: Enhance error handling when an
       invalid time domain is specified
- xgl: [mGPU] vkEnumeratePhysicalDevices will always rank Navi after
       Vega/Polaris
- xgl: Implement pipeline elf cache
- xgl: Expose VK_EXT_line_rasterization extension
- xgl: Enable VK_EXT_calibrated_timestamps extension
- xgl: Tune shader performance for Serious Sam Fusion 2017
- xgl: Tune shader performance for DawnOfWar3
- xgl: Implement VK_KHR_pipeline_executable_properties
- xgl: Fix Memory Leak in VK_Semaphore
- xgl: Implement shader module async compile
- xgl: App detect Elite Dangerous to avoid corruption
- xgl: Bump up LLPC version to enable interface 32 “Add
       ShdaderModuleOptions in ShaderModuleBuildInfo”
- xgl: Update PAL Interface in Vulkan to 527
- xgl: Update Vulkan headers to 1.1.121
- xgl: Build cwpack from external third_party/cwpack path
- xgl: Fix  crash when calling vk_EXT_debug_utils extension when using
       DevDriver
- xgl: Add  lots of missing enabled feature verification for device
       create
- pal: Fix potential bug with max_size programming in indexed draw
       packets
- pal: [GFX10] Drop Z/Stencil base writes for the NULL DSV case
- pal: Fix an interface logger formatting bug in SubmitInfo
- pal: [GFX9/10] Merge three sequential ranges into one in GS pipeline
       chunk context regs
- pal: [mGPU] vkEnumeratePhysicalDevices will always rank Navi after
       Vega/Polaris
- pal: Disable PAL Internal CE Usage By Default
- pal: Fix internal state tracking that depends on AddGpuMemoryReferences
       and RemoveGpuMemoryReferences
- pal: Initialize HiZ to expanded instead of "equal to zero", Htile inits
       are now the same as resummarizes
- pal: GFX10: Add CalcMetaEquation support for DCC/Cmask/hTile
- pal: Prevent busy chunk tracking from reusing chunks while shaders are
       reading from them
- pal: CB fixed function resolve cannot be performed if the src and dst
       array slice is different
- pal: Change to GetShaderStats to return ApiShaderStageGeometry when
       IsGsEnabled() is enabled
- pal: [AcqRelBarrier] CmdBufferLogger missing image transition dump
- pal: [AcqRelBarrier] Don't request RB sync if FastClearEliminate is not
       submitted
- pal: Remove duplicate CAS shader binaries from our DLLs and add
       "#pragma once" to some pipeline headers
- pal: Add finer grained MALL control for CBs, DBs, and SRDs. Some blocks
       provide fine grained disabling of MALL usage
- pal: Implement pipeline elf cache
- pal: Clean up cwpack dependency, support build with external cwpack
- pal: Skip programming scratch related registers for the AQL dispatch
       when they're not required.
- pal: [GFX6-10] Minor CPU opt to convert pass by ref to pass by value
- pal: Fix IL_OP_LDS_STORE_B64 instruction definition
- pal: Skip programming scratch related registers for the AQL dispatch
       when they're not required
- pal: [GFX9/10] - Rework DB_DFSM_CONTROL programming
- pal: [AcqRelBarrier] New barrier path the acquire doesn't need to
       invalidate RB
- pal: Fix bad free's in pipeline upload
- pal: Clean up the PAL NGG settings
- pal: Load alwaysOnCuMask from deviceInfo
- pal: GFX10: Fix (hide...) a potential access violation with generating
       the (unneeded) cMask addressing equation
- pal: Add CmdGenerateMipmaps to automatically and efficiently generate
       mipmap levels
- llpc: Refine NGG implementation
- llpc: Port [PR218] Revert "[PR156] Builder trigonometric, exp, log,
        inverse sqrt"
- llpc: Port [PR202] Revert PR162 "PatchDescriptorLoad: extract
        buildBufferDescriptor"
- llpc: Port Fix gfx10 smod compile bug
- llpc: Port [PR191] Reinstated CapabilityImageGatherBiasLodAMD

* Thu Aug 29 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.105.0.20190829.gita14d42d

- xgl: Update Vulkan headers to 1.1.119
- xgl: Expose VK_EXT_subgroup_size_control version 2
- xgl: Talos principle performance tuning
- xgl: Back out the change that added system info into account for UUID
- xgl: Pipeline cache UUID: move calculation to physicalDevice:Init
- xgl: Switch to the new DivergenceAnalysis pass, re-enables atomic
       optimizations for Three Kingdoms.
- xgl: Fix Semaphore Handle Leak
- xgl: Implementation for VK_EXT_calibrated_timestamps
- xgl: Implementation  for VK_KHR_pipeline_executable_properties
- xgl: Fix memory leak in memoryCache
- xgl: Build driver with external single instance of Metrohash
- xgl: Set entryStage in Device::CreateInternalComputePipeline
- xgl: Update LLPC Interface in Vulkan to 31
- pal: switchVgtOnDraw should 0 by default
- pal: Re-enable SkipFceOptimization feature in PAL
- pal: [AcqRelBarrier] Port SkipFceOptimization to acquire/release
       barrier
- pal: [AcqRelBarrier] Adjust layout transition info struct to apply
       optimization
- pal: Add support to build PAL with external single instance of
       Metrohash
- pal: Disable comp-to-single for 8bpp and 16bpp by default.
- pal: Add Gfx10UseCompToSingle8bpp and Gfx10UseCompToSingle16bpp to
       'UseCompToSingle' panel setting, so we can set panel to force
       comp-to-single for 8bpp and 16bpp surface.
- pal: [NGG] Fast Launch requires the index buffer address to be written
       to different registers with the correct value
- pal: Change the definition of HDMI_STATIC_METADATA_TYPE1 to 0
- pal: Support FORMAT_A2B10G10R10_UNORM_PACK32 format for HDR
- pal: Fix HDR test hang
- pal: Fix segment fault in memoryCache
- pal: Bump version number to 229
- llpc: Implementation for VK_KHR_spirv_1_4
- llpc: Clean up Metrohash dependency, add support to build llpc with
        external single instance of Metrohash

* Thu Aug 15 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.104.0.20190815.gitddb9bc0

- xgl: Support VK_EXT_subgroup_size_control extension
- xgl: Set allowExternalPipelineCacheObject to false by default
- xgl: Enable Atomic Optimizations for all ASICs to fix ICD
       initialization failure for system with a mix of GFX10 and other
       GFX versions ASICs
- xgl: Fix crash with AMD GPU disabled
- xgl: Add system info into account for UUID
- xgl: Return VK_SUBOPTIMAL_KHR from queuePresent and acquireNextImage if
       surface resolution has changed.
- xgl: Fix the getQueryPoolResults for not ready queries
       VK_QUERY_TYPE_TRANSFORM_FEEDBACK_STREAM_EXT
- xgl: Update reported CTS version in VK_KHR_driver_properties
- xgl: Update Vulkan headers to 1.1.116
- xgl: Update PAL Interface in Vulkan to 525
- xgl: Use a higher unrolling threshold for two apps that lost
       performance due to the previous unrolling changes.
- pal:  Bump version number to 228
- pal:  Update PAL_MINIMUM_INTERFACE_MAJOR_VERSION to 465
- pal:  [Gfx10] Fix programming of mmSPI_SHADER_REQ_CTRL_VS
- pal:  Fix SPM being missing for compute dispatches
- pal:  Add locks around all gpaSession-shared state that timed queue
        operations touch
- pal:  Move disableAlphaToCoverageDither to flags bitfield
- pal:  Fix signed vs. unsigned mismatches
- pal:  [DbgOverlay] Display peak mem usage in PAL Debug overlay
- pal:  Fix an issue that the setting DisableSyncObject failed to exclude
        the kernel compatibility/support check when DisableSyncObject is
        set to true.
- pal:  Fix PAL_ASSERT bug in Pal::Amdgpu::GpuMemory::OpenSharedMemroy
- pal:  Fix LlpcOptions not working with amdPalSettings.cfg file when
        trying to set multiple options
- pal:  Add new syncobj query interface v2
- pal:  QueueSemaphore: add WaitBeforeSignal support v6
- pal:  Restore pipeline registers state if nested command buffer have a
        pipeline or set pipelineDirty flag
- pal:  Add support for programing the PA_SC_LINE_STIPPLE register
- pal:  Improve ScaledCopyImage() performance
- pal:  First fix for resolve failures when FMASK disabled
- pal:  Deprecate IDevice::ScpcGraphicsPipelineTuningOptions. We want to
        move away from having PAL settings that directly control what the
        compiler does, and move them into the compiler instead
- llpc: Refine NGG implementation
- llpc: Implement VK_KHR_spirv_1_4 support
- llpc: Remove llpcPatchGroupOp files
- llpc: Fix CTS test dEQP-VK.binding_model.descriptorset_random.* - tests
        failing
- llpc: Add !invariant.load to load descriptor sets
- llpc: Set fast math flags on more FP ops in the SPIRV reader
- llpc: Remove waterfall loop from Builder interface 
- llpc: Rework image ops in SPIR-V reader to use Builder interface

* Mon Jul 29 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.101.0.20190729.git53d1a7c

- xgl: Support extension VK_KHR_imageless_framebuffer
- xgl: Support extension VK_AMD_shader_core_properties2
- xgl: Vulkan Settings Refactor to enable modification of vulkan settings
       through developer tools (RDP
- xgl: Call CmdBuffer::End() after CmdBuffer::Begin(), to ensure the
       m_recordState in Pal is correct
- xgl: Fix smoke flickering in game Three Kingdoms
- xgl: Fix incorrect behavior with OpImageSampleExplicitLod + Lod|Offset
- xgl: Vulkan Resource DCC Tuning
- xgl: Navi10 performance tuning for Dirt4, Totalwar:WarhammerII, F1 2017
- xgl: Fix PAL debug overlay with SW compositing
- xgl: Update PAL Interface in Vulkan to 518
- pal: [GFX6-10] - Minor simplifications to ColorBlendState objs.
- pal: Resolve occlusion/pipeline stats query: always write availability
       data
- pal: Add missing support of IL_OP_SAMPLE_XXX_PO to ILP
- pal: [GFX9/10] Reduce the size of Gfx9MaskRam class
- pal: [GFX9-10] Minor tweak to Gfx9Fmask
- pal: [GFX6-10] Remove unneed m_device ref from Gfx*MsaaState
- pal: GFX6-8] Port some minor DepthStencilState space savings from GFX9
       hwl
- pal: [GFX6-10] Remove device pointer from several hw-independent state
       object classes
- pal: Optimize ACE offload for WaitRegMem
- pal: Pal::Amdpg::Platform::ReQueryDevices() - Exiting this function
       gracefully instead of segfault
- pal: Fix bug in gfx9 perf experiment legacy SQ counter stop sequence
- pal: Setting clock mode through driver ext should fill in the shader
       and memory clock freq in RGP asic_info chunk
- pal: Fix Vk.api.device_init.create_instance_device_intentional_alloc_fail
       test failure
- pal: Initialize the enableTcpBigPageTranslationCoalescing setting to a
       default value
- pal: [GFX6-10] Increase storage for debug only path AutoBuffer
- pal: [GFX9/10] Remove device pointer member from MetaDataAddrEquation
- pal: Bump version number to 225
- llpc: Add a helper to get entry-point name from SPIR-V binary.
- llpc: Set EntryTarget to empty string ("") for AMDLLPC. Thus, we could
        check if the EntryTarget is specified and make follow-up decision.
- llpc: Add IR builder to NGG primitive shader class. Use IR builder to
        generate LLVM IR.
- llpc: Support dynamic index in interpolate functions
- llpc: Add LLPC support of VK_KHR_shader_clock
- llpc: Implement VK_extension_string support
- llpc: Set register SPI_SHADER_PGM_LO_GS to NggCullingData. This is
        required by PAL
- llpc: Remove PipelineOptions::autoLayoutDesc, also bump LLPC interface
        version to 30
- llpc: Add some spirv1.4 shaderdb test

* Mon Jul 15 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.98.0.20190715.gite835c3b

- xgl: Add Navi10 support
- xgl: Enable shader writes for alphaToCoverageEnable when attachment is
       set to VK_ATTACHMENT_UNUSED
- xgl: Change reported driver UUID from pal major/minor version (and
       timestamp on Linux) to AMD-LINUX-DRV
- pal: Add Navi10 support
- pal: Indirect function support in ILP.
- pal: Clear ops issued against external d/ds/s images trigger assertion
       failures in PAL, followed by test failures
- pal: Remove unneeded device pointer from DepthStencilState
- pal: Pass timeline flag to palQueueSemaphore when import new one.
- pal: Add support of LLVM IR section (.AMDGPU.comment.llvmir)   in PAL
       ABI processor
- pal: Bump version number to 222
- llpc: Add Navi10 support
- llpc: Add support for OpCopyLogical. glslang will generate it if 1_4
        environment is specified
- llpc: Enable 1_4 environment in SPVGEN
- llpc: GPU workaround useOriginalVgtGsOnchipCntl

* Tue Jul 02 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.97.0.20190630.git474c74e

- xgl: Add HDR10 support for direct display mode, enable EXT_HDR_METADATA
- xgl: Expose VK_EXT_display_surface_counter by default
- xgl: Disable attachment image memory type
- xgl: Hook up Vulkan panel setting to PAL public key
       enableGpuEventMultiSlot
- xgl: Implement GetPhysicalDevicePresentRectangles to fix a CTS test
       dEQP-VK.wsi.*.surface.query_devgroup_present_modes
- xgl: Remove unused IL internal shaders
- xgl: Always write the timestamp query availability value if it was
       requested at result copy time
- xgl: Fix MGPU app crashes when disable panel setting
       useSharedCmdAllocator
- xgl: Handle vkGetEventStatus success return codes better
- xgl: Enable scratch bounds checking as target feature
- xgl: Update PAL Interface in Vulkan to 516
- pal: Resolve asserts in VK CTS
       VK.memory.pipeline_barrier.transfer_dst_storage*)
- pal: Improve the way PAL handles HiStencil
- pal: Split barrier performance
- pal: Pipeline upload changes
- pal: Settings JSON and auto-gen script QoL improvements
- pal: Add maxFrameAverageLightLevel
- pal: Restrict the drmSyncobjTransfer ioctl check
- pal: Fix an access violation when destroying Image objects
- pal: Fix an issue that the data written into the buffer is corrupt when
       a copy is done from a render target to a buffer using
       CopyTextureRegion and the render target is dcc compressed
- pal: Handle Pipelines with Zero PS Interpolants
- pal: Modify the settings script to eliminate some of the newline
       characters
- pal: Linux implementation of Util::HashContext
- pal: Linux Implentation of Util::ArchiveFile
- pal: HDR10 support
- pal: Add a Util class for Loading DLL's & Shared Objects
- pal: Implement acquire-release on DMA queues
- pal: Add a debug option to make command stream memory read-only
- pal: Fix reserved bit count to keep flags as uint32
- pal: Fix reading wrong slice from mip 1 when a 2d array of 9 slices, 2
       mips is viewed as cubemap
- pal: Removal of IL_OP_DCL_UAV in pal
- pal: Interface change move AllocGranularity size/alignment from clients
       -> PAL
- pal: Bump version number to 220

* Thu Jun 06 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.93.0.20190606.git245f34b

- xgl: Enable Scratch Bounds Checking for GFX9 to fix F1 2018 hang issue
- xgl: Update SDK headers to 1.1.109
- xgl: Update PAL Interface in Vulkan to 502
- xgl: VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD: add support for the
       attachment image Vulkan memory type, which is very similar to the
       default local/invisible memory type
- pal: Make CPDMA query slot reset bypass L2 to avoid reading stale data
       at ComputeResults time
- pal: [GFX9] Trivial removal of unneeded DepthStencilState field
- pal: [GFX6-8] Port rework PA_SC_GENERIC/SCREEN_SCISSOR writes
- pal: Fix the override of SPI_CONFIG_CNTL
- pal: Disable pipeline upload to local invis mem for null devices
- pal: Update pipeline generation script to keep ifdefs in a consistent
       order
- pal: Implement HDR10 support
- pal: Add option to zero srd in unbound descriptor table
- pal: Transition to COPY_SOURCE does not decompress for copy to buffer
- pal: Fix hangs in layers surrounding acq-rel barriers
- pal: Fix acquire-release hanq on SE4
- pal: Optimizations for Acq-Rel
- pal: Implement blt optimizations for acquire-release barrier
- pal: [RPM] Minor tweak to ResolveImageGraphics path.
- pal: Add PipelineStageAllStages field in PipelineStageFlag enum
- pal: Remove reference to IL_REGTYPE_SHADER_RATE
- pal: Remove more redundant wait_reg_mem's in release-acquire
- pal: Fix generation of size_t for use with settingsTool and RDP
- pal: Deprecate ShaderCacheMode in PAL since it is no longer useful
- pal: Rename Linux OS Back-end to "Amdgpu"
- pal: Integrate latest Developer Driver Library
- llpc: Remove cwpack in LLPC,  use llvm::msgpack::Document to decode PAL
        metadata
- llpc: Add option lower-dyn-index back to fix build error
- llpc: Fix gfx9+ breakage from "Merge user data nodes"
- llpc: Fix divergent load bug and remove waterfalls

* Mon May 27 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.91-0.20190524.git8d085a7

- xgl: Enable VK_EXT_host_query_reset extension
- xgl: Enable VK_EXT_separate_stencil_usage  extension
- xgl: Enable VK_KHR_uniform_buffer_standard_layout extension
- xgl: Fix VK.renderpass*.suballocation.multisample.
       separate_stencil_usage.*.testing_stencil failure
- xgl: Use internal pipeline hash for Vulkan pipeline reinjection
- xgl: Add enableSPP option to Vulkan Panel
- xgl: Fix VkExample DepthStencilResolve test failure
- xgl: Add Macro define for XCB_SURFACE and XLIB_SURFACE extension
- xgl: Change if-statement to for loop for processing pNext structure in
       GetImageFormatProperties2
- xgl: Add XGL_BUILD_LIT option for lit test build
- xgl: Update PAL Interface in Vulkan to 501
- xgl: Remove Vulkan 1.0 build
- xgl: Fix small surf size disable compression setting
- pal: Remove ETC2 support from GFXIP 8.1
- pal: Fix a bug where the last shader wouldn't get a "#endif" if its
       defines were different from the second-to-last shader's defines
- pal: Minor modification in generate settings code script to support
       Vulkan Settings Refactor
- pal: [RPM] More accurately detect FMask in CopyImageCompute
- pal: Support UAV exports
- pal: Enable cu soft group for VS by default in gfx9
- pal: Late alloc GS limit clamp
- pal: Makes the perf data buffer independent of the pipeline binary so
       that accessing the perf data is easier irrespective of the
       resident heap type of the pipeline binary
- pal: Only restore Predication state once during GenericColorBlit
- pal: Fix segfault in interfacelogger
- pal: IGpuEvent objects do not need multiple slots when acquire\release
       barriers are not active
- pal: [GFX9]Update CB_DCC_CONTROL programming
- pal: Make GfxCmdBufState a structure, not a union.
- pal: Combine CE RAM Dump with Increment CE Counter
- pal: Change cas.h/a.h include paths in rpmUtil to be rooted at src
- pal: Fix hang with split-mode barriers and layers enabled
- pal: Upload pipelines to local invis mem
- pal: TA_GRAD_ADJ needs to be updated based on queue priority
- pal: Report correct memory bandwidth for GDDR6 parts
- pal: [GFX9] Rework PA_SC_GENERIC/SCREEN_SCISSOR writes
- pal: [GFX9] Filter redundant target scissor writes in BindTargets
- pal: Bump version number to 218
- llpc: Fix DiRT Rally 2.0  hang in ultra settings
- llpc: Support merge ELF binary for per stage cache and enable
        per-stage-shader cache
- llpc: Add support for MsgPack PAL metadata
- llpc: Fix lit test errors that are hidden by typo "SHADERTEST :"
- llpc: Implement memset/memcpy for buffer fat pointers using loops
- llpc: If cmpxchg is strong, need to set the cmp bit

* Sat May 11 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.85-0.20190511.git1dd300a

- xgl: Update PAL Interface in Vulkan to 489
- xgl: Update Vulkan header to 1.1.106
- xgl: Add entry vkCmdDrawIndirectCountKHR and
       vkCmdDrawIndexedIndirectCountKHR to sqtt layer to solve RGP crash issue
- xgl: Add support for subgroup cluster instruction
- xgl: Add setting to elevate priority of descriptor memory. Keep
       descriptors from getting paged if localHeap is oversubscribed
- xgl: Adds support for starting a  RGP trace based on a given frame
       index (so that detailed trace data is available for that frame)
- xgl: Implement extension VK_EXT_separate_stencil_usage,
       AMD_DEVICE_COHERENT_MEMORY and EXT_BUFFER_DEVICE_ADDRESS
- xgl: Make sure that MSAA depth/stencil images are treated as such by
       PAL
- xgl: Update the availability state for transform feedback query
- xgl: Change shader log file dumping directory/filename to:
       AMD_DEBUG_DIR+PipelineDumpDir+LogFileName<compileType>.txt
- xgl: Enable disk cache for Dawn of War3
- xgl: Performance tuning for game Thrones of Britannia
- xgl: Fix wrong usage of pImmutableSamplers
- pal: [GFX9]Trivial Draw function clean up
- pal: Update the availability state even if the query is not ready
- pal: Add option to use GpuHeapGartUswc for the pipeline uploader.
- pal: Set availability state for the result of streamout query
- pal: Changes to offline pipeline code gen script for more aggressive
       duplicate detection, minor bug fix
- pal: Indirect function support fixes
- pal: Remove "wholePipelineOptimizations" from the settings.
- pal: Fix PAL_ASSERT(pProps->gfx6.numMcdTiles <= MaxMcdTiles) is
       triggered with debug driver
- pal: Add option to force 64k padding for big page testing
- pal: Change activeCuMask to CUs on all HW
- pal: Add IL_OP_GET_ELEMENT_POINTER in ilp
- pal: Add support flag for out of order primitives and removed
       unnecessary variable
- pal: Add format overriding for scaled copy
- pal: Need precheck for bounded GPU memory's existence
- pal: Supply the image pointer associated with the mask-rams in the
       constructor so that the image and device objects don't have to get
       passed around everywhere
- pal: [AcqRelBarrier] GpuEventPool refactor to better meet PAL client
       needs
- pal: Adjust the amount of parameter cache we allow for a single binning
       batch
- pal: Remove unnecessary CpDma sync for Htile equation upload
- pal: Use "HasEntry" to load the compute user accumlator registers
       instead of "A
- pal: Bump version number to 215
- llpc: Update shaderdb tests
- llpc: Refine LLPC hash code
- llpc: Refine the lock time in pipeline dump
- llpc: Optimize pipeline compile time
- llpc: Optimize the buffer merge load/store functions for the tess shage
- llpc: Rework buffers to support fat pointers

* Mon Apr 22 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.85-0.20190421.git1dd300a

- xgl: Fix MGPU: vkCmdNextSubpass and vkCmdEndRenderPass incorrectly use
       the currently set device mask
- xgl: Fix VK_KHR_device_group issue that "set" event status triggered by
       vkCmdSetEvents() executed by multi-GPU devices is not seen on host
       end
- pal: Update block instance counts (GL2A and GL2C)
- pal: Minor SPM logging enhancements
- pal: Correct copy_data alignment assert logic
- pal: Fix interface 478: relax compression in srds in the new interface
       from “enable only if we know the image is compressed” to “enable
       unless we write”
- pal: Add global Src/Dst cache masks to BarrierInfo
- pal: Tidy up ISettingsLoader's use of IndirectAllocator
- pal: Allow shared memory to be CPU visible
- pal: Reset query pool from CPU
- pal: Tweaks to PA_SC_SHADER_CONTROL draw-time code
- pal: Integrate latest addrlib
- pal: Update ELF Target Machine Numbers
- pal: Add a pal key to control the cmd buffer token size with 32 bit
       build when Gpu profiler mode is enabled
- pal: Fix GpaSession has intemittent zero-duration timestamps
- pal: Refactor wavefront size reporting and selection to make it easier
       to use wave intrinsics
- pal: Fix CPU mapping problem for memory shared cross device
- pal: Fix Thrones of Britannia tearing regression
- pal: Bump version number to 211
- llpc: Move shaderdb test from xgl to llpc repository
- llpc: Add support for dumping AMDIL binaries through the LLPC
        PipelineDumper with new interface version 25
- llpc: lit test fixes for llvm upgrade

* Thu Apr 11 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.84-0.20190411.gitb21105a

- xgl: Fix Just Cause3 flicker issue: skip the store instruction when the
       index is out-of-bound if feature robustBufferAccess is used,
       relying on LLPC interface version 23
- xgl: Simplify the implementation of ShaderReplaceShaderISA
- xgl: PipelineCompiler refactoring
- xgl: Add support for AMDIL to VK_AMD_shader_info, relying on LLPC
       interface version 25
- xgl: Add shader optimizer JSON options for enableSelectiveInline and
       disableloopunrolls
- xgl: Implement VK_EXT_host_query_reset
- xgl: Update Vulkan headers to 1.1.105
- xgl: Update PAL Interface in Vulkan to 481
- xgl: Update LLPC Interface in Vulkan to 24
- pal: Update block instance counts (GL2A and GL2C)
- pal: Minor SPM logging enhancements
- pal: Correct copy_data alignment assert logic
- pal: Fix interface 478: relax compression in srds in the new interface
       from “enable only if we know the image is compressed” to “enable
       unless we write”
- pal: Add global Src/Dst cache masks to BarrierInfo
- pal: Tidy up ISettingsLoader's use of IndirectAllocator
- pal: Allow shared memory to be CPU visible
- pal: Reset query pool from CPU
- pal: Tweaks to PA_SC_SHADER_CONTROL draw-time code
- llpc: Move shaderdb test from xgl to llpc repository
- llpc: Add support for dumping AMDIL binaries through the LLPC
        PipelineDumper with new interface version 25

* Fri Mar 29 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.82-0.20190329.git3160bb6

- xgl: Update shaderdb OpImageSample_TestSeparateSampler_lit.frag test
- xgl: Fix issue for capturing detailed tracing on a per PSO basis
- xgl: Enable priority regardless of whether VK_EXT_memory_priority is
       enabled or not for all external queues, relying on PAL interface
       version 479
- xgl: Disable TC compatible reads for MSAA depth-stencil target for
       Thrones of Britannia, relying on PAL interface version 481
- xgl: Add per shader optimizations to disable loop unroll  for
       Total:WarhammerII, relying on LLPC interface version 24
- xgl: Update PAL Interface in Vulkan to 475
- pal: Replace the existing "noMetadata" image-create flag with an enum
       that adds an option to disable TC compatibility
- pal: GpuEvent: fix bug related to heap type count
- pal: Fix null buffer views
- pal: Change the late alloc scheme to limit the amount of late alloc to
       a specific amount of space in the Position Buffer based on CU/SA
- pal: Remove L2 Cache flushes from indirect command generation for gfx9
- pal: Fix crash in GpaSession
- pal: Set GpaSession's default SQTT size to 128MB, clamped to whatever
       the max reported by PAL is
- pal: Maximize concurrency accessing Pipeline ELF cache
- pal: Clean up some additional L2 Flush and Invalidate related things in
       gfx9Barrier.cpp
- llpc: Factored out new base class ConfigBuilderBase
- llpc: Set PAL metadata pseudo-registers in ConfigBuilderBase
- llpc: Add support when image resource are selected from control flow

* Tue Mar 26 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.81-0.20190326.git3160bb6

- xgl: Enable VK_EXT_memory_priority extension
- xgl: Enable VK_EXT_memory_budget extension
- xgl: Set dccBitsPerPixelThreshold to 16 for Vega20
- xgl: Update PAL Interface in Vulkan to 473
- xgl: PipelineCompiler refactor: separate Llpc part
- xgl: Convert VkPipelineLayout to support an arbitrary number of
       descriptor sets
- xgl: Add replace isa shader function in the pipeline
- xgl: Add offset number before shader output text
- xgl: Add per-shader stage wave size settings
- xgl: Use the correct heap index to determine if the heap is
       multi-instance
- xgl: Fix nullptr deref while walking over
       VkPhysicalDeviceSurfaceInfo2KHR chain
- pal: CmdUtil Enhancements, mostly changes to BuildWriteDat
- pal: Link gpu memory priority system to os on linux
- pal: Add the extended SPM segment size registers to the non-shadowed
       lists
- pal: [GFX9] Minor fix and opt for draw-time conservative rast register
- pal: [GFX9] Trivial removal of unneeded BlendState field
- pal: [GFX6-9] Trivial removal of unneeded code related to MSAA
       SamplePos
- pal: Modify release mem path to explicitly read and write through L2
- pal: Refactor of various code related to GPU page sizes > 4KiB
- pal: Change ApiInfo chunk version bump to be a minor version change
       instead of a major one
- pal: Return the default color gfx layout for multi-media surfaces
- pal: Fix wrong ICmdBuffer pointer passed through developer callbacks
       when GpuProfiler layer is enabled
- pal: PAL IPerfExperiment implementation refactoring
- pal: Fix a bug in ApiPsoHash support
- pal: Fix a dead loop in converting a FP16 denorm back to normalized
       FP32
- pal: Fix memory leak in GpaSession
- pal: [CmdBufferLogger] Fixes for the timestamp/waitIdle features
- pal: [AcqRelBarrier] Bug fixes and clean-ups
- pal: Retire PAL interfaces up to 443

* Fri Mar 22 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.79-0.20190318.git735d204

- xgl: Add test result check in shaderdb test using lit
- xgl: Fix abnormal timestamp on transfer queue
- xgl: Do not stop instruction tracing at pipeline unbind since it may
       cut the trace short
- xgl: Enable PAL skip fast clear eliminate optimization by default
- xgl: Fix noisy assert by moving it after extensions are populated in
       late physical device init
- pal: Use the peerWritable flag when creating presentable images: this
       fixes a few assertions that fire when rendering using a swapchain
       with a device group (MGPU) in Vulkan
- pal: Remove palRuntimeHash and add ApiPsoHash to CmdBindPipeline
- pal: Reduce unnecessary L2 cache actions on GFX9
- pal: Gfx9 SPM changes
- pal: Fix ShaderDbg bugs
- pal: Update pipeline ABI metadata note ID to 32 (from 13) to match HSA
       code objects
- pal: Add compute queue support for pausing perf experiments and
       CmdUpdateSqttTokenMask
- pal: Improve CPU-Bound Performance in Mad Max: make the internal
       timestamp memory allocated using GpuScratch; makes internal GPU
       event objects able to use the BindGpuMemory to avoid the internal
       memory manager for the internal release/acquire event and instead
       uses GpuScratch
- pal: [GFX7/8] Default IndexBuffer fetchs to STREAM cache policy instead
       of LRU
- pal: Use the proper CP path for all non-user-mode config registers on
       gfx9
- pal: Change srd creation to handle (un)compressed writes
- pal: Minor profiling validation and memory leak fixes
- pal: Resolve hang sending dummy LOAD_CONST_RAM packet

* Fri Mar 15 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.78-0.20190315.git735d204

- xgl: Implement and enable VK_KHR_vulkan_memory_model extension
- xgl: Implement and enable VK_EXT_depth_clip_enable extension
- xgl: Implement and enable VK_KHR_depth_stencil_resolve extension
- xgl: Enable VK_KHR_shader_float16_int8 extension by default
- xgl: Enable VK_EXT_debug_utils extension extension by default
- xgl: Enable VK_EXT_transform_feedback extension by default
- xgl: Implement VK_EXT_memory_budget extension (not finished)
- xgl: Don't count preserve attachments as first use
- xgl: PipelineCompiler refactor: separate CompilerSolution into isolated
       files
- xgl: Add support for  BindPipeline marker
- xgl: Start/Stop instruction trace based on ApiPsoHash
- xgl: Set apiPsoHash for binding of internal and NULL XGL pipelines to
       Pal::InternalApiPsoHash
- xgl: Move memory usage tracking from Device to PhysicalDevice.
- xgl: Set semaphore use in device group to be shareable
- pal: Add new Developer Callback BindPipeline for support to generate
       instrumentation describing the Pipeline bind event
- pal: Choose fixed function resolve pipeline based on resolve format
       instead of surface format
- pal: Fix dEQP-VK.spirv_assembly.instruction.graphics.float16.derivative_*
       - tests fail on gfx9
- pal: Minor fixes relevant to adding Developer Callback CmdBindPipeline
- pal: Support Vulkan driver implementation for VK_EXT_memory_budget
- pal: Indirect User-Data Clean-Up and Refactor, Part #3: mainly focused
       around PAL ABI changes for how the GPU virtual addresses for the
       vertex buffer and stream-out tables are mapped to user-SGPR's
- pal: Add ICmdBuffer::CmdSetVertexBuffers() to update the vertex buffer
       SRD table
- pal: Optimize the query pool slot reset operation in occlusion query's
       issue_begin which causes too many map/unmap of GPU memory
- pal: Add a "most" section to the generated register structs which helps
       prevent register definition fragmentation
- pal: Change IGpuEvent interface from IDestroyable to IGpuMemoryBindable
- pal: Convert a bunch of const CmdUtil methods to static
- pal: Supplement the judgment conditions of CB fixed function resolve
- pal: Add an optional path which can update the spill table, vertex
       buffer table and stream-out table using the CPU and embedded data
       instead of the existing CE RAM path
- pal: Edit the UseDcc setting to allow separate dcc control for
       resources that are used as a render target and a UAV and for
       resources that are only used as a UAV
- pal: Only execute DepthStencilCopy when resolve mode is average (i.e.
       sample_zero)
- pal: Fix shareable semaphore to stall queue
- llpc: Fix a bug in the LLPC ShaderCache Merge function which cause
        Dota2 stuttering and performance drop after recent game update
- llpc: Fall back to the internal shader cache for the case of
        VkPipelineCache miss
- llpc: Implement VK_KHR_shader_float_controls extension (not finished)
- llpc: Fix dynamic loop unroll crash
- llpc: Add LLVM library func tanf in emu lib to fix Rise of the Tomb
        Rider game crash with gcc 7 build
- llpc: Fix Witcher3-dxvk hang after loading screen

* Mon Mar 04 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.77-0.20190301.gitc59b998

- xgl: Add result check pattern in shaderdb test for llvm-lit test
- pal: Upgrade addrlib
- pal: Add supports for min and max stencil resolve using compute
       pipeline.
- pal: Add support for VK_EXT_calibrated_timestamps
- pal: Fix memory leak in CmdBufferLogger
- pal: Fix vkmark corruption observed on Fiji + wayland
- pal: Fix perf counter max event id for CPG block
- llpc: Support .raw.buffer and .struct.buffer
- llpc: Resolve swizzling of LLPC API shader hash by removing call to
        MetroHash::Compact64()
- llpc: [TransformFeedback] Fix the register setting for
        RasterizationStreamSelect capablitity

* Tue Feb 26 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.76-0.20190225.git27ef34e

- xgl: Implement VK_EXT_memory_priority support
- xgl: Add transfer queue workaround for Gfx6-8 to avoid PRT issues with
       SDMA
- xgl: Add barrier performance debug settings
- xgl: Implement an API PSO hash for Vulkan that is consistent from run
       to run and unique to the state of the PSO. This hash is registered
       with the dev driver profiling GpaSession to be written into .rgp
       files
- pal: Remove unnecessary assert in CmdDrawOpaque()
- pal: Add SupportsUnmappedPrtPageAccess flag to
       DeviceProperties::engineProperties::flags.
- pal: Fix corruption when enhanced sync enabled with Vsync on
- pal: Indirect User-Data Clean-Up and Refactor, Part #1: reduces the
       number of indirect user-data tables offered by PAL to one
- pal: Indirect User-Data Clean-Up and Refactor, Part #2: makes the
       internal changes in PAL necessary to start treating indirect
       user-data tables as what they really are used for by clients: the
       vertex buffer table
- pal: [RGP]Add functionality to enable instruction-level trace
       per-pipeline
- pal: Make sure that waitOnMetadataMipTail and
       depthStencilNeedsEopFlushTcc are both false in the CmdBindTargets
       function to avoid unnecessary cache flushes
- pal: Add multi-wave copy option for HS
- pal: Resolve Vulkan CTS OOM test case crashes, and a wide range of many
       other potential PAL_NEW alloc failure crashes
- pal: Delete queuesUseCaches flag
- pal: Update RGP API_INFORMATION chunk to reflect latest spec changes to
       include profile mode information
- pal: Update settings generation to calculate and populate the
       settingsDataHash field for each component
- pal: Add debug support to the CmdBufferLogger layer that allows for
       "single-stepping" of draws/dispatches
- pal: Don't reset GpuEvents on the CPU
- pal: Add settings to control the number of parameter cache lines for
       GE_PC_ALLOC and to control the number of cache lines for
       SPI_SHADER_LATE_ALLOC_VS
- pal: Improve AllocateGpuScratchMem function flexibility, prepare for
       changing IGpuEvent to IGpuMemoryBindable interface
- llpc: Fix the broken path of offchip GS
- llpc: Change TFE mechanism to use up-streamed support
- llpc: Change the builder interface to be more forward-looking & efficient
- llpc:  Move fmask and subpass data handling into lowering
- llpc: Remove ICmpInst from StoreValueToStreamOutBuffer
- llpc: Fix transformfeedback multi-stream cts on gfxip 8 and gfxip 9.
        Now transformfeedback cts erros are cleared
- llpc: New fix for CTS v1.1.2.2 hang in ./deqp-vk -n
        dEQP-VK.binding_model.descriptorset_random.sets32.noarray.ubolimitlow
- llpc: Add LLPC support for VK_KHR_shader_clock
- llpc: Moved auto-layout-desc code into amdllpc
- llpc: Introduce a new Builder::CreateWaterfallLoop method to create
        waterfall loop code for a buffer/image op with a non-uniform
	descriptor
- llpc: Separate descriptor load out of buffer op
- llpc: Add assert that lib func has the right type

* Fri Feb 01 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.73-0.20190201.git20a62e8

- xgl: Update Vulkan Headers to 1.1.97
- xgl: Enable the extensions under development (VK_EXT_DEBUG_UTILS,
       VK_KHR_SHADER_FLOAT16_INT8,VK_ EXT_TRANSFORM_FEEDBACK) through the
       environment variable AMDVLK_ENABLE_DEVELOPING_EXT
- xgl: Implement VK_KHR_shader_float16_int8 extension
- xgl: Fix a memory priority issue: MemoryPriority shall select priority
       instead of offset as the high 16bit
- xgl: Refine the code to distinguish between
       VkGraphicsPipelineCreateInfo and
       GraphicsPipeline::CreateInfo/ComputePipeline::CreateInfo.
- xgl: Use the correct features pointer when VkPhysicalDeviceFeatures2 is
       used during device creation
- xgl: Implement SQTT support for the marker/label functionality of
       VK_EXT_debug_utils
- xgl: [shadertest] amdllpc lit test changes for per-shader lowering
- pal: Upgrade the VAM component
- pal: Add proper handling of allocation failures
- pal: Fix up some of the support for ECC GPR protection on Vega20
- pal: Fix GFX7: vkCmdDispatchIndirect() does not work correctly when
       submitted to a compute queue
- pal: Add support for GPU un-cached memory allocation
- pal: Add IL opcodes for some Dot ops
- pal: Fix regressions caused by CPU clock support in RGP
- llpc: Default to -enable-shadow-desc
- llpc: Remove address-space mutation passes
- llpc: Add proper handling of allocation failures
- llpc: Initial definition of Builder interface
- llpc: Increase max line to 65536. because we may have very long
        comments in .pipe file
- llpc: Fix the so-called "native" emu lib functions with allocas to use
        the right datalayout and put their allocas into the right address
        space
- llpc: Fix transformfeedback stride calculation in the output shader
        block
- llpc: Revert previous changes for lowering passes to per-shader
- llpc: Added timing of LLPC phases to -time-passes

* Wed Jan 30 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.72-0.20190130.gitfbfa56c

- amdvlk: Add Vega20 and Raven2 support
- xgl: Implement VK_EXT_transform_feedback
- xgl: Move VK_EXT_swapchain_colorspace to instance extension
- xgl: Add int8 shaderdb tests
- pal: Report CPU clock speed to RGP
- pal: Properly reset events in EventPool and CmdReleaseThenAcquire
- pal: Fix bugs in Release/acquire-based barrier
- pal: Fix a typo in parsing /proc/cpuinfo output
- pal: Add a L2 flush and invalidate before copying leftover
       block-compressed pixels (Gfx9)
- pal: Add a flag in DeviceProperties to indicate whether the engine
       supports trackBusyChunks
- pal: Fix top pipelines identified by timeReport.py is mismatched with
       the dumped pipelines
- llpc: Implement VK_KHR_vulkan_memory_model
- llpc: Add arithmetic support for int8
- llpc: Use explicit waterfall intrinsics for subgroupshuffle
- llpc: Add xfblocation support for the Transformfeedback
- llpc: Fix assert in switch emu lib to an archive of bitcode modules
- llpc: gsPrimsPerSubgroup shouldn't be bigger than wave size

* Sun Jan 27 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.71-0.20190125.git96f3ad7

- xgl: Enable EXT_INLINE_UNIFORM_BLOCK extension
- xgl: Enable EXT_PCI_BUS_INFO extension
- xgl: Add barrier filtering
- xgl: Implement extension VK_KHR_vulkan_memory_model in vulkan api layer
- xgl: Implement VK_EXT_display_surface_counter support
- xgl: Fix asserts related to valid vkCmdPushConstants usage
- pal: Fix wrong reported LDS size per threadgroup for GFX7+
- pal: Add new flag 'notLockable' into GpuMemoryCreateFlags to indicate
       the GpuMemory will be indirect lock
- pal: Upgrade gpuopen
- llpc: Remove unnecessary assert in amdllpc
- llpc: Fix CTS v1.1.2.2 failure in ./deqp-vk -n
        dEQP-VK.binding_model.descriptorset_random.sets32.noarray.ubolimitlow
- llpc: Enable inclusion of llvm-ir in section of ELF output
- llpc: Expand the shader inout meta node from 64 bit to 64 bit array

* Tue Jan 15 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.70-0.20190115.git45222f8

- amdvlk: Update Vulkan Headers to 1.1.96
- amdvlk: Add pipeline optimizer key to pipeline dump file
- amdvlk: Optimization for fully overwritten resolve
- amdvlk: Add atomicOp support for the variable pointer
- amdvlk: Fix A performance regression with the Talos Principle
- amdvlk: Fix A potential access violation
- amdvlk: Fix A RGP regression
- amdvlk: Fix Multi-process failure
- xgl: Expose YUV planes, allow applications to implement their own color
       conversion accessing each YUV planes
- xgl: Do not include symbols while building release driver
- xgl: Code refactoring for pipeline dump
- xgl: Fix random VM fault caused by that the image descriptor and the
       fmask descriptor contain the same lower virtual address (as
       designed) but use different offsets in the suballocation
- xgl: Change the default WgpMode from wgp to cu
- xgl: Fix a null pointer access violation
- xgl: Implement VK_EXT_debug_utils
- xgl: Fix dxvk ELEX  corruption issue
- pal: Expose CuMask to gpaSession clients
- pal: Fix a  performance regression introduced by changes which added
       support for the LOAD_INDEX path for handling pipeline binds
- pal: Revise the alert of doing expand in late phase to print more info
- pal: Use mmTA_GRAD_ADJ_UCONFIG on GFX9 to prevent writing to a
       privileged register
- pal: Enable Int8 Arithmetic op in PAL ILP
- pal: Update ELF strtab section name offset when loading an ELF binary
- pal: Fix QuerySystemInfo() implementation for a number of issues
       affecting many-core CPUs like Threadripper and Epyc
- pal: Add a new declaration for the name prefix of ELF section dedicated
       to storing comments such as compiler intermediate representation
       (e.g. LLVM IR)
- llpc: Update naming scheme of LLVM IR inclusion:
- llpc: Add pipeline option includeIr for including IR in the ELF section
        in AMD_SHADER_INFO
- llpc: Fix  float test failure for transform_feedback

* Mon Jan 07 2019 Tomas Kovar <tkov_fedoraproject.org> - 2.68-0.20190107.git094be24

- xgl: Update Vulkan Headers to 1.1.96
- xgl: Add GPU memory references to SW compositing images
- xgl: Switch the default error code in PalToVkError from
       VK_ERROR_INTIALIZATION_FAILED to VK_ERROR_OUT_OF_HOST_MEMORY
- xgl: Fix a potential access violation if pPalMemory is nullptr
- xgl: Barrier cleanup
- xgl: Remove code for PAL_CLIENT_INTERFACE_MAJOR_VERSION <= 450
- xgl: Add new shaderdb test cases for transform feedback and variable
       pointer
- pal: Fix format X10Y10Z10W2Bias_Unorm is missed in Image::GetAddrFormat
- pal: Move the dccBitsPerPixelThreshold setting from a private Gfx9
       setting to a public Pal setting that can be set by clients.
       Refactor the code to use the public PAL setting when checking for
       the threshold to determine if DCC should be turned off
- pal: Avoid redundant pixel copy for BCn format
- pal: [RGP] Switch 64-bit pipeline compiler hashes to 128-bit internal
       pipeline hashes. Add PSO Correlation RGP chunk, update Code Object
       Database and Loader Event RGP chunks
- pal: Don't allow any meta-data texture fetches through that surface's
       hTile for the stencil if the hTile surface for a depth / stencil
       buffer doesn't contain any stencil data
- pal: Fix an RGP regression in the gpasession back-compat code
- pal: Pad shader size with shader instruction prefetch cache lines
- pal: Add new TossPoint for killing primitives in the PA during setup
- pal: Fix improper order of string for the enum EngineType
- pal: Fix the issue that pipelineAbiProcessor::LoadFromBuffer then
       PipelineAbiProcessor::SaveToBuffer ends up with different ELF size
- pal: Optimization for fully overwritten resolve
- pal: Make client specific debug string in public settings work
- pal: Fix Multi-process failure
- llpc: Rationalize LLPC's various ad-hoc pass managers into a single
        pass manager that runs on a single whole-pipeline LLVM IR module
- llpc: Move LLPC pass initialization so that a pass name can be used in
        an option such as -print-after, or the forthcoming
	-llpc-stop-after
- llpc: Add -dump-cfg-after=<passname> to dump CFG to a file per function
        after the specified pass
- llpc: Add additional flags to keep floating point optimization after
        limited opt pass
- llpc: Add pipeline optimizer key to pipeline dump file
- llpc: Use DEBUG_TYPE in all passes' INITIALIZE_PASS
- llpc: Use global Create function for all passes
- llpc: Include llvm-ir in ELF section
- llpc: Remove IR Value pointers from pipeline state
- llpc: Add 16-bit and 64-bit data to transform feedback.
- llpc: Correct the behavior of XFB enablement. In glslang, xfb_offset
        will trigger XFB rather than other XFB decorations.
- llpc: Remove glslCopyShaderEmu.ll. Add the function to
        llpcPatchCopyShader.cpp. Generate expected IR by C++.
- llpc: Fix dynamic loop unroll GetPipelineStatistics which was broken in
        PR#16
- llpc: Fix failure for clspv shader using atomic increment, add atomicOp
        support for the variable pointer
- llpc: Fix unused variable error on clang
- llpc: Fix asin float 16 CTS errors

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

* Mon Apr 02 2018 Tomas Kovar <tkov_fedoraproject.org> - 2.23-0.20180402.gitae72750

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
