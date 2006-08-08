#
%bcond_without	x	# without X11 graphics support
#
Summary:	Icon programming language
Summary(pl):	Jêzyk programowania Icon
Name:		icon
Version:	9.4.1
%define	sver	%(echo %{version} | tr -d .)
Release:	2
License:	Public Domain (see README)
Group:		Development/Languages
Source0:	http://www.cs.arizona.edu/icon/ftp/packages/unix/%{name}.v%{sver}src.tgz
# Source0-md5:	5ab62c32eb0d20fa6ee5840dd88a09f6
Patch0:		%{name}-system-Xpm.patch
Patch1:		%{name}-paths.patch
URL:		http://www.cs.arizona.edu/icon/
%{?with_x:BuildRequires:	XFree86-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon is a very high level general-purpose programming language with
extensive features for processing strings (text) and data structures.
Icon is an imperative, procedural language with a syntax that is
reminiscent of C and Pascal, but with semantics at a much higher
level.

%description -l pl
Icon to jêzyk programowania ogólnego przeznaczenia bardzo wysokiego
poziomu z du¿ymi mo¿liwo¶ciami przetwarzania ³añcuchów (tekstu) i
struktur danych. Icon jest imperatywnym, proceduralnym jêzykiem ze
sk³adni± przypominaj±c± C i Pascala, ale z semantyk± na du¿o wy¿szym
poziomie.

%prep
%setup -q -n %{name}.v%{sver}src
%patch0 -p1

%build
%{__make} %{?with_x:X-}Configure \
	name=linux

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	XLIBS="-L/usr/X11R6/%{_lib} -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/icon/{bin,lib}}

install bin/* $RPM_BUILD_ROOT%{_libdir}/icon/bin
install lib/* $RPM_BUILD_ROOT%{_libdir}/icon/lib

for f in icon icont iconx vib ; do
	ln -sf %{_libdir}/icon/bin/$f $RPM_BUILD_ROOT%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.{txt,htm,css,gif,jpg}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/icon
%dir %{_libdir}/icon/bin
%attr(755,root,root) %{_libdir}/icon/bin/[!r]*
%attr(755,root,root) %{_libdir}/icon/bin/rtt
%{_libdir}/icon/bin/rt.h
%{_libdir}/icon/lib
