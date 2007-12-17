%define name edos-testrunner
%define version 1.0.4beta
%define release %mkrel 1

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
Packager:       Francois Dechelle <fdechelle@mandriva.com>
%py_requires -d
Requires:	python-pyxml
Requires:	python-rpm
Requires:	zip

%description
A test runner that can run any test suite and make reports to an HTTP server, developped by the EDOS project.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot} --install-scripts=%{buildroot}/usr/bin --install-lib=%{buildroot}/%python_sitelib
# Remove unpackage egg-info file
rm -rf %{buildroot}/%python_sitelib/edos_testrunner*.egg-info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README config/edos-testrunner.cfg.sample tests/test-basic.xml
%python_sitelib/edostestrunner/*.py
%python_sitelib/edostestrunner/*.pyc
%_bindir/edos-runtest

%changelog
* Thu May 10 2007 Francois Dechelle <fdechelle@mandriva.com>
- changed Requires and BuildRequires to use %py_requires -d

* Mon May 07 2007 Francois Dechelle <fdechelle@mandriva.com>
- added removal of unpackaged egg-info file

* Wed Apr 04 2007 Francois Dechelle <fdechelle@mandriva.com>
- fixed python version

* Wed Jan 10 2007 Francois Dechelle <fdechelle@mandriva.com>
- moved to setup.py

* Tue Oct 24 2006 Francois Dechelle <fdechelle@mandriva.com>
- initial package

