%define 	module	ClientForm

Summary:	Python module for handling HTML forms (on the client side)
Summary(pl):	Modu³ Pythona do obs³ugi formularzy HTML (po stronie klienta)
Name:		python-%{module}
Version:	0.2.6
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	24173e5aee32027f77f688f9e78eaafa
URL:		http://wwwsearch.sourceforge.net/ClientForm/
Requires:	python-modules >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClientForm is a Python module for handling HTML forms on the client
side, useful for parsing HTML forms, filling them in and returning the
completed forms to the server. It developed from a port of Gisle Aas'
Perl module HTML::Form, from the libwww-perl library, but the
interface is not the same.

%description -l pl
ClientForm to modu³ Pythona obs³uguj±cy formularze HTML po stronie
klienta. Przydatny do przetwarzania tych¿e, wype³niania i odsy³ania do
serwera. Zosta³ stworzony na wzór perlowego modu³u HTML::Form
napisanego przez Gislea Aasa, pochodz±cego z biblioteki libwww-perl,
ale jego interfejs (API) jest inny.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean %{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt ChangeLog.txt GeneralFAQ.html README.html
%{py_sitescriptdir}/*.py[co]
#%dir %{py_sitescriptdir}/ClientForm-%{version}-py2.5.egg-info
#%{py_sitescriptdir}/ClientForm-%{version}-py2.5.egg-info/*
