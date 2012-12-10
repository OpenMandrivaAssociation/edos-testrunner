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


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.0.4beta-6mdv2011.0
+ Revision: 593870
- fix file list

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4beta-5mdv2010.0
+ Revision: 437377
- rebuild

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.0.4beta-4mdv2009.1
+ Revision: 333260
- bump rel

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + François Déchelle <fdechelle@mandriva.org>
    - * I messed up the release number

* Thu May 24 2007 François Déchelle <fdechelle@mandriva.org> 1.0.4beta-4mdv2008.0
+ Revision: 30676
- * fixed utf8 problem

* Thu May 10 2007 François Déchelle <fdechelle@mandriva.org> 1.0.3beta-4mdv2008.0
+ Revision: 26077
- changed requires and buildrequires to use %%py_requires

* Thu May 10 2007 François Déchelle <fdechelle@mandriva.org> 1.0.3beta-3mdv2008.0
+ Revision: 26054
- Fixing 64bits build problem
- Commited first package of edos-testrunner
- builds with iurt
- Create edos-testrunner

