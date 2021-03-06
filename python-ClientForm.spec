%define 	module	ClientForm
Summary:	Python module for handling HTML forms (on the client side)
Summary(pl.UTF-8):	Moduł Pythona do obsługi formularzy HTML (po stronie klienta)
Name:		python-%{module}
Version:	0.2.10
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	832c0ca78674f9263d1fc5fab8756e66
URL:		http://wwwsearch.sourceforge.net/ClientForm/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClientForm is a Python module for handling HTML forms on the client
side, useful for parsing HTML forms, filling them in and returning the
completed forms to the server. It developed from a port of Gisle Aas'
Perl module HTML::Form, from the libwww-perl library, but the
interface is not the same.

%description -l pl.UTF-8
ClientForm to moduł Pythona obsługujący formularze HTML po stronie
klienta. Przydatny do przetwarzania tychże, wypełniania i odsyłania do
serwera. Został stworzony na wzór perlowego modułu HTML::Form
napisanego przez Gislea Aasa, pochodzącego z biblioteki libwww-perl,
ale jego interfejs (API) jest inny.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean %{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt ChangeLog.txt GeneralFAQ.html README.html
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/ClientForm-*.egg-info
%endif
