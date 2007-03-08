Summary:	Semi-standard extensions to Ruby
Summary(pl.UTF-8):	Półstandardowe rozszerzenia dla Ruby
Name:		ruby-extensions
Version:	0.6.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/2144/extensions-%{version}.tgz
# Source0-md5:	f9deb99d623d74b47a536414baa4d1d2
URL:		http://extensions.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
extensions provides utilites to assist the process of developing Ruby
programs. At the moment, the target areas are debugging and unit
testing (planned).

%description -l pl.UTF-8
extensions udostępnia narzędzia wspomagające proces rozwoju programów
w Ruby. Obecnie docelowymi obszarami są: debugowanie i testowanie
modułów (w planach).

%prep
%setup -q -n extensions-%{version}

%build
ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby install.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/rbxtm
%{ruby_rubylibdir}/extensions
# Does not merge well with others.
#%{ruby_ridir}/*
