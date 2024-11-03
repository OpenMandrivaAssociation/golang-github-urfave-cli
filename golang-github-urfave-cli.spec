%bcond_with bootstrap2

%global debug_package %{nil}

# Run tests in check section
# We currently don't package all dependencies of the tests
%bcond_with check

# https://github.com/urfave/cli
%global goipath		github.com/urfave/cli
%global forgeurl	https://github.com/urfave/cli
Version:			2.27.5

%gometa

Summary:	Simple, fast, and fun package for building command line apps in go
Name:		golang-github-urfave-cli

Release:	1
Source0:	https://github.com/urfave/cli/archive/v%{version}/cli-%{version}.tar.gz
%if %{with bootstrap2}
# Generated from Source100
Source3:	vendor.tar.zst
Source100:	golang-package-dependencies.sh
%endif
URL:		https://github.com/urfave/cli
License:	GPL
Group:		Development/Other

BuildRequires:	compiler(go-compiler)
%if ! %{with bootstrap2}
BuildRequires:	golang(github.com/BurntSushi/toml)
BuildRequires:	golang(github.com/cpuguy83/go-md2man/v2/md2man)
BuildRequires:	golang(gopkg.in/yaml.v2)
%endif

%description
Cli is a simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc docs/CONTRIBUTING.md docs/v1 README.md CODE_OF_CONDUCT.md

#-----------------------------------------------------------------------

%prep
%autosetup -n cli-%{version}

rm -rf vendor

%if %{with bootstrap2}
tar xf %{S:3}
%endif

%build
export GO111MODULE=off
#gobuildroot

%install
export GO111MODULE=off
%goinstall

%check
%if %{with check}
%gochecks
%endif
