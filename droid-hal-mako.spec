# These and other macros are documented in dhd/droid-hal-device.inc

%define device mako
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 4

%define installable_zip 1

%define enable_kernel_update 1

%define use_generic_obexd_configs 1
%define use_generic_bluez4_configs 1

%include rpm/dhd/droid-hal-device.inc
