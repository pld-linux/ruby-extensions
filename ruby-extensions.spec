%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Semi-standard extensions to Ruby
Summary(pl):	Pó³standardowe rozszerzenia dla Ruby
Name:		ruby-extensions
Version:	0.6.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/2144/extensions-%{version}.tgz
# Source0-md5:	f9deb99d623d74b47a536414baa4d1d2
URL:		http://extensions.rubyforge.org/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
extensions provides utilites to assist the process of developing Ruby
programs. At the moment, the target areas are debugging and unit
testing (planned).

%description -l pl
extensions udostêpnia narzêdzia wspomagaj±ce proces rozwoju programów
w Ruby. Obecnie docelowymi obszarami s±: debugowanie i testowanie
modu³ów (w planach).

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

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/rbxtm
%{ruby_rubylibdir}/extensions
# Does not merge well with others.
#%{ruby_ridir}/*
