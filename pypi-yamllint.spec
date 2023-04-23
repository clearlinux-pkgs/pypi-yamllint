#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-yamllint
Version  : 1.31.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/5f/44/d68632e248a2b64399b5cedcc2ff19ee2f1408cdaca6b57a88c00c65f63e/yamllint-1.31.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/44/d68632e248a2b64399b5cedcc2ff19ee2f1408cdaca6b57a88c00c65f63e/yamllint-1.31.0.tar.gz
Summary  : A linter for YAML files.
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0-only
Requires: pypi-yamllint-bin = %{version}-%{release}
Requires: pypi-yamllint-license = %{version}-%{release}
Requires: pypi-yamllint-python = %{version}-%{release}
Requires: pypi-yamllint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
yamllint
========
A linter for YAML files.
yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%package bin
Summary: bin components for the pypi-yamllint package.
Group: Binaries
Requires: pypi-yamllint-license = %{version}-%{release}

%description bin
bin components for the pypi-yamllint package.


%package license
Summary: license components for the pypi-yamllint package.
Group: Default

%description license
license components for the pypi-yamllint package.


%package python
Summary: python components for the pypi-yamllint package.
Group: Default
Requires: pypi-yamllint-python3 = %{version}-%{release}

%description python
python components for the pypi-yamllint package.


%package python3
Summary: python3 components for the pypi-yamllint package.
Group: Default
Requires: python3-core
Provides: pypi(yamllint)
Requires: pypi(pathspec)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-yamllint package.


%prep
%setup -q -n yamllint-1.31.0
cd %{_builddir}/yamllint-1.31.0
pushd ..
cp -a yamllint-1.31.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682273690
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-yamllint
cp %{_builddir}/yamllint-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-yamllint/31a3d460bb3c7d98845187c716a30db81c44b615 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yamllint

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-yamllint/31a3d460bb3c7d98845187c716a30db81c44b615

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
