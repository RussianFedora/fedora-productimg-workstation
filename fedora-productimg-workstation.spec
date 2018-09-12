%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/workstation

Name:           fedora-productimg-workstation
Version:        27
Release:        3%{?dist}.R
Summary:        Installer branding and configuration for Fedora Workstation

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        fedora-workstation.css
Source1:        fedora-workstation.py

BuildRequires:  cpio, findutils, xz
BuildRequires:  python3-devel

Provides:       lorax-product-workstation
Conflicts:      fedora-productimg-cloud, fedora-productimg-server

%description
This package contains differentiated branding and configuration for Fedora
Workstation for use in a product.img file for Anaconda, the Fedora
installer. It is not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

install -m 644 %{SOURCE0} %{buildroot}%{pixmaptarget}/../

mkdir -p %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{pixmaptarget}
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{pixmaptarget}

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{pixmaptarget}/sidebar-logo_flavor.png

install -m 755 -d %{buildroot}%{_datadir}/fedora-productimg

pushd %{buildroot}%{_datadir}/lorax/product/
find %{buildroot}%{_datadir}/lorax/product/ -depth -printf '%%P\0' | \
   cpio --null --quiet -H newc -o | \
   xz -9 > \
   %{buildroot}%{_datadir}/fedora-productimg/product.img
popd


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/fedora-workstation.css
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/fedora-workstation.py
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/__pycache__/*
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{_datadir}/lorax/product
%dir %{_datadir}/lorax
%dir %{pixmaptarget}
%{pixmaptarget}/*.png
%dir %{_datadir}/fedora-productimg
%{_datadir}/fedora-productimg/product.img

%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 27-3.R
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-2.R
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Stephen Gallagher <sgallagh@redhat.com> - 27-1
- Bump release for Fedora 27

* Mon Aug 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 23-9
- Own %%{_datadir}/lorax{,/product} dirs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar  9 2017 Arkady L. Shane <ashejn@russianfedora.pro> 23-6.R
- bump release to rebuild

* Wed Mar 16 2016 Arkady L. Shane <ashejn@russianfedora.pro> 23-3.R
- bump release to rebuild

* Thu Jan 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> 23-2.R
- rebuilt

* Sun Oct 25 2015 Arkady L. Shane <ashejn@russianfedora.pro> 23-1.R
- set rfremix env by default

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 23-1
- Switch to Python 3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Adam Williamson <awilliam@redhat.com> - 22-7
- BuildRequire python2-devel so the install class goes to the right place

* Wed Feb 18 2015 Kalev Lember <kalevlember@gmail.com> 22-6
- Create a Fedora Workstation InstallClass object to modify the installer defaults.
- Install the CSS in the proper location so that it can be merged in rather
  than replacing the existing copy.
- Change the default environment group to be Fedora Workstation.

* Wed Nov 26 2014 Matthew Miller <mattdm@fedoraproject.org> 22-5
- correctly pregenerate product.img cpio archive

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-4
- provides lorax-product-workstation

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-3
- merge changes in from f21

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-2
- actually also generate a product.img cpio archive and store
  that in the rpm (for use with livecd-creator or other convenience)

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1 
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- Change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21
