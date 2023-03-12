Summary:	Bonk lossy/lossless audio coder
Summary(pl.UTF-8):	Stratny i bezstratny koder dźwięku Bonk
Name:		bonk
Version:	0.6
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	https://logarithmic.net/pfh-files/bonk/%{name}-%{version}.tar.gz
# Source0-md5:	e89bfb9c7e985b548e8effc3b059b888
Patch0:		%{name}-c++.patch
URL:		http://www.logarithmic.net/pfh/bonk
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonk is a high quality audio compression program. It can operate in
either lossless or lossy mode. In lossless mode, the exact original
WAV file can be recovered from the compressed file. In lossy mode,
some information is discarded in the compressed file, yielding a much
higher compression ratio. The information discarded is perceptually
unimportant, and the result should be a *perceptually* lossless
encoding.

%description -l pl.UTF-8
Bonk to program do kompresji dźwięku wysokiej jakości. Może działać w
trybie stratnym i bezstratnym. W trybie bezstratnym z pliku
skompresowanego można odtworzyć dokładnie oryginalny plik WAV. W
trybie stratnym część informacji jest tracona, dzięki czemu osiąga
dużo większy współczynnik kompresji. Tracone informacje są zmysłowo
nieistotne, więc wynik powinien być zakodowany *dla słuchu*
bezstratnie.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/bonk
