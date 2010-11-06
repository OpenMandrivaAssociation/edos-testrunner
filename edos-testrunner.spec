%define name edos-testrunner
%define version 1.0.4beta
%define release %mkrel 6

%define _unpackaged_files_terminate_build	0
%define _missing_doc_files_terminate_build	0

Summary:	The EDOS Meta Test Runner
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.edos-project.org
License:	GPL
Group:		Development/Python
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
Requires:	python-pyxml
Requires:	python-rpm
Requires:	zip

%description
A test runner that can run any test suite and make reports to an HTTP server,
developped by the EDOS project.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot} --install-scripts=%{buildroot}/usr/bin --install-lib=%{buildroot}/%python_sitelib

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README config/edos-testrunner.cfg.sample tests/test-basic.xml
%python_sitelib/edostestrunner/*.py
%_bindir/edos-runtest
