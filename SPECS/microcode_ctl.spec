%global package_srccommit bbba30dd5237561a3f4fc5f16a69b9dd113320f8

%define debug_package %{nil}

%define base_dir %{name}-%{version}-%{release}

Summary:        Tool to transform and deploy CPU microcode update for x86.
Name:           microcode_ctl
Version:        2.1
Release:        26.xs22
Epoch:          2
Group:          System Environment/Base
License:        Redistributable, no modification permitted
URL:            https://pagure.io/microcode_ctl

Source0: https://code.citrite.net/rest/archive/latest/projects/XSC/repos/intel-nda-ucode/archive?at=bbba30dd5237561a3f4fc5f16a69b9dd113320f8&prefix=microcode_ctl-2.1-26.xs22&format=tar.gz#/microcode_ctl-2.1-26.xs22.tar.gz
Source1: SOURCES/microcode_ctl/01-microcode.conf



Buildroot:      %{_tmppath}/%{name}-%{version}-root
ExclusiveArch:  %{ix86} x86_64
BuildRequires:  kernel-devel

%description
The microcode_ctl utility is a companion to the microcode driver written
by Tigran Aivazian <tigran@aivazian.fsnet.co.uk>.

The microcode update is volatile and needs to be uploaded on each system
boot i.e. it doesn't reflash your cpu permanently, reboot and it reverts
back to the old microcode.

%prep
%setup -q -n %{base_dir}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/lib/firmware/intel-ucode
install -m 644 intel-ucode/* intel-ucode-with-caveats/* %{buildroot}/lib/firmware/intel-ucode

mkdir -p  %{buildroot}/usr/share/doc/microcode_ctl/
install -m 644 *.md %{buildroot}/usr/share/doc/microcode_ctl/
install -m 644 license %{buildroot}/usr/share/doc/microcode_ctl/

mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/dracut/dracut.conf.d

%post
%{regenerate_initrd_post}

%postun
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%clean
rm -rf %{buildroot}

%files
/lib/firmware/*
%config(noreplace) /usr/lib/dracut/dracut.conf.d/01-microcode.conf
%doc /usr/share/doc/microcode_ctl/*


%changelog
* Thu Jul 21 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 2.1.26-xs22
- Update to IPU 2022.2 release.

* Thu May 5 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 2.1.26-xs21
- Update to IPU 2022.1 release.

* Mon Feb 21 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 2.1.26-xs20
- Rework build system, build directly from Intel microcode repository.
- Import staging microcode-20220207 tag.

* Mon Feb 07 2022 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1.26-xs19
- Import staging microcode-20220204 tag
- Import staging microcode-20220131 tag
- Import staging microcode-20220126 tag
- Import staging microcode-20220121 tag

* Tue May 25 2021 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1.26-xs15
- Import staging microcode-20210521 tag
- Import staging microcode-20210430 tag

* Fri Oct 30 2020 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1.26-xs13
- Import new blobs from ucode-2020-11-10

* Wed Jun 03 2020 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1.26-xs12
- Import Skylake/Kabylake from ucode-2020-06-02-public-demo

* Fri May 29 2020 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs11
- Import Haswell/Broadwell from ucode-2020-05-11-public-demo
- Import public microcode-20200520 tag

* Wed Nov 20 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs10
- Include microcode-20191115 tag from the public Intel repo

* Wed Nov 06 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs9
- Add ucode for November

* Tue Nov 05 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs8
- Revert the latest SandyBridge ucode

* Thu Sep 19 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs7
- Include microcode-20190918 tag from the public Intel repo

* Fri Jun 28 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs6
- Include microcode-20190618 tag from Intel (includes SandyBridge ucode)

* Thu May 09 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs5
- Add more ucode for May

* Tue Apr 30 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs4
- Add more ucode for May

* Mon Apr 29 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs3
- Update to include a new microcode

* Fri Feb 08 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-26-xs2
- Update to intel Q4'18 microcode

* Mon Aug 13 2018 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1-26-xs1
- Update to upstream 2.1-19. 20180807 to take a Broadwell bundle
- Fix Makefile in the tarball to work with our version of tar

* Thu Aug 09 2018 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1-24-xs2
- Update to intel microcode 20180807

* Fri Aug 03 2018 Igor Druzhinin <igor.druzhinin@citrix.com> - 2.1-24-xs1
- Update to intel microcode 20180801
- Add Intel EULA

* Mon Jul 09 2018 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-24
- Update to upstream 2.1-18. 20180703

* Tue Mar 20 2018 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-22-xs1
- Update 06-4f-01 (Broadwell E) microcode to rev 0xb00002a, 2018-01-19, sig 0x000406f1

* Mon Mar 19 2018 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-22
- Update to upstream 2.1-16. 20180312
- Fedora SRPM link: https://rpmfind.net/linux/RPM/fedora/devel/rawhide/x86_64/m/microcode_ctl-2.1-22.fc29.x86_64.html

* Wed Jan 17 2018 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-20.xs2
- Revert microcode archive back to 2.1-14

* Wed Jan 10 2018 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-20.xs1
- Update to upstream 2.1-15. 20180108
- Backport of http://pkgs.fedoraproject.org/rpms/microcode_ctl/c/b6f8e6b7aa2d1bafee3136db0e543fd273a45100
- Microcode 06-4f-01 comes from 2.1-16.xs1 (2.1-14-bti1)

* Mon Aug 21 2017 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-16
- Update to intel microcode 20170707
- Backport of http://pkgs.fedoraproject.org/rpms/microcode_ctl/c/cd339e377a5a153cab28e81650f1ed96257d194e

* Thu Jun 22 2017 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-14.2
- Update to intel microcode 20170511
- Backport of http://pkgs.fedoraproject.org/cgit/rpms/microcode_ctl.git/commit/?h=f26&id=232fdf0223ebbb5b60e7dbdb4bb38d8b17423e80

* Tue Apr 25 2017 Sergey Dyasli <sergey.dyasli@citrix.com> - 2.1-13.1
- Update to intel microcode 20161104
- Backport of http://pkgs.fedoraproject.org/cgit/rpms/microcode_ctl.git/commit/?h=f26&id=7a4a2d14c56b8ac1a11abfe6ea2b3dc43e8a3b39

* Tue Jun 7 2016 Petr Oros <poros@redhat.com> - 2.1-12.1
- Run dracut -f for all kernels.
- Resolves: #1343614

* Fri Jul 3 2015 Petr Oros <poros@redhat.com> - 2.1-12
- Update to upstream 2.1-7. Intel CPU microcode update to 20150121.
- Resolves: #1174983

* Fri Oct 10 2014 Petr Oros <poros@redhat.com> - 2.1-11
- Run dracut -f after install microcode for update initramfs.
- Resolves: #1151192

* Tue Sep 30 2014 Petr Oros <poros@redhat.com> - 2.1-10
- Update to upstream 2.1-6. Intel CPU microcode update to 20140913.
- Resolves: #1142302

* Tue Jul 15 2014 Petr Oros <poros@redhat.com> - 2.1-9
- Update to upstream 2.1-5. Intel CPU microcode update to 20140624.
- Resolves: #1113396

* Tue Jun 3 2014 Petr Oros <poros@redhat.com> - 2.1-8
- Fix bogus time in changelog
- Resolves: #1085117

* Tue Jun 3 2014 Petr Oros <poros@redhat.com> - 2.1-8
- Update to upstream 2.1-4. Intel CPU microcode update to 20140430.
- Resolves: #1085117

* Wed Mar 12 2014 Anton Arapov <anton@redhat.com> - 2.1-7.1
- Fix the microcode's behaviour in virtual environment.

* Fri Feb 28 2014 Anton Arapov <anton@redhat.com> - 2.1-7
- Fix the microcode's dracut configuration file location. 

* Tue Feb 18 2014 Anton Arapov <anton@redhat.com> - 2.1-6
- Enable early microcode capabilities. Systemd and Dracut support. (Jeff Bastian)

* Fri Jan 24 2014 Anton Arapov <anton@redhat.com> - 2.1-5
- Update to upstream 2.1-3. Intel CPU microcode update to 20140122.

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2:2.1-4
- Mass rebuild 2013-12-27

* Mon Sep 09 2013 Anton Arapov <anton@redhat.com> 2.1-3
- Imported to RHEL tree

* Mon Sep 09 2013 Anton Arapov <anton@redhat.com> 2.1-2
- Update to upstream 2.1-2.

* Wed Aug 14 2013 Anton Arapov <anton@redhat.com> 2.1-1
- Update to upstream 2.1-1.

* Sat Jul 27 2013 Anton Arapov <anton@redhat.com> 2.1-0
- Update to upstream 2.1. AMD microcode has been removed, find it in linux-firmware.

* Wed Apr 03 2013 Anton Arapov <anton@redhat.com> 2.0-3.1
- Update to upstream 2.0-3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Anton Arapov <anton@redhat.com> 2.0-2
- Update to upstream 2.0-2

* Tue Oct 02 2012 Anton Arapov <anton@redhat.com> 2.0-1
- Update to upstream 2.0-1

* Mon Aug 06 2012 Anton Arapov <anton@redhat.com> 2.0
- Update to upstream 2.0

* Wed Jul 25 2012 Anton Arapov <anton@redhat.com> 1.18-1
- Update to upstream 1.18

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Anton Arapov <anton@redhat.com> 1.17-25
- Update to microcode-20120606.dat

* Tue Feb 07 2012 Anton Arapov <anton@redhat.com> 1.17-24
- Update to amd-ucode-2012-01-17.tar

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Anton Arapov <anton@redhat.com> 1.17-21
- Fix a segfault that may be triggered by very long parameter [#768803]

* Tue Dec 13 2011 Anton Arapov <anton@redhat.com> 1.17-20
- Update to microcode-20111110.dat

* Tue Sep 27 2011 Anton Arapov <anton@redhat.com> 1.17-19
- Update to microcode-20110915.dat

* Thu Aug 04 2011 Anton Arapov <anton@redhat.com> 1.17-18
- Ship splitted microcode for Intel CPUs [#690930]
- Include tool for splitting microcode for Intl CPUs (Kay Sievers )

* Thu Jun 30 2011 Anton Arapov <anton@redhat.com> 1.17-17
- Fix udev rules (Dave Jones ) [#690930]

* Thu May 12 2011 Anton Arapov <anton@redhat.com> 1.17-14
- Update to microcode-20110428.dat

* Thu Mar 24 2011 Anton Arapov <anton@redhat.com> 1.17-13
- fix memory leak.

* Mon Mar 07 2011 Anton Arapov <anton@redhat.com> 1.17-12
- Update to amd-ucode-2011-01-11.tar

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Anton Arapov <anton@redhat.com> 1.17-10
- manpage fix (John Bradshaw ) [#670879]

* Wed Jan 05 2011 Anton Arapov <anton@redhat.com> 1.17-9
- Update to microcode-20101123.dat

* Mon Nov 01 2010 Anton Arapov <anton@redhat.com> 1.17-8
- Update to microcode-20100914.dat

* Wed Sep 29 2010 jkeating - 1:1.17-7
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Anton Arapov <anton@redhat.com> 1.17-6
- Update to microcode-20100826.dat

* Tue Sep 07 2010 Toshio Kuratomi <toshio@fedoraproject.org> 1.17-5
- Fix license tag: bz#450491

* Fri Aug 27 2010 Dave Jones <davej@redhat.com> 1.17-4
- Update to microcode-20100826.dat

* Tue Mar 23 2010 Anton Arapov <anton@redhat.com> 1.17-3
- Fix the udev rules (Harald Hoyer )

* Mon Mar 22 2010 Anton Arapov <anton@redhat.com> 1.17-2
- Make microcode_ctl event driven (Bill Nottingham ) [#479898]

* Thu Feb 11 2010 Dave Jones <davej@redhat.com> 1.17-1.58
- Update to microcode-20100209.dat

* Fri Dec 04 2009 Kyle McMartin <kyle@redhat.com> 1.17-1.57
- Fix duplicate message pointed out by Edward Sheldrake.

* Wed Dec 02 2009 Kyle McMartin <kyle@redhat.com> 1.17-1.56
- Add AMD x86/x86-64 microcode. (Dated: 2009-10-09)
  Doesn't need microcode_ctl modifications as it's loaded by
  request_firmware() like any other sensible driver.
- Eventually, this AMD firmware can probably live inside
  kernel-firmware once it is split out.

* Wed Sep 30 2009 Dave Jones <davej@redhat.com>
- Update to microcode-20090927.dat

* Fri Sep 11 2009 Dave Jones <davej@redhat.com>
- Remove some unnecessary code from the init script.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.17-1.52.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Dave Jones <davej@redhat.com>
- Shorten sleep time during init.
  This really needs to be replaced with proper udev hooks, but this is
  a quick interim fix.

* Wed Jun 03 2009 Kyle McMartin <kyle@redhat.com> 1:1.17-1.50
- Change ExclusiveArch to i586 instead of i386. Resolves rhbz#497711.

* Wed May 13 2009 Dave Jones <davej@redhat.com>
- update to microcode 20090330

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.17-1.46.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Dave Jones <davej@redhat.com>
- update to microcode 20080910

* Tue Apr 01 2008 Jarod Wilson <jwilson@redhat.com>
- Update to microcode 20080401

* Sat Mar 29 2008 Dave Jones <davej@redhat.com>
- Update to microcode 20080220
- Fix rpmlint warnings in specfile.

* Mon Mar 17 2008 Dave Jones <davej@redhat.com>
- specfile cleanups.

* Fri Feb 22 2008 Jarod Wilson <jwilson@redhat.com>
- Use /lib/firmware instead of /etc/firmware

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com>
- Fix permissions on microcode.dat

* Thu Feb 07 2008 Jarod Wilson <jwilson@redhat.com>
- Spec cleanup and macro standardization.
- Update license
- Update microcode data file to 20080131 revision.

* Mon Jul  2 2007 Dave Jones <davej@redhat.com>
- Update to upstream 1.17

* Thu Oct 12 2006 Jon Masters <jcm@redhat.com>
- BZ209455 fixes.

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Fri Jun 16 2006 Bill Nottingham <notting@redhat.com>
- remove kudzu requirement
- add prereq for coreutils, awk, grep

* Thu Feb 09 2006 Dave Jones <davej@redhat.com>
- rebuild.

* Fri Jan 27 2006 Dave Jones <davej@redhat.com>
- Update to upstream 1.13

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Dave Jones <davej@redhat.com>
- initscript tweaks.

* Tue Sep 13 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.12

* Wed Aug 17 2005 Dave Jones <davej@redhat.com>
- Check for device node *after* loading the module. (#157672)

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Thu Feb 17 2005 Dave Jones <davej@redhat.com>
- s/Serial/Epoch/

* Tue Jan 25 2005 Dave Jones <davej@redhat.com>
- Drop the node creation/deletion change from previous release.
  It'll cause grief with selinux, and was a hack to get around
  a udev shortcoming that should be fixed properly.

* Fri Jan 21 2005 Dave Jones <davej@redhat.com>
- Create/remove the /dev/cpu/microcode dev node as needed.
- Use correct path again for the microcode.dat.
- Remove some no longer needed tests in the init script.

* Fri Jan 14 2005 Dave Jones <davej@redhat.com>
- Only enable microcode_ctl service if the CPU is capable.
- Prevent microcode_ctl getting restarted multiple times on initlevel change (#141581)
- Make restart/reload work properly
- Do nothing if not started by root.

* Wed Jan 12 2005 Dave Jones <davej@redhat.com>
- Adjust dev node location. (#144963)

* Tue Jan 11 2005 Dave Jones <davej@redhat.com>
- Load/Remove microcode module in initscript.

* Mon Jan 10 2005 Dave Jones <davej@redhat.com>
- Update to upstream 1.11 release.

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.

