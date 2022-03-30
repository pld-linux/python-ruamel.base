#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		_enable_debug_packages	0

%define		module		ruamel.base
Summary:	Common routines for ruamel packages
Summary(pl.UTF-8):	Wspólne funkcje dla pakietów ruamel
Name:		python-%{module}
Version:	1.0.0
Release:	7
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.base/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.base/%{module}-%{version}.tar.gz
# Source0-md5:	5b2fb0e7df10672eb2a48dc329f770ee
URL:		https://pypi.org/project/ruamel.base/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 2
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common routines for ruamel packages.

%description -l pl.UTF-8
Wspólne funkcje dla pakietów ruamel.

%package -n python3-%{module}
Summary:	Common routines for ruamel packages
Summary(pl.UTF-8):	Wspólne funkcje dla pakietów ruamel
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Common routines for ruamel packages.

%description -n python3-%{module} -l pl.UTF-8
Wspólne funkcje dla pakietów ruamel.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitedir}/ruamel

%py_install

%py_postclean
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitedir}/ruamel

%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py_sitescriptdir}/ruamel
%{py_sitescriptdir}/ruamel/base
%{py_sitescriptdir}/ruamel.base-%{version}-py*.egg-info
%{py_sitescriptdir}/ruamel.base-%{version}-py*-nspkg.pth
%dir %{py_sitedir}/ruamel
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py3_sitescriptdir}/ruamel
%{py3_sitescriptdir}/ruamel/base
%{py3_sitescriptdir}/ruamel.base-%{version}-py*.egg-info
%{py3_sitescriptdir}/ruamel.base-%{version}-py*-nspkg.pth
%dir %{py3_sitedir}/ruamel
%endif
