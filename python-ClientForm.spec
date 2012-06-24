%define 	module	ClientForm

Summary:	Python module for handling HTML forms (on the client side)
Summary(pl):	Modu� Pythona do obs�ugi formularzy HTML (po stronie klienta)
Name:		python-%{module}
Version:	0.1.16
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	b9b18a365ff9625b413fa62cdae75e84
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
ClientForm to modu� Pythona obs�uguj�cy formularze HTML po stronie
klienta. Przydatny do przetwarzania tych�e, wype�niania i odsy�ania do
serwera. Zosta� stworzony na wz�r perlowego modu�u HTML::Form
napisanego przez Gislea Aasa, pochodz�cego z biblioteki libwww-perl,
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

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog GeneralFAQ.html INSTALL README.html
%{py_sitescriptdir}/*.py[co]
