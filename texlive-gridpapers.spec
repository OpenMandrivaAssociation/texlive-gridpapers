Name:		texlive-gridpapers
Version:	58723
Release:	2
Summary:	Graph paper backgrounds and color schemes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gridpapers
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridpapers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridpapers.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridpapers.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides many preset yet customizable graph paper
backgrounds. Some of the preset patterns include standard
quadrille or graph pattern, dot grid, hexagons, isometric or
triangular grid, squares with 45deg "light cone" lines, ruled,
and more. Pattern sizes can be controlled via package options.
There are several preset color palletes, and colors can be
overridden. The package uses the PGF/TikZ package, and the
geometry package to control page size.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gridpapers
%{_texmfdistdir}/tex/latex/gridpapers
%doc %{_texmfdistdir}/doc/latex/gridpapers

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
