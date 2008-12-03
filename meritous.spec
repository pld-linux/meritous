
%define src_ver v12

Summary:	Action-adventure dungeon crawl game
Summary(pl.UTF-8):	Przygodowa gra typu roguelike
Name:		meritous
Version:	1.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://www.asceai.net/files/%{name}_%{src_ver}_src.tar.bz2
# Source0-md5:	88e439c773ee0e334fd2b256100983b8
URL:		http://www.asceai.net/meritous/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meritous is an action-adventure dungeon crawl game.

%description -l pl.UTF-8
Meritious jest przygodową grą typu roguelike.

%prep
%setup -q -n %{name}_%{src_ver}_src
%{__sed} -i -e 's@gcc@\$(CC)@g' Makefile

# chane path to data files (manual installation)
find . -name '*.c' -exec %{__sed} -i -e 's@dat/@%{_datadir}/%{name}/dat/@g' {} \;

%build
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} `sdl-config --cflags`" \
	LDFLAGS="%{rpmldflags} `sdl-config --libs` -lSDL_image -lSDL_mixer -lz"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -r dat $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dat/d/helpfile.txt readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
