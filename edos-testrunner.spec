%define beta beta

Summary:	The EDOS Meta Test Runner
Name:		edos-testrunner
Version:	1.0.4
Release:	0.%{beta}.1
License:	GPLv2+
Group:		Development/Python
Url:		https://www.edos-project.org
Source0:	http://www.edos-project.org/releases/%{name}-%{version}%{beta}.tar.bz2
BuildRequires:	python
Requires:	python-pyxml
Requires:	python-rpm
Requires:	zip
BuildArch:	noarch

%description
A test runner that can run any test suite and make reports to an HTTP server,
developped by the EDOS project.

%files
%doc README config/edos-testrunner.cfg.sample tests/test-basic.xml
%{_bindir}/edos-runtest
%{python_sitelib}/edostestrunner/*.py
%{python_sitelib}/*.egg-info

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}%{beta}

%build
python setup.py build

%install
python setup.py install \
	--prefix=%{buildroot} \
	--install-scripts=%{buildroot}%{_bindir} \
	--install-lib=%{buildroot}%{python_sitelib}


