# Run tests in check section
%bcond_without check

# https://github.com/urfave/cli
%global goipath         github.com/urfave/cli
Version:                1.20.0
%global goipath_v1      gopkg.in/urfave/cli.v1
%global goname_v1       %gorpmname %{goipath_v1}

%global common_description %{expand:
cli is a simple, fast, and fun package for building command line apps in Go. 
The goal is to enable developers to write fast and distributable command line 
applications in an expressive way.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple, fast, and fun package for building command line apps in Go
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         0001-fix-ineffective-assigns.patch

BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(gopkg.in/yaml.v2)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%package -n %{goname_v1}-devel
Summary:    %{summary}
BuildArch:  noarch

%description -n %{goname_v1}-devel
%{common_description}

This package contains compatibility glue for code that imports the
%{goipath_v1} Go namespace.


%prep
%forgeautosetup -p1


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{goipath_v1})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{goipath_v1}


%if %{with check}
%check
%gochecks -d altsrc
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md


%files -n %{goname_v1}-devel
%dir %{gopath}/src/%(dirname %{goipath_v1})
%{gopath}/src/%{goipath_v1}


%changelog
* Wed Oct 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.20.0-1
- Release 1.20.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-0.6.git61f519f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-0.5.git61f519f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-0.4.git61f519f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-0.3.git61f519f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-0.2.git61f519f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.18.0-0.1.git61f519f
- Bump to upstream 61f519fe5e57c2518c03627b194899a105838eba
  related: #1354378

* Wed Jul 27 2016 jchaloup <jchaloup@redhat.com> - 1.17.0-0.2.git6011f16
- enable devel and unit-test for epel7
  related: #1354378 

* Mon Jul 11 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git6011f16
- First package for Fedora
  resolves: #1354378 


